"""Inspect JSONL files and generate TypedDict schema documentation.

This module provides a standalone implementation for:
- Inspecting JSONL files and tracking type/count statistics.
- Generating nested TypedDict definitions from inspection data.
- Building markdown documentation for a directory of JSONL files.
- Comparing inspection snapshots and rendering markdown change reports.

The schema generator targets dictionary-shaped top-level records. Non-dictionary
top-level values are counted and reported, but they are not converted into
TypedDict fields.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, TypedDict

JsonTypeName = Literal["dict", "list", "str", "int", "float", "bool", "null"]


class JsonlParseError(TypedDict):
    """Details about a JSON decode failure for one line."""

    line_number: int
    message: str
    snippet: str


class ListInspection(TypedDict):
    """Inspection details for list-valued fields."""

    item_count: int
    item_type_counts: dict[str, int]
    empty_list_count: int
    item: FieldInspection


class FieldInspection(TypedDict):
    """Recursive per-field inspection information."""

    presence_count: int
    value_type_counts: dict[str, int]
    children: dict[str, FieldInspection]
    list_inspection: ListInspection | None


class JsonlFileInspection(TypedDict):
    """Full inspection output for one JSONL file."""

    file_name: str
    file_path: str
    total_lines: int
    valid_json_lines: int
    invalid_json_lines: int
    top_level_type_counts: dict[str, int]
    top_level_dict_count: int
    parse_errors: list[JsonlParseError]
    fields: dict[str, FieldInspection]


class DirectoryInspection(TypedDict):
    """Inspection output for a directory of JSONL files."""

    directory_path: str
    generated_at_utc: str
    file_count: int
    files: dict[str, JsonlFileInspection]


class TypedDictClassDefinition(TypedDict):
    """A generated TypedDict class block."""

    class_name: str
    source: str
    code: str


class FileSchema(TypedDict):
    """Generated schema for one inspected file."""

    root_class_name: str
    class_definitions: list[TypedDictClassDefinition]
    code: str


class FieldSignature(TypedDict):
    """Flattened field signature for compare workflows."""

    path: str
    type_expr: str
    required: bool


class FieldChange(TypedDict):
    """Represents a field-level change between snapshots."""

    path: str
    old_type_expr: str
    new_type_expr: str
    old_required: bool
    new_required: bool
    change_kind: Literal["type", "required", "list"]


class TopLevelCountDelta(TypedDict):
    """Top-level type count changes."""

    type_name: str
    old_count: int
    new_count: int
    delta: int


class FileComparison(TypedDict):
    """Comparison output for one file name."""

    file_name: str
    status: Literal["added", "removed", "modified", "unchanged"]
    old_total_lines: int
    new_total_lines: int
    old_top_level_dict_count: int
    new_top_level_dict_count: int
    top_level_type_deltas: list[TopLevelCountDelta]
    added_fields: list[FieldSignature]
    removed_fields: list[FieldSignature]
    changed_fields: list[FieldChange]


class DirectoryComparison(TypedDict):
    """Comparison output for two directory inspections."""

    old_directory: str
    new_directory: str
    generated_at_utc: str
    files: list[FileComparison]


@dataclass
class _ListStats:
    """Internal mutable stats for list values."""

    item_count: int = 0
    item_type_counts: Counter[str] = field(default_factory=Counter)
    empty_list_count: int = 0
    item_node: _FieldNode = field(default_factory=lambda: _FieldNode())


@dataclass
class _FieldNode:
    """Internal mutable node used while aggregating field statistics."""

    presence_count: int = 0
    value_type_counts: Counter[str] = field(default_factory=Counter)
    children: dict[str, _FieldNode] = field(default_factory=dict)
    list_stats: _ListStats | None = None


def _json_type_name(value: Any) -> JsonTypeName:
    """Return a normalized JSON type name for a Python value.

    Args:
        value: Value decoded from JSON.

    Returns:
        Normalized JSON type name.
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


