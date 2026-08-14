"""Dataclasses for SDE performance reports."""

from dataclasses import dataclass, field

from pydantic import RootModel

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata


@dataclass(slots=True)
class DatasetTiming:
    """Timing details for a single dataset source."""

    dataset_name: str
    record_count: int | None = None
    total_seconds: float | None = None
    key_lookup_seconds: float | None = None
    read_seconds: float | None = None
    source_type: str | None = None
    key_type: str | None = None
    file_size_bytes: int | None = None
    notes: str | None = None


@dataclass(slots=True, kw_only=True)
class SourceReport:
    """Source-specific performance report payload."""

    source_type: str
    source_path: str
    generated_at: str
    startup_seconds: float | None = None
    total_seconds: float | None = None
    dataset_count: int | None = None
    serialization_format: str | None = None
    deserialization_method: str | None = None
    file_size_bytes: int | None = None
    sde_metadata: SdeMetadata | None = None
    datasets: list[DatasetTiming] = field(default_factory=list[DatasetTiming])

    def serialize(self, indent: int | None = None) -> str:
        """Serialize the report to a JSON string."""
        return SourceReportRoot(self).model_dump_json(indent=indent)

    @classmethod
    def deserialize(cls, json_string: str) -> SourceReport:
        """Deserialize a JSON string to a SourceReport instance."""
        return SourceReportRoot.model_validate_json(json_string).root


SourceReportRoot = RootModel[SourceReport]
