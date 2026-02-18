"""An incomplete set of models for localized SDE data.

More models to be added as needed for use.
"""

from typing import Self

from eve_static_data.access.sde_records_td import SDERecordsTD
from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk
from eve_static_data.models import sde_pydantic as PM
from eve_static_data.models import sde_pydantic_localized as PML


class SdeDataset(BaseModelToDisk):
    build_number: int
    release_date: str


class AncestriesDataset(SdeDataset):
    data: dict[int, PML.AncestriesLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create an AncestriesDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.ancestries():
            item = PML.AncestriesLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class BlueprintsDataset(SdeDataset):
    data: dict[int, PM.Blueprints]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a BlueprintsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.blueprints():
            item = PM.Blueprints.from_sde(record)
            result.data[item.key] = item
        return result
