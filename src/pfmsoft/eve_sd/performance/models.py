"""Dataclasses for SDE performance reports."""

from dataclasses import dataclass, field

from pydantic import RootModel

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata


@dataclass(slots=True, kw_only=True)
class FileDatasetTiming:
    """Timing details for a single dataset loaded from files."""

    dataset_name: str
    record_count: int | None = None
    total_seconds: float | None = None
    key_type: str | None = None
    file_size_bytes: int | None = None
    notes: str | None = None


@dataclass(slots=True, kw_only=True)
class DbDatasetTiming:
    """Timing details for a single dataset accessed from SQLite."""

    dataset_name: str
    record_count: int | None = None
    total_seconds: float | None = None
    dataset_load_seconds: float | None = None
    all_dataset_keys_seconds: float | None = None
    random_record_access_seconds: float | None = None
    random_record_access_sample_size: int | None = None
    key_type: str | None = None
    notes: str | None = None


@dataclass(slots=True, kw_only=True)
class FileSourceReport:
    """Performance report for file-backed datasets."""

    source_type: str = "files"
    source_path: str
    generated_at: str
    startup_seconds: float | None = None
    total_seconds: float | None = None
    dataset_count: int | None = None
    deserialization_method: str | None = None
    sde_metadata: SdeMetadata | None = None
    file_size_bytes: int | None = None
    datasets: list[FileDatasetTiming] = field(default_factory=list[FileDatasetTiming])

    def serialize(self, indent: int | None = None) -> str:
        """Serialize the report to a JSON string."""
        return FileSourceReportRoot(self).model_dump_json(indent=indent)

    @classmethod
    def deserialize(cls, json_string: str) -> FileSourceReport:
        """Deserialize a JSON string to a FileSourceReport instance."""
        return FileSourceReportRoot.model_validate_json(json_string).root


FileSourceReportRoot = RootModel[FileSourceReport]


@dataclass(slots=True, kw_only=True)
class DbSourceReport:
    """Performance report for SQLite-backed datasets."""

    source_type: str = "db"
    source_path: str
    generated_at: str
    startup_seconds: float | None = None
    total_seconds: float | None = None
    dataset_count: int | None = None
    dataset_names: list[str] = field(default_factory=list[str])
    serialization_format: str | None = None
    sde_metadata: SdeMetadata | None = None
    datasets: list[DbDatasetTiming] = field(default_factory=list[DbDatasetTiming])

    def serialize(self, indent: int | None = None) -> str:
        """Serialize the report to a JSON string."""
        return DbSourceReportRoot(self).model_dump_json(indent=indent)

    @classmethod
    def deserialize(cls, json_string: str) -> DbSourceReport:
        """Deserialize a JSON string to a DbSourceReport instance."""
        return DbSourceReportRoot.model_validate_json(json_string).root


DbSourceReportRoot = RootModel[DbSourceReport]

SourceReport = FileSourceReport | DbSourceReport
