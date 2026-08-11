"""Dataclass model code generation from SchemaReport."""

import logging
from dataclasses import dataclass

from jinja2 import Environment, PackageLoader

from pfmsoft.eve_sd.schema_inspection.models import (
    DatasetSchema,
    FieldSchema,
    SchemaReport,
    _to_class_name,
    _widen_value_types,
)

logger = logging.getLogger(__name__)


@dataclass(slots=True, kw_only=True)
class _FieldDef:
    field_name: str
    type_annotation: str
    # True when field is not required in source data; template emits = None
    has_default: bool


@dataclass(slots=True, kw_only=True)
class _ClassDef:
    class_name: str
    fields: list[_FieldDef]


# ── public name derivation ────────────────────────────────────────────────────


def to_record_class_name(dataset_name: str) -> str:
    """Convert a dataset name to a PascalCase record class name.

    Args:
        dataset_name: The dataset name (e.g. ``accountingEntryTypes``).

    Returns:
        PascalCase class name with ``Record`` suffix
        (e.g. ``AccountingEntryTypesRecord``).
    """
    return _to_class_name(dataset_name) + "Record"


def to_nested_class_name(parent_class_name: str, *, field_name: str) -> str:
    """Return the global class name for a nested field's dataclass.

    Args:
        parent_class_name: Class name of the enclosing dataclass.
        field_name: Snake or camelCase field name.

    Returns:
        ``{parent_class_name}_{PascalCase(field_name)}``.
    """
    return parent_class_name + "_" + _to_class_name(field_name)


def to_item_class_name(parent_class_name: str, *, field_name: str) -> str:
    """Return the global class name for list-of-dict item dataclasses.

    Args:
        parent_class_name: Class name of the enclosing dataclass.
        field_name: Snake or camelCase field name.

    Returns:
        ``{parent_class_name}_{PascalCase(field_name)}Item``.
    """
    return to_nested_class_name(parent_class_name, field_name=field_name) + "Item"


# ── type annotation derivation ────────────────────────────────────────────────


def codegen_type(field_schema: FieldSchema, parent_class_name: str) -> str:
    """Derive a Python type annotation string for use in generated dataclasses.

    Unlike ``canonical_type``, nested class names are qualified with the parent
    class prefix and non-required fields are typed as ``X | None``.

    Args:
        field_schema: The field to derive the type for.
        parent_class_name: Enclosing class name used to build nested class names.

    Returns:
        A Python type annotation string.
    """
    name = field_schema.name

    if "list" in field_schema.value_types:
        if field_schema.children:
            base = f"list[{to_item_class_name(parent_class_name, field_name=name)}]"
        elif field_schema.list_item_types:
            base = f"list[{_widen_value_types(field_schema.list_item_types)}]"
        else:
            base = "list[Any]"
    elif field_schema.children:
        nested = to_nested_class_name(parent_class_name, field_name=name)
        # non-identifier children are enumerated mapping keys, not struct fields
        has_struct_children = all(c.isidentifier() for c in field_schema.children)
        if field_schema.key_type == "int":
            base = f"dict[int, {nested}]" if has_struct_children else "dict[int, Any]"
        elif field_schema.key_type == "str":
            base = f"dict[str, {nested}]" if has_struct_children else "dict[str, Any]"
        else:
            base = nested
    elif field_schema.key_type is not None:
        # scalar dynamic mapping — key_type set but no dict children
        key = "int" if field_schema.key_type == "int" else "str"
        base = f"dict[{key}, Any]"
    else:
        base = _widen_value_types(field_schema.value_types)

    # non-required fields also get | None so they can safely default to None
    optional = field_schema.nullable or not field_schema.required
    return f"{base} | None" if optional else base


# ── class tree collection ─────────────────────────────────────────────────────


