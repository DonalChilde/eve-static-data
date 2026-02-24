"""The base dataset model for SDE datasets, containing common metadata fields."""

from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk


class SdeDataset(BaseModelToDisk):
    build_number: int
    release_date: str