def _update_node_from_value(node: _FieldNode, value: Any) -> None:
    """Recursively update a node with one observed value.

    Args:
        node: Mutable node to update.
        value: Observed field value.
    """
    type_name = _json_type_name(value)
    node.value_type_counts[type_name] += 1

    if isinstance(value, dict):
        for child_name, child_value in value.items():
            child_node = node.children.setdefault(child_name, _FieldNode())
            child_node.presence_count += 1
            _update_node_from_value(child_node, child_value)
        return

    if isinstance(value, list):
        list_stats = node.list_stats
        if list_stats is None:
            list_stats = _ListStats()
            node.list_stats = list_stats

        if not value:
            list_stats.empty_list_count += 1
            return

        for item in value:
            item_type = _json_type_name(item)
            list_stats.item_count += 1
            list_stats.item_type_counts[item_type] += 1
            list_stats.item_node.presence_count += 1
            _update_node_from_value(list_stats.item_node, item)


def _node_to_typed_dict(node: _FieldNode) -> FieldInspection:
    """Convert an internal node into a serialized TypedDict shape.

    Args:
        node: Internal mutable field node.

    Returns:
        Immutable dictionary matching FieldInspection.
    """
    children = {
        name: _node_to_typed_dict(child) for name, child in node.children.items()
    }
    list_inspection: ListInspection | None = None
    if node.list_stats is not None:
        list_inspection = {
            "item_count": node.list_stats.item_count,
            "item_type_counts": dict(node.list_stats.item_type_counts),
            "empty_list_count": node.list_stats.empty_list_count,
            "item": _node_to_typed_dict(node.list_stats.item_node),
        }
    return {
        "presence_count": node.presence_count,
        "value_type_counts": dict(node.value_type_counts),
        "children": children,
        "list_inspection": list_inspection,
    }


def inspect_jsonl_file(file_path: str | Path) -> JsonlFileInspection:
    """Inspect one JSONL file and return counts and recursive field statistics.

    Args:
        file_path: Path to a JSONL file.

    Returns:
        Inspection data with top-level counts, parse errors, and recursive field stats.
    """
    path = Path(file_path)
    top_level_type_counts: Counter[str] = Counter()
    parse_errors: list[JsonlParseError] = []
    root_fields: dict[str, _FieldNode] = {}

    total_lines = 0
    valid_json_lines = 0
    top_level_dict_count = 0

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            total_lines += 1
            text = raw_line.rstrip("\n")

            if not text.strip():
                parse_errors.append(
                    {
                        "line_number": line_number,
                        "message": "Empty line is not valid JSON",
                        "snippet": "",
                    }
                )
                continue

            try:
                data = json.loads(text)
            except json.JSONDecodeError as exc:
                parse_errors.append(
                    {
                        "line_number": line_number,
                        "message": str(exc),
                        "snippet": text[:140],
                    }
                )
                continue

            valid_json_lines += 1
            type_name = _json_type_name(data)
            top_level_type_counts[type_name] += 1

            if not isinstance(data, dict):
                continue

            top_level_dict_count += 1
            for field_name, field_value in data.items():
                node = root_fields.setdefault(field_name, _FieldNode())
                node.presence_count += 1
                _update_node_from_value(node, field_value)

    return {
        "file_name": path.name,
        "file_path": str(path),
        "total_lines": total_lines,
        "valid_json_lines": valid_json_lines,
        "invalid_json_lines": len(parse_errors),
        "top_level_type_counts": dict(top_level_type_counts),
        "top_level_dict_count": top_level_dict_count,
        "parse_errors": parse_errors,
        "fields": {
            name: _node_to_typed_dict(node) for name, node in root_fields.items()
        },
    }


def inspect_jsonl_directory(directory_path: str | Path) -> DirectoryInspection:
    """Inspect every JSONL file in a directory.

    Args:
        directory_path: Directory containing JSONL files.

    Returns:
        Aggregated inspection object keyed by file name.
    """
    path = Path(directory_path)
    files = sorted(path.glob("*.jsonl"))
    inspected = {file.name: inspect_jsonl_file(file) for file in files}
    return {
        "directory_path": str(path),
        "generated_at_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "file_count": len(inspected),
        "files": inspected,
    }


