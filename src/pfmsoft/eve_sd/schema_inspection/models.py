"""Dataclass models for schema inspection reports."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Literal

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata

SdeTypeName = Literal["dict", "list", "str", "int", "float", "bool", "null"]
SdeFormat = Literal["yaml-model", "jsonl-model"]

INTEGER_KEY = "INTEGER_KEY"
STRING_KEY = "STRING_KEY"


@dataclass(slots=True, kw_only=True)
class PathInspection:
    """Flattened inspection data for one dotted field path."""

    path: str
    presence_count: int
    container_count: int
    required: bool
    value_type_counts: dict[str, int]
    list_item_type_counts: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable mapping for this path."""
        return {
            "path": self.path,
            "presence_count": self.presence_count,
            "container_count": self.container_count,
            "required": self.required,
            "value_type_counts": dict(self.value_type_counts),
            "list_item_type_counts": dict(self.list_item_type_counts),
        }


@dataclass(slots=True, kw_only=True)
class DatasetInspection:
    """Inspection output for one normalized dataset."""

    dataset_name: str
    dataset_source: str
    sde_metadata: SdeMetadata
    top_level_key_type_counts: dict[str, int]
    total_records: int
    valid_record_count: int
    skipped_record_count: int
    path_count: int
    paths: dict[str, PathInspection]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable mapping for this dataset."""
        return {
            "dataset_name": self.dataset_name,
            "dataset_source": self.dataset_source,
            "sde_metadata": self.sde_metadata,
            "top_level_key_type_counts": dict(self.top_level_key_type_counts),
            "total_records": self.total_records,
            "valid_record_count": self.valid_record_count,
            "skipped_record_count": self.skipped_record_count,
            "path_count": self.path_count,
            "paths": {
                path: inspection.to_dict() for path, inspection in self.paths.items()
            },
            "warnings": list(self.warnings),
        }


@dataclass(slots=True, kw_only=True)
class SchemaReport:
    """Top-level schema report for one or more datasets."""

    source_path: str
    generated_at_utc: str
    sde_metadata: SdeMetadata
    file_count: int
    total_records: int
    total_unique_paths: int
    datasets: dict[str, DatasetInspection]

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable mapping for this report."""
        return {
            "source_path": self.source_path,
            "generated_at_utc": self.generated_at_utc,
            "sde_metadata": self.sde_metadata,
            "file_count": self.file_count,
            "total_records": self.total_records,
            "total_unique_paths": self.total_unique_paths,
            "datasets": {
                name: dataset.to_dict() for name, dataset in self.datasets.items()
            },
        }


@dataclass(slots=True, kw_only=True)
class ListStats:
    item_count: int = 0
    item_type_counts: Counter[str] = field(default_factory=Counter[str])
    empty_list_count: int = 0
    item_node: FieldNode = field(default_factory=lambda: FieldNode())


@dataclass(slots=True, kw_only=True)
class FieldNode:
    presence_count: int = 0
    value_type_counts: Counter[str] = field(default_factory=Counter[str])
    children: dict[str, FieldNode] = field(default_factory=dict[str, "FieldNode"])
    list_stats: ListStats | None = None
