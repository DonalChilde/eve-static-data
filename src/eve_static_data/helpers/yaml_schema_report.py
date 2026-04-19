"""Generate schema inspection reports for YAML SDE datasets."""

from __future__ import annotations

import logging
from collections import Counter
from dataclasses import dataclass, field
from datetime import UTC, datetime
from glob import glob
from pathlib import Path
from typing import Any, Literal, TypedDict, cast

from yaml import YAMLError, safe_load

logger = logging.getLogger(__name__)

type PathStatsMap = dict[str, "YamlPathInspection"]
type DatasetMap = dict[str, "YamlDatasetInspection"]
type WarningList = list[str]
YamlTypeName = Literal["dict", "list", "str", "int", "float", "bool", "null"]


def _string_counter() -> Counter[str]:
    """Return a typed string counter for dataclass defaults."""
    return Counter()


def _field_node_map() -> dict[str, _FieldNode]:
    """Return a typed field-node mapping for dataclass defaults."""
    return {}


class YamlPathInspection(TypedDict):
    """Flattened inspection data for one dotted field path."""

    path: str
    presence_count: int
    container_count: int
    required: bool
    value_type_counts: dict[str, int]


class YamlDatasetInspection(TypedDict):
    """Inspection output for one YAML dataset file."""

    file_name: str
    file_path: str
    top_level_key_type_counts: dict[str, int]
    total_records: int
    valid_record_count: int
    skipped_record_count: int
    path_count: int
    paths: PathStatsMap
    warnings: WarningList


class YamlSchemaReport(TypedDict):
    """Top-level schema report for one or more YAML dataset files."""

    source_path: str
    generated_at_utc: str
    file_count: int
    total_records: int
    total_unique_paths: int
    datasets: DatasetMap


@dataclass
class _ListStats:
    """Mutable aggregation state for list-valued paths."""

    item_count: int = 0
    item_type_counts: Counter[str] = field(default_factory=_string_counter)
    empty_list_count: int = 0
    item_node: _FieldNode = field(default_factory=lambda: _FieldNode())


@dataclass
class _FieldNode:
    """Mutable aggregation node for one observed path."""

    presence_count: int = 0
    value_type_counts: Counter[str] = field(default_factory=_string_counter)
    children: dict[str, _FieldNode] = field(default_factory=_field_node_map)
    list_stats: _ListStats | None = None


def _yaml_type_name(value: Any) -> YamlTypeName:
    """Return a normalized YAML value type name.

    Args:
        value: Parsed YAML value.

    Returns:
        Stable type label used in reports.
    """
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
    """Return mapping items with a concrete type for iteration."""
    return list(cast(dict[object, object], value).items())


def _sequence_items(value: Any) -> list[object]:
    """Return sequence items with a concrete type for iteration."""
    return list(cast(list[object], value))


def _update_node_from_value(node: _FieldNode, value: Any) -> None:
    """Recursively aggregate one observed value into a field node.

    Args:
        node: Aggregation node to update.
        value: Observed value for the path represented by ``node``.
    """
    type_name = _yaml_type_name(value)
    node.value_type_counts[type_name] += 1

    if isinstance(value, dict):
        for child_name, child_value in _mapping_items(value):
            child_node = node.children.setdefault(str(child_name), _FieldNode())
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
        item_type = _yaml_type_name(item)
        list_stats.item_count += 1
        list_stats.item_type_counts[item_type] += 1
        if isinstance(item, dict):
            list_stats.item_node.presence_count += 1
            _update_node_from_value(list_stats.item_node, item)


def _sorted_type_counts(type_counts: dict[str, int]) -> dict[str, int]:
    """Return type counts in a stable display order.

    Args:
        type_counts: Raw type counter mapping.

    Returns:
        Ordered dictionary preserving deterministic output.
    """
    keys = sorted(type_counts)
    return {key: type_counts[key] for key in keys}


def _flatten_field_rows(
    fields: dict[str, _FieldNode],
    container_count: int,
    prefix: str = "",
    ancestor_required: bool = True,
) -> PathStatsMap:
    """Flatten recursive field nodes into dotted-path rows.

    Args:
        fields: Field nodes for the current object level.
        container_count: Number of parent containers at this level.
        prefix: Current dotted-path prefix.
        ancestor_required: Whether every ancestor path is required.

    Returns:
        Flat mapping of dotted paths to report rows.
    """
    rows: PathStatsMap = {}

    for field_name in sorted(fields):
        field_data = fields[field_name]
        path = f"{prefix}.{field_name}" if prefix else field_name
        local_required = (
            container_count > 0 and field_data.presence_count >= container_count
        )
        required = ancestor_required and local_required
        rows[path] = {
            "path": path,
            "presence_count": field_data.presence_count,
            "container_count": container_count,
            "required": required,
            "value_type_counts": _sorted_type_counts(
                dict(field_data.value_type_counts)
            ),
        }

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