def _pascal_case(value: str) -> str:
    """Convert a string into a safe PascalCase Python identifier.

    Args:
        value: Arbitrary string.

    Returns:
        Sanitized PascalCase identifier.
    """
    pieces = [
        part
        for part in "".join(ch if ch.isalnum() else " " for ch in value).split()
        if part
    ]
    if not pieces:
        return "GeneratedSchema"
    candidate = "".join(piece[:1].upper() + piece[1:] for piece in pieces)
    if candidate[:1].isdigit():
        return f"N{candidate}"
    return candidate


def _scalar_python_type(type_name: str) -> str:
    """Map normalized JSON type names to Python annotation names.

    Args:
        type_name: Normalized type label.

    Returns:
        Type expression fragment.
    """
    mapping = {
        "str": "str",
        "int": "int",
        "float": "float",
        "bool": "bool",
        "null": "None",
    }
    return mapping.get(type_name, "Any")


def _union_type(type_parts: list[str]) -> str:
    """Return a deterministic union expression from type fragments.

    Args:
        type_parts: Candidate type strings.

    Returns:
        Single type string or union type expression.
    """
    unique: list[str] = []
    for part in type_parts:
        if part not in unique:
            unique.append(part)
    if not unique:
        return "Any"
    if len(unique) == 1:
        return unique[0]
    return " | ".join(sorted(unique))


@dataclass
class _SchemaBuilder:
    """Build nested TypedDict classes from one file inspection."""

    root_name: str
    class_defs: list[TypedDictClassDefinition] = field(default_factory=list)
    _used_class_names: set[str] = field(default_factory=set)

    def _unique_class_name(self, candidate: str) -> str:
        """Return a unique class name for this schema run.

        Args:
            candidate: Preferred class name.

        Returns:
            Unique class name.
        """
        if candidate not in self._used_class_names:
            self._used_class_names.add(candidate)
            return candidate

        index = 2
        while True:
            name = f"{candidate}{index}"
            if name not in self._used_class_names:
                self._used_class_names.add(name)
                return name
            index += 1

    def _build_type_for_field(
        self,
        parent_class: str,
        field_name: str,
        field_data: FieldInspection,
    ) -> str:
        """Build a Python type expression for one field.

        Args:
            parent_class: Parent class name used for nested naming.
            field_name: Current field name.
            field_data: Inspection data for this field.

        Returns:
            Python type expression.
        """
        types: list[str] = []
        value_type_counts = field_data["value_type_counts"]

        for value_type in sorted(value_type_counts):
            if value_type == "dict":
                child_name = self._unique_class_name(
                    f"{parent_class}_{_pascal_case(field_name)}"
                )
                self._build_class(
                    class_name=child_name,
                    source=f"dict field {field_name}",
                    fields=field_data["children"],
                    container_count=value_type_counts["dict"],
                )
                types.append(child_name)
                continue

            if value_type == "list":
                list_inspection = field_data["list_inspection"]
                list_type = self._build_list_type(
                    parent_class=parent_class,
                    field_name=field_name,
                    list_inspection=list_inspection,
                )
                types.append(list_type)
                continue

            types.append(_scalar_python_type(value_type))

        return _union_type(types)

    def _build_list_type(
        self,
        parent_class: str,
        field_name: str,
        list_inspection: ListInspection | None,
    ) -> str:
        """Build a list type expression from list inspection details.

        Args:
            parent_class: Parent class name used for nested naming.
            field_name: Current field name.
            list_inspection: Collected list stats for this field.

        Returns:
            A list type expression.
        """
        if list_inspection is None:
            return "list[Any]"

        item_types: list[str] = []
        item_type_counts = list_inspection["item_type_counts"]
        item_node = list_inspection["item"]

        for item_type in sorted(item_type_counts):
            if item_type == "dict":
                class_name = self._unique_class_name(
                    f"{parent_class}_{_pascal_case(field_name)}Item"
                )
                self._build_class(
                    class_name=class_name,
                    source=f"list item field {field_name}",
                    fields=item_node["children"],
                    container_count=item_type_counts["dict"],
                )
                item_types.append(class_name)
                continue

            if item_type == "list":
                nested_list = self._build_list_type(
                    parent_class=f"{parent_class}_{_pascal_case(field_name)}Item",
                    field_name="item",
                    list_inspection=item_node["list_inspection"],
                )
                item_types.append(nested_list)
                continue

            item_types.append(_scalar_python_type(item_type))

        item_expr = _union_type(item_types)
        return f"list[{item_expr}]"

    def _build_class(
        self,
        class_name: str,
        source: str,
        fields: dict[str, FieldInspection],
        container_count: int,
    ) -> None:
        """Create and store one TypedDict class definition.

        Args:
            class_name: Class name to emit.
            source: Text describing where this class came from.
            fields: Field inspection mapping for this class.
            container_count: Count used to infer required vs optional fields.
        """
        lines: list[str] = [f"class {class_name}(TypedDict):"]
        if not fields:
            lines.append("    pass")
        else:
            for field_name in sorted(fields):
                field_data = fields[field_name]
                type_expr = self._build_type_for_field(
                    class_name, field_name, field_data
                )
                required = field_data["presence_count"] >= container_count
                rendered_type = type_expr if required else f"NotRequired[{type_expr}]"
                lines.append(f"    {field_name}: {rendered_type}")

        self.class_defs.append(
            {
                "class_name": class_name,
                "source": source,
                "code": "\n".join(lines),
            }
        )

    def build(self, inspection: JsonlFileInspection) -> FileSchema:
        """Build a complete file schema for one inspection object.

        Args:
            inspection: File inspection data.

        Returns:
            Generated schema definition bundle.
        """
        self._used_class_names.add(self.root_name)
        self._build_class(
            class_name=self.root_name,
            source=inspection["file_name"],
            fields=inspection["fields"],
            container_count=inspection["top_level_dict_count"],
        )

        ordered = [
            class_def
            for class_def in self.class_defs
            if class_def["class_name"] != self.root_name
        ]
        ordered.append(
            next(c for c in self.class_defs if c["class_name"] == self.root_name)
        )

        import_line = "from typing import Any, NotRequired, TypedDict"
        code = "\n\n".join([import_line] + [item["code"] for item in ordered])

        return {
            "root_class_name": self.root_name,
            "class_definitions": ordered,
            "code": code,
        }