def _collect_field_classes(
    *,
    field_schema: FieldSchema,
    field_name: str,
    parent_class_name: str,
    result: list[_ClassDef],
    dataset_name: str,
) -> None:
    if not field_schema.children:
        if field_schema.key_type is not None:
            logger.warning(
                "Dataset %r field %r is a scalar dynamic mapping "
                "(key_type=%r) — no class generated; full dataset coverage "
                "requires manual handling",
                dataset_name,
                field_name,
                field_schema.key_type,
            )
        return

    # When key_type is set, children should be value-struct fields (valid identifiers).
    # If any child name is not a valid identifier, they are enumerated mapping keys
    # (e.g. "100", "2103") with scalar values — cannot generate a dataclass.
    if field_schema.key_type is not None and not all(
        child.isidentifier() for child in field_schema.children
    ):
        logger.warning(
            "Dataset %r field %r has a dynamic mapping with non-identifier keys "
            "(%r ...) — no class generated; full dataset coverage requires manual handling",
            dataset_name,
            field_name,
            next(iter(field_schema.children)),
        )
        return

    if "list" in field_schema.value_types:
        class_name = to_item_class_name(parent_class_name, field_name=field_name)
    else:
        class_name = to_nested_class_name(parent_class_name, field_name=field_name)

    child_fields: list[_FieldDef] = []
    for child_name, child_schema in field_schema.children.items():
        if not child_name.isidentifier():
            logger.warning(
                "Dataset %r field %r.%r is not a valid Python identifier — "
                "skipped in generated dataclass; full dataset coverage requires manual handling",
                dataset_name,
                field_name,
                child_name,
            )
            continue
        # recurse children-first so nested classes are defined before parents
        _collect_field_classes(
            field_schema=child_schema,
            field_name=child_name,
            parent_class_name=class_name,
            result=result,
            dataset_name=dataset_name,
        )
        child_fields.append(
            _FieldDef(
                field_name=child_name,
                type_annotation=codegen_type(child_schema, class_name),
                has_default=not child_schema.required,
            )
        )

    # required fields before optionals; both groups sorted by name
    child_fields.sort(key=lambda f: (f.has_default, f.field_name))
    result.append(_ClassDef(class_name=class_name, fields=child_fields))


def collect_classes(
    dataset_schema: DatasetSchema,
    *,
    record_class_name: str,
) -> list[_ClassDef]:
    """Walk a DatasetSchema tree and return ClassDef nodes in definition order.

    Nested classes appear before the classes that reference them, so the
    generated source requires no forward references.  A ``logger.warning`` is
    emitted for any scalar dynamic-mapping field that cannot be modelled as a
    dataclass.

    Args:
        dataset_schema: Schema for one dataset.
        record_class_name: Class name for the top-level record dataclass.

    Returns:
        Ordered list of class descriptor nodes; the record class is last.
    """
    result: list[_ClassDef] = []
    record_fields: list[_FieldDef] = []

    for field_name, field_schema in dataset_schema.fields.items():
        _collect_field_classes(
            field_schema=field_schema,
            field_name=field_name,
            parent_class_name=record_class_name,
            result=result,
            dataset_name=dataset_schema.dataset_name,
        )
        if not field_name.isidentifier():
            logger.warning(
                "Dataset %r: field name %r is not a valid Python identifier — "
                "skipped in generated dataclass; full dataset coverage requires manual handling",
                dataset_schema.dataset_name,
                field_name,
            )
            continue
        record_fields.append(
            _FieldDef(
                field_name=field_name,
                type_annotation=codegen_type(field_schema, record_class_name),
                has_default=not field_schema.required,
            )
        )

    record_fields.sort(key=lambda f: (f.has_default, f.field_name))
    result.append(_ClassDef(class_name=record_class_name, fields=record_fields))
    return result


# ── rendering ─────────────────────────────────────────────────────────────────


def _build_environment() -> Environment:
    return Environment(
        loader=PackageLoader("pfmsoft.eve_sd", "templates"),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )


def generate_record_models(report: SchemaReport) -> str:
    """Generate Python dataclass source for all dataset record types in a schema report.

    Args:
        report: Schema report produced by schema inspection.

    Returns:
        Python source string with one dataclass per dataset record type and all
        required nested types. The output is not formatted; formatting is the
        caller's responsibility.
    """
    classes_by_dataset = {
        dataset_name: collect_classes(
            schema, record_class_name=to_record_class_name(dataset_name)
        )
        for dataset_name, schema in sorted(report.datasets.items())
    }
    env = _build_environment()
    template = env.get_template("codegen/dataclass_models.j2")
    return template.render(report=report, classes_by_dataset=classes_by_dataset)
