"""Dataclasses for SDE performance reports."""

from dataclasses import dataclass, field

from pydantic import RootModel

from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata


@dataclass(slots=True, kw_only=True)
class FileDatasetTiming:
    """Timing details for a single dataset loaded from files."""

    dataset_name: str
    """Name of the dataset as it appears in the SDE export."""

    record_count: int | None = None
    """Total number of records in the dataset when known."""

    total_seconds: float | None = None
    """Elapsed wall-clock time spent loading and processing the dataset."""

    key_type: str | None = None
    """The type of key used for indexing or lookup within the dataset."""

    file_size_bytes: int | None = None
    """Byte size of the source file for the dataset, if available."""

    notes: str | None = None
    """Free-form notes about anomalies, assumptions, or measurement context."""


@dataclass(slots=True, kw_only=True)
class DbDatasetTiming:
    """Timing details for a single dataset accessed from SQLite."""

    dataset_name: str
    """Name of the dataset as it appears in the SQLite database."""

    record_count: int | None = None
    """Total number of rows in the dataset when known."""

    total_seconds: float | None = None
    """Overall time spent querying or processing the dataset."""

    dataset_load_seconds: float | None = None
    """Time required to load or initialize the dataset from SQLite."""

    all_dataset_keys_seconds: float | None = None
    """Time spent retrieving all keys for the dataset for comparison work."""

    random_record_access_seconds: float | None = None
    """Average access time for random record lookups sampled across the dataset."""

    random_record_access_sample_size: int | None = None
    """Number of random record access probes used to derive the timing."""

    key_type: str | None = None
    """The type of key used to identify rows in the dataset."""

    notes: str | None = None
    """Additional context about SQLite access patterns or observed issues."""


@dataclass(slots=True, kw_only=True)
class FileSourceReport:
    """Performance report for file-backed datasets."""

    source_type: str = "files"
    """A stable label describing the storage backend: file-based data."""

    source_path: str
    """Filesystem path used to load these file-backed datasets."""

    generated_at: str
    """Timestamp when the performance report was generated."""

    startup_seconds: float | None = None
    """Time required to start the source reader before dataset loading begins."""

    total_seconds: float | None = None
    """Total elapsed time captured for the entire file-backed report."""

    dataset_count: int | None = None
    """Number of datasets included in the report."""

    deserialization_method: str | None = None
    """Method used to parse the source files into Python objects."""

    sde_metadata: SdeMetadata | None = None
    """Metadata describing the SDE version and source package associated with the report."""

    file_size_bytes: int | None = None
    """Combined size of the underlying source files in bytes, if tracked."""

    datasets: list[FileDatasetTiming] = field(default_factory=list[FileDatasetTiming])
    """Per-dataset timing samples included in the file-backed performance report."""

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
    """A stable label describing the storage backend: SQLite-backed data."""

    source_path: str
    """Filesystem or database path used to access these SQLite datasets."""

    generated_at: str
    """Timestamp when the database performance report was generated."""

    startup_seconds: float | None = None
    """Time needed to initialize the SQLite source before dataset work begins."""

    total_seconds: float | None = None
    """Overall elapsed time captured for the SQLite-backed report."""

    dataset_count: int | None = None
    """Number of datasets represented in the database report."""

    dataset_names: list[str] = field(default_factory=list[str])
    """List of dataset names included in the report for quick inspection."""

    serialization_format: str | None = None
    """Format used to serialize or export the database data."""

    sde_metadata: SdeMetadata | None = None
    """SDE metadata for the database snapshot that was measured."""

    datasets: list[DbDatasetTiming] = field(default_factory=list[DbDatasetTiming])
    """Per-dataset timings collected from SQLite access patterns."""

    def serialize(self, indent: int | None = None) -> str:
        """Serialize the report to a JSON string."""
        return DbSourceReportRoot(self).model_dump_json(indent=indent)

    @classmethod
    def deserialize(cls, json_string: str) -> DbSourceReport:
        """Deserialize a JSON string to a DbSourceReport instance."""
        return DbSourceReportRoot.model_validate_json(json_string).root


DbSourceReportRoot = RootModel[DbSourceReport]

SourceReport = FileSourceReport | DbSourceReport