def generate_file_schema(
    inspection: JsonlFileInspection,
    class_name: str | None = None,
) -> FileSchema:
    """Generate TypedDict schema text for one file inspection.

    Args:
        inspection: File inspection output from inspect_jsonl_file().
        class_name: Optional explicit root class name.

    Returns:
        Generated schema object containing individual classes and full code.
    """
    root_name = class_name or _pascal_case(Path(inspection["file_name"]).stem)
    builder = _SchemaBuilder(root_name=root_name)
    return builder.build(inspection)


def generate_directory_markdown(inspection: DirectoryInspection) -> str:
    """Generate markdown documentation for a directory inspection.

    Args:
        inspection: Output from inspect_jsonl_directory().

    Returns:
        Markdown report with per-file stats and generated TypedDicts.
    """
    lines: list[str] = [
        "# JSONL Type Inspection",
        "",
        f"- Directory: {inspection['directory_path']}",
        f"- Generated (UTC): {inspection['generated_at_utc']}",
        f"- File count: {inspection['file_count']}",
        "",
    ]

    for file_name in sorted(inspection["files"]):
        file_inspection = inspection["files"][file_name]
        schema = generate_file_schema(file_inspection)
        lines.extend(
            [
                f"## {file_name}",
                "",
                f"- Total lines: {file_inspection['total_lines']}",
                f"- Valid JSON lines: {file_inspection['valid_json_lines']}",
                f"- Invalid JSON lines: {file_inspection['invalid_json_lines']}",
                (
                    "- Top-level type counts: "
                    + ", ".join(
                        f"{name}={count}"
                        for name, count in sorted(
                            file_inspection["top_level_type_counts"].items()
                        )
                    )
                ),
                f"- Top-level dict records: {file_inspection['top_level_dict_count']}",
                "",
            ]
        )

        if file_inspection["parse_errors"]:
            lines.append("### Parse Errors")
            lines.append("")
            for error in file_inspection["parse_errors"]:
                lines.append(f"- Line {error['line_number']}: {error['message']}")
            lines.append("")

        lines.extend(
            ["### TypedDict Schema", "", "```python", schema["code"], "```", ""]
        )

    return "\n".join(lines).rstrip() + "\n"


