"""Dataclass models for schema inspection v2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata


@dataclass(slots=True, kw_only=True)
class FieldSchema:
    """Nested schema description of one field observed during inspection.

    Children represent sub-fields of a dict-valued field or the item schema
    of a list-of-dict field.  When key_type is set the children are values of a
    dynamic mapping rather than fixed record fields.
    """

    name: str
    required: bool
    nullable: bool
    value_types: list[str]  # sorted; null is separated into nullable
    key_type: Literal["int", "str"] | None  # None = fixed record; set = dynamic mapping
    list_item_types: list[str]  # scalar types when field is list[scalar]
    children: dict[str, FieldSchema]  # sub-fields (fixed record or list-item schema)
    presence_count: int
    container_count: int
    warnings: list[str] = field(default_factory=list)


@dataclass(slots=True, kw_only=True)
class DatasetSchema:
    """Observed schema for one normalized dataset."""

    dataset_name: str
    dataset_source: str
    sde_metadata: SdeMetadata
    record_key_type: Literal["int", "str"]
    total_records: int
    valid_record_count: int
    skipped_record_count: int
    fields: dict[str, FieldSchema]
    warnings: list[str]


@dataclass(slots=True, kw_only=True)
class SchemaReport2:
    """Top-level schema report (v2) for one or more datasets."""

    source_path: str
    generated_at_utc: str
    sde_metadata: SdeMetadata
    file_count: int
    total_records: int
    datasets: dict[str, DatasetSchema]


# ── type derivation helpers ────────────────────────────────────────────────────


def _widen_value_types(types: list[str]) -> str:
    """Return a minimal Python type string from a list of observed primitive types."""
    if not types:
        return "Any"
    # int is a subtype of float; widen to float when both present
    widened = [t for t in types if not (t == "int" and "float" in types)]
    if len(widened) == 1:
        return widened[0]
    return " | ".join(widened)


def _to_class_name(name: str) -> str:
    """Convert a camelCase or snake_case field name to PascalCase."""
    if "_" in name:
        return "".join(part.capitalize() for part in name.split("_"))
    return (name[0].upper() + name[1:]) if name else "Field"


def canonical_type(field_schema: FieldSchema) -> str:
    """Derive a Python type annotation string from a FieldSchema.

    Args:
        field_schema: The field to derive the type for.

    Returns:
        A Python type annotation such as ``str``, ``list[int]``,
        ``NameModel | None``, etc.
    """
    class_name = _to_class_name(field_schema.name)

    if "list" in field_schema.value_types:
        if field_schema.children:
            base = f"list[{class_name}Item]"
        elif field_schema.list_item_types:
            base = f"list[{_widen_value_types(field_schema.list_item_types)}]"
        else:
            base = "list[Any]"
    elif field_schema.children:
        if field_schema.key_type == "int":
            base = f"dict[int, {class_name}Value]"
        elif field_schema.key_type == "str":
            base = f"dict[str, {class_name}Value]"
        else:
            base = class_name
    else:
        base = _widen_value_types(field_schema.value_types)

    return f"{base} | None" if field_schema.nullable else base


def flat_fields(
    fields: dict[str, FieldSchema],
    prefix: str = "",
) -> list[tuple[str, FieldSchema]]:
    """Flatten a FieldSchema tree into (dotted_path, schema) pairs for rendering.

    Dynamic-key dict children are not recursed into because their children
    represent values in a mapping, not fixed record fields.

    Args:
        fields: Top-level field name → FieldSchema mapping.
        prefix: Accumulated dotted path prefix.

    Returns:
        Ordered list of (path, schema) tuples in tree order.
    """
    result: list[tuple[str, FieldSchema]] = []
    for name in sorted(fields):
        schema = fields[name]
        path = f"{prefix}.{name}" if prefix else name
        result.append((path, schema))
        # recurse into fixed-record children; skip dynamic-key mapping children
        if schema.children and schema.key_type is None:
            result.extend(flat_fields(schema.children, path))
    return result
