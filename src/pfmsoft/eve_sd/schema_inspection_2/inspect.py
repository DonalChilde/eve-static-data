"""Schema inspection pipeline that produces a FieldSchema tree."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any, Literal, cast

from whenever import Instant

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata
from pfmsoft.eve_sd.schema_inspection_2.models import (
    DatasetSchema,
    FieldSchema,
    SchemaReport2,
)

# ── internal traversal nodes ──────────────────────────────────────────────────


@dataclass(slots=True, kw_only=True)
class _ListStats:
    item_count: int = 0
    item_type_counts: Counter[str] = field(default_factory=Counter)
    empty_list_count: int = 0
    item_node: _FieldNode = field(default_factory=lambda: _FieldNode())


@dataclass(slots=True, kw_only=True)
class _FieldNode:
    presence_count: int = 0
    value_type_counts: Counter[str] = field(default_factory=Counter)
    # tracks key types of this dict's children to detect dynamic-key mappings
    child_key_types: Counter[str] = field(default_factory=Counter)
    children: dict[str, _FieldNode] = field(default_factory=dict)
    list_stats: _ListStats | None = None


# ── public input type ─────────────────────────────────────────────────────────


@dataclass(slots=True, kw_only=True)
class DatasetInput:
    """Input for one normalized dataset."""

    dataset_name: str
    dataset_data: dict[int | str, Any]
    sde_metadata: SdeMetadata


# ── traversal helpers ─────────────────────────────────────────────────────────


def _sde_type_name(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        return "list"
    return "dict"


def _mapping_items(value: Any) -> list[tuple[object, object]]:
    return list(cast(dict[object, object], value).items())


def _sequence_items(value: Any) -> list[object]:
    return list(cast(list[object], value))


def _is_int_key(key: object) -> bool:
    if isinstance(key, int):
        return True
    if isinstance(key, str):
        try:
            int(key)
            return True
        except ValueError:
            return False
    return False


def _append_warning(warnings: list[str], message: str) -> None:
    if message not in warnings:
        warnings.append(message)


def _update_node_from_value(node: _FieldNode, value: Any) -> None:
    type_name = _sde_type_name(value)
    node.value_type_counts[type_name] += 1

    if isinstance(value, dict):
        for child_name, child_value in _mapping_items(value):
            node.child_key_types["int" if _is_int_key(child_name) else "str"] += 1
            child_key = str(child_name)
            child_node = node.children.setdefault(child_key, _FieldNode())
            child_node.presence_count += 1
            _update_node_from_value(child_node, child_value)
        return

    if not isinstance(value, list):
        return

    list_stats = node.list_stats
    if list_stats is None:
        list_stats = _ListStats()
        node.list_stats = list_stats

    if not value:
        list_stats.empty_list_count += 1
        return

    for item in _sequence_items(value):
        item_type = _sde_type_name(item)
        list_stats.item_count += 1
        list_stats.item_type_counts[item_type] += 1
        if isinstance(item, dict):
            list_stats.item_node.presence_count += 1
            _update_node_from_value(list_stats.item_node, item)


# ── tree conversion helpers ───────────────────────────────────────────────────


def _split_nullable(type_counts: Counter[str]) -> tuple[bool, list[str]]:
    nullable = type_counts.get("null", 0) > 0
    types = sorted(k for k in type_counts if k != "null")
    return nullable, types


def _derive_key_type(
    child_key_types: Counter[str],
) -> Literal["int", "str"] | None:
    total = sum(child_key_types.values())
    if total == 0:
        return None
    # classify as dynamic-int-key mapping when >90% of observed keys are integers
    if child_key_types.get("int", 0) / total > 0.9:
        return "int"
    return None


def _convert_children(
    parent_path: str,
    child_nodes: dict[str, _FieldNode],
    container_count: int,
    ancestor_required: bool,
    dataset_warnings: list[str],
) -> dict[str, FieldSchema]:
    return {
        child_name: _node_to_field_schema(
            path=f"{parent_path}.{child_name}",
            name=child_name,
            node=child_node,
            container_count=container_count,
            ancestor_required=ancestor_required,
            dataset_warnings=dataset_warnings,
        )
        for child_name, child_node in sorted(child_nodes.items())
    }


def _node_to_field_schema(
    path: str,
    name: str,
    node: _FieldNode,
    container_count: int,
    ancestor_required: bool,
    dataset_warnings: list[str],
) -> FieldSchema:
    local_required = container_count > 0 and node.presence_count >= container_count
    required = ancestor_required and local_required
    nullable, value_types = _split_nullable(node.value_type_counts)
    key_type = _derive_key_type(node.child_key_types)

    field_warnings: list[str] = []
    container_types = {"dict", "list"}
    scalar_types = set(node.value_type_counts) - container_types - {"null"}
    if container_types & set(node.value_type_counts) and scalar_types:
        type_summary = ", ".join(
            f"{k}:{v}" for k, v in sorted(node.value_type_counts.items())
        )
        msg = f"{path}: mixes container and scalar types ({type_summary})"
        _append_warning(dataset_warnings, msg)
        field_warnings.append("mixes container and scalar types")

    list_stats = node.list_stats
    list_item_types: list[str] = []
    children: dict[str, FieldSchema] = {}

    if list_stats is not None:
        if list_stats.empty_list_count:
            suffix = "s" if list_stats.empty_list_count != 1 else ""
            _append_warning(
                dataset_warnings,
                f"{path}: {list_stats.empty_list_count} empty list{suffix}",
            )
        if len(list_stats.item_type_counts) > 1:
            item_summary = ", ".join(
                f"{k}:{v}" for k, v in sorted(list_stats.item_type_counts.items())
            )
            _append_warning(
                dataset_warnings,
                f"{path}: list has mixed item types ({item_summary})",
            )

        _, all_item_types = _split_nullable(Counter(list_stats.item_type_counts))
        list_item_types = [t for t in all_item_types if t != "dict"]

        dict_in_list = list_stats.item_type_counts.get("dict", 0)
        if list_stats.item_node.children and dict_in_list:
            # list-of-dict: children are the item record schema
            children = _convert_children(
                path,
                list_stats.item_node.children,
                dict_in_list,
                True,
                dataset_warnings,
            )

    dict_count = node.value_type_counts.get("dict", 0)
    if node.children and dict_count and not children:
        # dict field: children are the record fields (or dynamic-key mapping values)
        children = _convert_children(
            path,
            node.children,
            dict_count,
            required,
            dataset_warnings,
        )

    return FieldSchema(
        name=name,
        required=required,
        nullable=nullable,
        value_types=value_types,
        key_type=key_type,
        list_item_types=list_item_types,
        children=children,
        presence_count=node.presence_count,
        container_count=container_count,
        warnings=field_warnings,
    )


# ── public API ────────────────────────────────────────────────────────────────


def inspect_dataset_data(
    dataset_name: str,
    dataset_data: dict[int | str, Any],
    sde_metadata: SdeMetadata,
    *,
    dataset_source: str | None = None,
) -> DatasetSchema:
    """Inspect one normalized dataset and return a FieldSchema tree.

    Args:
        dataset_name: Logical name for the dataset.
        dataset_data: Normalized mapping of record keys to record dicts.
        sde_metadata: SDE metadata for the dataset.
        dataset_source: Optional display label for the source.

    Returns:
        DatasetSchema with a nested FieldSchema tree for all discovered fields.
    """
    dataset_source = dataset_source or dataset_name
    dataset_warnings: list[str] = []
    root_fields: dict[str, _FieldNode] = {}
    int_key_count = 0
    str_key_count = 0
    total_records = len(dataset_data)
    valid_record_count = 0
    skipped_record_count = 0

    for record_key, record_value in dataset_data.items():
        if _is_int_key(record_key):
            int_key_count += 1
        else:
            str_key_count += 1

        if not isinstance(record_value, dict):
            skipped_record_count += 1
            _append_warning(
                dataset_warnings,
                (
                    f"Top-level key {record_key!r} has non-dict value "
                    f"{_sde_type_name(record_value)}; skipped"
                ),
            )
            continue

        valid_record_count += 1
        for field_name, field_value in _mapping_items(record_value):
            node = root_fields.setdefault(str(field_name), _FieldNode())
            node.presence_count += 1
            _update_node_from_value(node, field_value)

    record_key_type: Literal["int", "str"] = (
        "int" if int_key_count >= str_key_count else "str"
    )

    fields = {
        field_name: _node_to_field_schema(
            path=field_name,
            name=field_name,
            node=node,
            container_count=valid_record_count,
            ancestor_required=True,
            dataset_warnings=dataset_warnings,
        )
        for field_name, node in sorted(root_fields.items())
    }

    return DatasetSchema(
        dataset_name=dataset_name,
        dataset_source=dataset_source,
        sde_metadata=sde_metadata,
        record_key_type=record_key_type,
        total_records=total_records,
        valid_record_count=valid_record_count,
        skipped_record_count=skipped_record_count,
        fields=fields,
        warnings=dataset_warnings,
    )


def build_schema_report(
    datasets: Iterable[DatasetInput],
    sde_metadata: SdeMetadata,
    *,
    dataset_source: str,
) -> SchemaReport2:
    """Build a schema report from multiple normalized datasets.

    Args:
        datasets: Iterable of DatasetInput instances.
        sde_metadata: SDE metadata for the report summary.
        dataset_source: Display label for the aggregate source.

    Returns:
        SchemaReport2 containing a DatasetSchema tree for each dataset.
    """
    inspected: list[DatasetSchema] = []
    for di in datasets:
        inspected.append(
            inspect_dataset_data(
                dataset_name=di.dataset_name,
                dataset_data=di.dataset_data,
                sde_metadata=di.sde_metadata,
                dataset_source=dataset_source,
            )
        )

    sorted_datasets = sorted(inspected, key=lambda d: d.dataset_name)
    return SchemaReport2(
        source_path=dataset_source,
        generated_at_utc=Instant.now().format_iso(),
        sde_metadata=sde_metadata,
        file_count=len(sorted_datasets),
        total_records=sum(d.total_records for d in sorted_datasets),
        datasets={d.dataset_name: d for d in sorted_datasets},
    )