def write_directory_markdown(
    directory_path: str | Path,
    output_path: str | Path,
) -> DirectoryInspection:
    """Inspect a directory and write markdown documentation.

    Args:
        directory_path: Directory with JSONL files.
        output_path: Markdown file output location.

    Returns:
        Directory inspection object used to render the markdown.
    """
    inspection = inspect_jsonl_directory(directory_path)
    markdown = generate_directory_markdown(inspection)
    Path(output_path).write_text(markdown, encoding="utf-8")
    return inspection


def _flatten_field_signatures(
    fields: dict[str, FieldInspection],
    parent_class: str,
    container_count: int,
    prefix: str = "",
) -> dict[str, FieldSignature]:
    """Flatten nested field definitions into path->signature mappings.

    Args:
        fields: Field inspection map for one object level.
        parent_class: Parent class name used for stable nested naming.
        container_count: Count used to infer required fields.
        prefix: Optional dotted path prefix.

    Returns:
        Mapping of dotted paths to field signatures.
    """
    signatures: dict[str, FieldSignature] = {}
    builder = _SchemaBuilder(root_name=parent_class)

    for field_name in sorted(fields):
        field_data = fields[field_name]
        path = f"{prefix}.{field_name}" if prefix else field_name
        type_expr = builder._build_type_for_field(parent_class, field_name, field_data)
        required = field_data["presence_count"] >= container_count
        signatures[path] = {
            "path": path,
            "type_expr": type_expr,
            "required": required,
        }

        if field_data["children"]:
            nested_container_count = field_data["value_type_counts"].get("dict", 0)
            nested = _flatten_field_signatures(
                fields=field_data["children"],
                parent_class=f"{parent_class}_{_pascal_case(field_name)}",
                container_count=nested_container_count,
                prefix=path,
            )
            signatures.update(nested)

        list_inspection = field_data["list_inspection"]
        if list_inspection is not None:
            item_node = list_inspection["item"]
            if item_node["children"]:
                list_dict_count = list_inspection["item_type_counts"].get("dict", 0)
                nested = _flatten_field_signatures(
                    fields=item_node["children"],
                    parent_class=f"{parent_class}_{_pascal_case(field_name)}Item",
                    container_count=list_dict_count,
                    prefix=f"{path}[]",
                )
                signatures.update(nested)

    return signatures


def compare_file_inspections(
    old: JsonlFileInspection,
    new: JsonlFileInspection,
) -> FileComparison:
    """Compare two inspection snapshots for the same file name.

    Args:
        old: Older file inspection.
        new: Newer file inspection.

    Returns:
        Structured per-file comparison output.
    """
    old_counts = old["top_level_type_counts"]
    new_counts = new["top_level_type_counts"]
    all_types = sorted(set(old_counts) | set(new_counts))
    deltas: list[TopLevelCountDelta] = []
    for type_name in all_types:
        old_count = old_counts.get(type_name, 0)
        new_count = new_counts.get(type_name, 0)
        if old_count != new_count:
            deltas.append(
                {
                    "type_name": type_name,
                    "old_count": old_count,
                    "new_count": new_count,
                    "delta": new_count - old_count,
                }
            )

    old_sig = _flatten_field_signatures(
        fields=old["fields"],
        parent_class=_pascal_case(Path(old["file_name"]).stem),
        container_count=old["top_level_dict_count"],
    )
    new_sig = _flatten_field_signatures(
        fields=new["fields"],
        parent_class=_pascal_case(Path(new["file_name"]).stem),
        container_count=new["top_level_dict_count"],
    )

    old_paths = set(old_sig)
    new_paths = set(new_sig)

    added_fields = [new_sig[path] for path in sorted(new_paths - old_paths)]
    removed_fields = [old_sig[path] for path in sorted(old_paths - new_paths)]

    changed_fields: list[FieldChange] = []
    for path in sorted(old_paths & new_paths):
        before = old_sig[path]
        after = new_sig[path]

        if before["type_expr"] != after["type_expr"]:
            changed_fields.append(
                {
                    "path": path,
                    "old_type_expr": before["type_expr"],
                    "new_type_expr": after["type_expr"],
                    "old_required": before["required"],
                    "new_required": after["required"],
                    "change_kind": "list"
                    if "list[" in before["type_expr"] or "list[" in after["type_expr"]
                    else "type",
                }
            )
            continue

        if before["required"] != after["required"]:
            changed_fields.append(
                {
                    "path": path,
                    "old_type_expr": before["type_expr"],
                    "new_type_expr": after["type_expr"],
                    "old_required": before["required"],
                    "new_required": after["required"],
                    "change_kind": "required",
                }
            )

    status: Literal["added", "removed", "modified", "unchanged"] = "unchanged"
    if (
        old["total_lines"] != new["total_lines"]
        or old["top_level_dict_count"] != new["top_level_dict_count"]
        or deltas
        or added_fields
        or removed_fields
        or changed_fields
    ):
        status = "modified"

    return {
        "file_name": new["file_name"],
        "status": status,
        "old_total_lines": old["total_lines"],
        "new_total_lines": new["total_lines"],
        "old_top_level_dict_count": old["top_level_dict_count"],
        "new_top_level_dict_count": new["top_level_dict_count"],
        "top_level_type_deltas": deltas,
        "added_fields": added_fields,
        "removed_fields": removed_fields,
        "changed_fields": changed_fields,
    }


