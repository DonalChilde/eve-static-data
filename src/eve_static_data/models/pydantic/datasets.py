"""Models for datasets in the EVE Static Data Export (SDE)."""

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import records as PM


class SdeDataset(BaseModel):
    build_number: int
    release_date: str


class BlueprintsDataset(SdeDataset):
    records: dict[int, PM.Blueprints]


LOOKUP: dict[SdeDatasetFiles, type[SdeDataset]] = {
    SdeDatasetFiles.BLUEPRINTS: BlueprintsDataset,
}
