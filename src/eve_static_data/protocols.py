"""Protocols for static data classes."""

from collections.abc import Iterable
from pathlib import Path
from typing import Any, Literal, Protocol, TypeVar

from multidict import CIMultiDictProxy

T = TypeVar("T")  # TypedDicts
P = TypeVar("P")  # Pydantic models of records
D = TypeVar("D")  # Pydantic models of datasets


class ESDToolsProtocol(Protocol):
    """Protocol for static data classes."""

    async def download(
        self,
        build_number: int,
        variant: Literal["jsonl", "yaml"],
        output_path: Path,
        overwrite: bool = False,
    ) -> CIMultiDictProxy[str]:
        """Download the static data."""
        ...

    def unpack(self, input_path: Path, output_path: Path) -> None:
        """Unpack the static data.

        Args:
            input_path: The path to the static data jsonl zip file.
            output_path: The path to the directory where the unpacked data should be saved.
        """
        ...

    def validate(self, input_path: Path, output_path: Path) -> bool:
        """Validate the static data.

        Save validation results to the <output_path> directory.

        Results include:
        - <output_path>/validation_report.json: A JSON file containing a summary of the validation results, including the number of records validated, the number of records that passed validation, and the number of records that failed validation.
        - <output_path>/validation_errors.json: A JSON file containing a list of validation errors, including the record that failed validation and the reason for the failure.
        - <output_path>/validation_summary.txt: A human-readable text file summarizing the validation results.
        - <output_path>/sde_data_changelog.jsonl: A JSONL file containing the sde data changelog.
        - <output_path>/sde_schema_changelog.yaml: A YAML file containing the schema changelog.

        """
        ...

    def derive(self, input_path: Path, output_path: Path) -> None:
        """Derive additional static data from the original data."""
        ...

    def esd_import(self, input_path: Path) -> None:
        """Prepare the static data for use.

        runs the full pipeline of unpacking, validating, and deriving the data.
        outputs to the esd app data directory, in a subdirectory named after the build number.

        Args:
            input_path: The path to the static data jsonl zip file.
        """
        ...


class StaticDataReaderProtocol(Protocol):
    def read_pm(self, file_name: str, record_model: type[P]) -> Iterable[P]:
        """Read the static data records as pydantic models."""
        ...

    def read_td(self, file_name: str, record_model: type[T]) -> Iterable[T]:
        """Read the static data records as TypedDicts."""
        ...

    def read_dict(self, file_name: str) -> Iterable[dict[str, Any]]:
        """Read the static data records as dictionaries."""
        ...

    def info(self) -> dict[str, Any]:
        """Return information about the static data."""
        ...


class StaticDataStoreProtocol(Protocol):
    """Protocol for static data store classes."""

    def read(self, dataset_name: str, dataset_model: type[D]) -> Iterable[D]:
        """Read the static data records as pydantic models."""
        ...

    def info(self) -> dict[str, Any]:
        """Return information about the static data store."""
        ...

    def update(self, input_path: Path) -> None:
        """Update the static data store with new data.

        Expects data to be in certain locations.

        - <input_path>/sde for unpacked data
        - <input_path>/derived for derived data
        - <input_path>/validated for validated data
        """
        ...


class StaticDataChangelogProtocol(Protocol):
    """Protocol for static data changelog classes."""

    async def download(self, output_path: Path | None) -> dict[str, Any]:
        """Download the static data changelog."""
        ...

    def load(self, input_path: Path) -> dict[str, Any]:
        """Load the static data changelog."""
        ...


class StaticDataSchemaChangelogProtocol(Protocol):
    """Protocol for static data schema changelog classes."""

    async def download(self, output_path: Path | None) -> dict[str, Any]:
        """Download the static data schema changelog."""
        ...

    def load(self, input_path: Path) -> dict[str, Any]:
        """Load the static data schema changelog."""
        ...