def _append_warning(warnings: WarningList, message: str) -> None:
    """Append a warning if it has not been recorded yet.

    Args:
        warnings: Accumulated warning messages.
        message: Warning text to add.
    """
    if message not in warnings:
        warnings.append(message)


def _collect_node_warnings(
    path: str,
    node: _FieldNode,
    warnings: WarningList,
) -> None:
    """Collect warnings from a field node and its descendants.

    Args:
        path: Dotted path represented by ``node``.
        node: Field node to inspect.
        warnings: Mutable warning list to update.
    """
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


def _inspect_yaml_dataset(file_path: Path) -> YamlDatasetInspection:
    """Inspect one YAML dataset file.

    Args:
        file_path: YAML dataset file to inspect.

    Returns:
        Flattened inspection report for a single dataset file.
    """
    warnings: WarningList = []
    root_fields: dict[str, _FieldNode] = {}
    top_level_key_type_counts: Counter[str] = _string_counter()

    try:
        with file_path.open("r", encoding="utf-8") as handle:
            data = safe_load(handle)
    except YAMLError as exc:
        logger.warning("Failed to parse YAML file %s: %s", file_path, exc)
        return {
            "file_name": file_path.name,
            "file_path": str(file_path),
            "top_level_key_type_counts": {},
            "total_records": 0,
            "valid_record_count": 0,
            "skipped_record_count": 0,
            "path_count": 0,
            "paths": {},
            "warnings": [f"Failed to parse YAML: {exc}"],
        }

    if not isinstance(data, dict):
        type_name = _yaml_type_name(data)
        return {
            "file_name": file_path.name,
            "file_path": str(file_path),
            "top_level_key_type_counts": {},
            "total_records": 0,
            "valid_record_count": 0,
            "skipped_record_count": 0,
            "path_count": 0,
            "paths": {},
            "warnings": [
                f"Top-level YAML value must be a mapping of records, found {type_name}",
            ],
        }

    record_mapping = cast(dict[object, object], data)
    total_records = len(record_mapping)
    valid_record_count = 0
    skipped_record_count = 0

    for record_key, record_value in record_mapping.items():
        top_level_key_type_counts[_yaml_type_name(record_key)] += 1
        if not isinstance(record_value, dict):
            skipped_record_count += 1
            _append_warning(
                warnings,
                (
                    f"Top-level key {record_key!r} has non-dict value "
                    f"{_yaml_type_name(record_value)}; skipped"
                ),
            )
            continue

        valid_record_count += 1
        for field_name, field_value in _mapping_items(record_value):
            node = root_fields.setdefault(str(field_name), _FieldNode())
            node.presence_count += 1
            _update_node_from_value(node, field_value)

    for field_name in sorted(root_fields):
        _collect_node_warnings(field_name, root_fields[field_name], warnings)

    paths = _flatten_field_rows(root_fields, container_count=valid_record_count)

    return {
        "file_name": file_path.name,
        "file_path": str(file_path),
        "top_level_key_type_counts": _sorted_type_counts(
            dict(top_level_key_type_counts)
        ),
        "total_records": total_records,
        "valid_record_count": valid_record_count,
        "skipped_record_count": skipped_record_count,
        "path_count": len(paths),
        "paths": paths,
        "warnings": warnings,
    }


def _build_schema_report(
    source_path: str, datasets: list[YamlDatasetInspection]
) -> YamlSchemaReport:
    """Build the top-level schema report object.

    Args:
        source_path: Source file, directory, or glob used for scanning.
        datasets: Dataset inspection results to aggregate.

    Returns:
        Aggregated schema report.
    """
    sorted_datasets = sorted(datasets, key=lambda dataset: dataset["file_name"])
    dataset_map: DatasetMap = {
        dataset["file_name"]: dataset for dataset in sorted_datasets
    }
    all_paths = {path for dataset in sorted_datasets for path in dataset["paths"]}
    total_records = sum(dataset["total_records"] for dataset in sorted_datasets)
    return {
        "source_path": source_path,
        "generated_at_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "file_count": len(sorted_datasets),
        "total_records": total_records,
        "total_unique_paths": len(all_paths),
        "datasets": dataset_map,
    }


