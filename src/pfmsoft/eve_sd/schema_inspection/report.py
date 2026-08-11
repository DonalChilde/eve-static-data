"""Schema inspection pipeline for normalized SDE datasets."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any, Literal, cast

from whenever import Instant

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata
from pfmsoft.eve_sd.schema_inspection.models import (
    DatasetInspection,
    FieldNode,
    ListStats,
    PathInspection,
    SchemaReport,
)

SdeTypeName = Literal["dict", "list", "str", "int", "float", "bool", "null"]
SdeFormat = Literal["yaml-model", "jsonl-model"]


@dataclass(slots=True, kw_only=True)
class DatasetInput:
    """Input for one normalized dataset."""

    dataset_name: str
    dataset_data: dict[int | str, Any]
    sde_metadata: SdeMetadata


def _string_counter() -> Counter[str]:
    return Counter()


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


def _top_level_key_bucket(key: object) -> str:
    return "INTEGER_KEY" if isinstance(key, int) else "STRING_KEY"


def _sorted_type_counts(type_counts: dict[str, int]) -> dict[str, int]:
    keys = sorted(type_counts)
    return {key: type_counts[key] for key in keys}


def _append_warning(warnings: list[str], message: str) -> None:
    if message not in warnings:
        warnings.append(message)


def _update_node_from_value(node: FieldNode, value: Any) -> None:
    type_name = _sde_type_name(value)
    node.value_type_counts[type_name] += 1

    if isinstance(value, dict):
        for child_name, child_value in _mapping_items(value):
            child_key = str(child_name)
            child_node = node.children.setdefault(child_key, FieldNode())
            child_node.presence_count += 1
            _update_node_from_value(child_node, child_value)
        return

    if not isinstance(value, list):
        return

    list_stats = node.list_stats
    if list_stats is None:
        list_stats = ListStats()
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


def _flatten_field_rows(
    fields: dict[str, FieldNode],
    container_count: int,
    prefix: str = "",
    ancestor_required: bool = True,
) -> dict[str, PathInspection]:
    rows: dict[str, PathInspection] = {}

    for field_name in sorted(fields):
        field_data = fields[field_name]
        path = f"{prefix}.{field_name}" if prefix else field_name
        local_required = (
            container_count > 0 and field_data.presence_count >= container_count
        )
        required = ancestor_required and local_required
        rows[path] = PathInspection(
            path=path,
            presence_count=field_data.presence_count,
            container_count=container_count,
            required=required,
            value_type_counts=_sorted_type_counts(dict(field_data.value_type_counts)),
        )

        dict_count = field_data.value_type_counts.get("dict", 0)
        if field_data.children and dict_count:
            rows.update(
                _flatten_field_rows(
                    fields=field_data.children,
                    container_count=dict_count,
                    prefix=path,
                    ancestor_required=required,
                )
            )

        list_stats = field_data.list_stats
        list_dict_count = 0
        if list_stats is not None:
            list_dict_count = list_stats.item_type_counts.get("dict", 0)

        if list_stats is not None and list_stats.item_node.children and list_dict_count:
            rows.update(
                _flatten_field_rows(
                    fields=list_stats.item_node.children,
                    container_count=list_dict_count,
                    prefix=path,
                    ancestor_required=required,
                )
            )

    return rows


def _collect_node_warnings(path: str, node: FieldNode, warnings: list[str]) -> None:
    container_types = {"dict", "list"}
    scalar_types = set(node.value_type_counts) - container_types
    if container_types & set(node.value_type_counts) and scalar_types:
        type_summary = ", ".join(
            f"{name}:{count}"
            for name, count in _sorted_type_counts(dict(node.value_type_counts)).items()
        )
        _append_warning(
            warnings,
            f"{path}: path mixes container and scalar types ({type_summary})",
        )

    list_stats = node.list_stats
    if list_stats is not None:
        if list_stats.empty_list_count:
            suffix = "s" if list_stats.empty_list_count != 1 else ""
            _append_warning(
                warnings,
                f"{path}: encountered {list_stats.empty_list_count} empty list{suffix}",
            )
        if len(list_stats.item_type_counts) > 1:
            item_summary = ", ".join(
                f"{name}:{count}"
                for name, count in _sorted_type_counts(
                    dict(list_stats.item_type_counts)
                ).items()
            )
            _append_warning(
                warnings,
                f"{path}: list contains mixed item types ({item_summary})",
            )

    for child_name in sorted(node.children):
        child_path = f"{path}.{child_name}" if path else child_name
        _collect_node_warnings(child_path, node.children[child_name], warnings)

    if list_stats is None:
        return

    for child_name in sorted(list_stats.item_node.children):
        child_path = f"{path}.{child_name}" if path else child_name
        _collect_node_warnings(
            child_path, list_stats.item_node.children[child_name], warnings
        )


def inspect_dataset_data(
    dataset_name: str,
    dataset_data: dict[int | str, Any],
    sde_metadata: SdeMetadata,
    *,
    dataset_source: str | None = None,
) -> DatasetInspection:
    """Inspect one normalized dataset mapping."""
    warnings: list[str] = []
    root_fields: dict[str, FieldNode] = {}
    top_level_key_type_counts: Counter[str] = _string_counter()
    dataset_source = dataset_source or dataset_name

    total_records = len(dataset_data)
    valid_record_count = 0
    skipped_record_count = 0

    for record_key, record_value in dataset_data.items():
        top_level_key_type_counts[_top_level_key_bucket(record_key)] += 1
        if not isinstance(record_value, dict):
            skipped_record_count += 1
            _append_warning(
                warnings,
                (
                    f"Top-level key {record_key!r} has non-dict value "
                    f"{_sde_type_name(record_value)}; skipped"
                ),
            )
            continue

        valid_record_count += 1
        for field_name, field_value in _mapping_items(record_value):
            node = root_fields.setdefault(str(field_name), FieldNode())
            node.presence_count += 1
            _update_node_from_value(node, field_value)

    for field_name in sorted(root_fields):
        _collect_node_warnings(field_name, root_fields[field_name], warnings)

    paths = _flatten_field_rows(root_fields, container_count=valid_record_count)

    return DatasetInspection(
        dataset_name=dataset_name,
        dataset_source=dataset_source,
        sde_metadata=sde_metadata,
        top_level_key_type_counts=_sorted_type_counts(dict(top_level_key_type_counts)),
        total_records=total_records,
        valid_record_count=valid_record_count,
        skipped_record_count=skipped_record_count,
        path_count=len(paths),
        paths=paths,
        warnings=warnings,
    )


def build_schema_report(
    datasets: Iterable[DatasetInput],
    sde_metadata: SdeMetadata,
    *,
    dataset_source: str,
) -> SchemaReport:
    """Build a schema report from multiple normalized datasets."""
    inspected_datasets: list[DatasetInspection] = []

    for inspection_args in datasets:
        inspected_datasets.append(
            inspect_dataset_data(
                dataset_name=inspection_args.dataset_name,
                dataset_data=inspection_args.dataset_data,
                sde_metadata=inspection_args.sde_metadata,
                dataset_source=dataset_source,
            )
        )

    sorted_datasets = sorted(
        inspected_datasets, key=lambda dataset: dataset.dataset_name
    )
    dataset_map = {dataset.dataset_name: dataset for dataset in sorted_datasets}
    all_paths = {path for dataset in sorted_datasets for path in dataset.paths}
    total_records = sum(dataset.total_records for dataset in sorted_datasets)
    return SchemaReport(
        source_path=dataset_source,
        generated_at_utc=Instant.now().format_iso(),
        sde_metadata=sde_metadata,
        file_count=len(sorted_datasets),
        total_records=total_records,
        total_unique_paths=len(all_paths),
        datasets=dataset_map,
    )
