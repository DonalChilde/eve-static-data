"""The base dataset model for SDE datasets, containing common metadata fields."""

from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk


class SdeDataset(BaseModelToDisk):
    build_number: int
    release_date: str


class LocalizedSdeDataset(SdeDataset):
    """Base class for localized SDE datasets."""

    localized: str