def compare_directory_inspections(
    old: DirectoryInspection,
    new: DirectoryInspection,
) -> DirectoryComparison:
    """Compare two directory inspections.

    Args:
        old: Older directory inspection.
        new: Newer directory inspection.

    Returns:
        Structured comparison object with per-file results.
    """
    old_files = old["files"]
    new_files = new["files"]
    all_names = sorted(set(old_files) | set(new_files))
    results: list[FileComparison] = []

    for name in all_names:
        if name not in old_files:
            added = new_files[name]
            results.append(
                {
                    "file_name": name,
                    "status": "added",
                    "old_total_lines": 0,
                    "new_total_lines": added["total_lines"],
                    "old_top_level_dict_count": 0,
                    "new_top_level_dict_count": added["top_level_dict_count"],
                    "top_level_type_deltas": [
                        {
                            "type_name": key,
                            "old_count": 0,
                            "new_count": value,
                            "delta": value,
                        }
                        for key, value in sorted(added["top_level_type_counts"].items())
                    ],
                    "added_fields": list(
                        _flatten_field_signatures(
                            fields=added["fields"],
                            parent_class=_pascal_case(Path(name).stem),
                            container_count=added["top_level_dict_count"],
                        ).values()
                    ),
                    "removed_fields": [],
                    "changed_fields": [],
                }
            )
            continue

        if name not in new_files:
            removed = old_files[name]
            results.append(
                {
                    "file_name": name,
                    "status": "removed",
                    "old_total_lines": removed["total_lines"],
                    "new_total_lines": 0,
                    "old_top_level_dict_count": removed["top_level_dict_count"],
                    "new_top_level_dict_count": 0,
                    "top_level_type_deltas": [
                        {
                            "type_name": key,
                            "old_count": value,
                            "new_count": 0,
                            "delta": -value,
                        }
                        for key, value in sorted(
                            removed["top_level_type_counts"].items()
                        )
                    ],
                    "added_fields": [],
                    "removed_fields": list(
                        _flatten_field_signatures(
                            fields=removed["fields"],
                            parent_class=_pascal_case(Path(name).stem),
                            container_count=removed["top_level_dict_count"],
                        ).values()
                    ),
                    "changed_fields": [],
                }
            )
            continue

        results.append(compare_file_inspections(old_files[name], new_files[name]))

    return {
        "old_directory": old["directory_path"],
        "new_directory": new["directory_path"],
        "generated_at_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "files": results,
    }


