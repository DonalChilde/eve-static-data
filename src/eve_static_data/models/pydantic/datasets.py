"""Models for datasets in the EVE Static Data Export (SDE)."""

from typing import Self

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM


class SdeDataset(BaseModel):
    build_number: int
    release_date: str

    @classmethod
    def from_jsonl_file(
        cls, file_path: str, build_number: int, release_date: str
    ) -> Self:
        """Create an instance of SdeDataset from a JSONL file."""
        raise NotImplementedError("This method should be implemented in a subclass.")


class BlueprintsDataset(SdeDataset):
    records: dict[int, PM.Blueprints]

    @classmethod
    def from_jsonl_file(
        cls, file_path: str, build_number: int, release_date: str
    ) -> Self:
        """Create a BlueprintsDataset instance from a JSONL file."""
        records: dict[int, PM.Blueprints] = {}
        for record, index in PM.Blueprints.from_jsonl_file(file_path):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number, release_date=release_date, records=records
        )


LOOKUP: dict[SdeDatasetFiles, type[SdeDataset]] = {
    SdeDatasetFiles.BLUEPRINTS: BlueprintsDataset,
}