def scan_yaml_file(path: Path) -> YamlSchemaReport:
    """Scan a single YAML file and return a schema report.

    Args:
        path: YAML file to scan.

    Returns:
        Schema report containing one dataset section.
    """
    dataset = _inspect_yaml_dataset(path)
    return _build_schema_report(str(path), [dataset])


def scan_yaml_directory(pattern: str | Path) -> YamlSchemaReport:
    """Scan multiple YAML files and return an aggregated schema report.

    Args:
        pattern: Directory, file path, or glob pattern selecting YAML files.

    Returns:
        Schema report with one section per matching dataset file.
    """
    if isinstance(pattern, Path):
        candidate = pattern
        if candidate.is_dir():
            files = sorted(candidate.glob("*.yaml"))
            source_path = str(candidate)
        elif candidate.is_file():
            files = [candidate]
            source_path = str(candidate)
        else:
            files = [Path(match) for match in sorted(glob(str(candidate)))]
            source_path = str(candidate)
    else:
        candidate = Path(pattern)
        if candidate.is_dir():
            files = sorted(candidate.glob("*.yaml"))
        elif candidate.is_file():
            files = [candidate]
        else:
            files = [Path(match) for match in sorted(glob(pattern))]
        source_path = str(pattern)

    datasets = [_inspect_yaml_dataset(file_path) for file_path in files]
    return _build_schema_report(source_path, datasets)


def generate_markdown_report(report: YamlSchemaReport) -> str:
    """Render a human-readable markdown schema report.

    Args:
        report: Schema report from ``scan_yaml_file`` or ``scan_yaml_directory``.

    Returns:
        Markdown text with a summary and per-dataset sections.
    """
    lines: list[str] = [
        "# YAML Schema Report",
        "",
        "## Summary",
        f"- source_path: {report['source_path']}",
        f"- generated_at_utc: {report['generated_at_utc']}",
        f"- files_scanned: {report['file_count']}",
        f"- total_records: {report['total_records']}",
        f"- total_unique_paths: {report['total_unique_paths']}",
        "",
    ]

    for file_name in sorted(report["datasets"]):
        dataset = report["datasets"][file_name]
        key_type_summary = ", ".join(
            f"{type_name}:{count}"
            for type_name, count in dataset["top_level_key_type_counts"].items()
        )
        lines.extend(
            [
                f"## {dataset['file_name']}",
                f"- Records: {dataset['total_records']}",
                f"- Top-level key types: {key_type_summary or 'unknown'}",
                f"- Valid dict records: {dataset['valid_record_count']}",
                f"- Skipped top-level items: {dataset['skipped_record_count']}",
                f"- Paths discovered: {dataset['path_count']}",
                "",
            ]
        )

        if dataset["paths"]:
            lines.extend(
                [
                    "| Path | Presence | Required | Types |",
                    "|------|----------|----------|-------|",
                ]
            )
            for path in sorted(dataset["paths"]):
                row = dataset["paths"][path]
                type_summary = ", ".join(
                    f"{type_name}:{count}"
                    for type_name, count in row["value_type_counts"].items()
                )
                presence = f"{row['presence_count']}/{row['container_count']}"
                required = "yes" if row["required"] else "no"
                lines.append(f"| {path} | {presence} | {required} | {type_summary} |")
        else:
            lines.append("No schema paths discovered.")

        lines.append("")
        lines.append("### Warnings")
        lines.append("")
        if dataset["warnings"]:
            for warning in dataset["warnings"]:
                lines.append(f"- {warning}")
        else:
            lines.append("- None")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate YAML schema report.")
    parser.add_argument(
        "input_path",
        type=str,
        help=(
            "Path to YAML file, directory, or glob pattern to scan. "
            "Examples: 'data.yaml', 'datasets/', 'yaml_files/*.yaml'"
        ),
    )
    parser.add_argument(
        "output_file",
        type=str,
        help="Path to write the markdown report. Use '-' for stdout.",
    )
    args = parser.parse_args()

    report = scan_yaml_directory(args.input_path)
    markdown = generate_markdown_report(report)
    if args.output_file == "-":
        print(markdown)
    else:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(markdown)