def generate_comparison_markdown(comparison: DirectoryComparison) -> str:
    """Render markdown from directory comparison output.

    Args:
        comparison: Result from compare_directory_inspections().

    Returns:
        Human-readable markdown change report.
    """
    lines: list[str] = [
        "# JSONL Inspection Comparison",
        "",
        f"- Old directory: {comparison['old_directory']}",
        f"- New directory: {comparison['new_directory']}",
        f"- Generated (UTC): {comparison['generated_at_utc']}",
        "",
    ]

    for file_result in comparison["files"]:
        status = file_result["status"]
        lines.extend(
            [
                f"## {file_result['file_name']} ({status})",
                "",
                f"- Total lines: {file_result['old_total_lines']} -> {file_result['new_total_lines']}",
                (
                    "- Top-level dict records: "
                    f"{file_result['old_top_level_dict_count']} -> "
                    f"{file_result['new_top_level_dict_count']}"
                ),
            ]
        )

        if file_result["top_level_type_deltas"]:
            lines.append("- Top-level type deltas:")
            for delta in file_result["top_level_type_deltas"]:
                lines.append(
                    "  "
                    f"- {delta['type_name']}: {delta['old_count']} -> {delta['new_count']} "
                    f"(delta {delta['delta']:+d})"
                )

        if file_result["added_fields"]:
            lines.append("- Added fields:")
            for field in file_result["added_fields"]:
                req = "required" if field["required"] else "optional"
                lines.append(f"  - {field['path']}: {field['type_expr']} ({req})")

        if file_result["removed_fields"]:
            lines.append("- Removed fields:")
            for field in file_result["removed_fields"]:
                req = "required" if field["required"] else "optional"
                lines.append(f"  - {field['path']}: {field['type_expr']} ({req})")

        if file_result["changed_fields"]:
            lines.append("- Changed fields:")
            for change in file_result["changed_fields"]:
                lines.append(
                    "  "
                    f"- {change['path']}: {change['old_type_expr']} -> "
                    f"{change['new_type_expr']} "
                    f"(required {change['old_required']} -> {change['new_required']}, "
                    f"kind={change['change_kind']})"
                )

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _save_json(data: Any, path: str | Path) -> None:
    """Save a Python object to JSON with indentation.

    Args:
        data: Object to serialize.
        path: Output file path.
    """
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")


def _load_directory_inspection(path: str | Path) -> DirectoryInspection:
    """Load a directory inspection object from a JSON file.

    Args:
        path: JSON file containing a directory inspection object.

    Returns:
        Loaded inspection mapping.
    """
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data


def _build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for quick manual workflows.

    Returns:
        Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Inspect JSONL types and generate docs."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_file = sub.add_parser("inspect-file", help="Inspect one JSONL file")
    inspect_file.add_argument("input", type=Path)
    inspect_file.add_argument("--output-json", type=Path, required=False)

    inspect_dir = sub.add_parser(
        "inspect-dir", help="Inspect all JSONL files in a directory"
    )
    inspect_dir.add_argument("input", type=Path)
    inspect_dir.add_argument("--output-json", type=Path, required=False)
    inspect_dir.add_argument("--output-md", type=Path, required=False)

    compare = sub.add_parser(
        "compare", help="Compare two directory inspection JSON files"
    )
    compare.add_argument("old", type=Path)
    compare.add_argument("new", type=Path)
    compare.add_argument("--output-json", type=Path, required=False)
    compare.add_argument("--output-md", type=Path, required=False)

    return parser


def main() -> None:
    """Run the CLI entrypoint for ad-hoc inspection workflows."""
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "inspect-file":
        result = inspect_jsonl_file(args.input)
        if args.output_json:
            _save_json(result, args.output_json)
        else:
            print(json.dumps(result, indent=2))
        return

    if args.command == "inspect-dir":
        result = inspect_jsonl_directory(args.input)
        if args.output_json:
            _save_json(result, args.output_json)
        if args.output_md:
            Path(args.output_md).write_text(
                generate_directory_markdown(result),
                encoding="utf-8",
            )
        if not args.output_json and not args.output_md:
            print(json.dumps(result, indent=2))
        return

    old = _load_directory_inspection(args.old)
    new = _load_directory_inspection(args.new)
    result = compare_directory_inspections(old, new)

    if args.output_json:
        _save_json(result, args.output_json)
    if args.output_md:
        Path(args.output_md).write_text(
            generate_comparison_markdown(result),
            encoding="utf-8",
        )
    if not args.output_json and not args.output_md:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
