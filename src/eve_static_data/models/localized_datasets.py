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


class CategoriesDataset(SdeDataset):
    data: dict[int, PML.CategoriesLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a CategoriesDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.categories():
            item = PML.CategoriesLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class GroupsDataset(SdeDataset):
    data: dict[int, PML.GroupsLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a GroupsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.groups():
            item = PML.GroupsLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class MapRegionsDataset(SdeDataset):
    data: dict[int, PML.MapRegionsLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a MapRegionsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.map_regions():
            item = PML.MapRegionsLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class MapSolarSystemsDataset(SdeDataset):
    data: dict[int, PML.MapSolarSystemsLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a MapSolarSystemsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.map_solar_systems():
            item = PML.MapSolarSystemsLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class MarketGroupsDataset(SdeDataset):
    data: dict[int, PML.MarketGroupsLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a MarketGroupsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.market_groups():
            item = PML.MarketGroupsLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class MetaGroupsDataset(SdeDataset):
    data: dict[int, PML.MetaGroupsLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a MetaGroupsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.meta_groups():
            item = PML.MetaGroupsLocalized.from_sde(record)
            result.data[item.key] = item
        return result


class TypeMaterialsDataset(SdeDataset):
    data: dict[int, PM.TypeMaterials]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create a TypeMaterialsDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.type_materials():
            item = PM.TypeMaterials.from_sde(record)
            result.data[item.key] = item
        return result


class EveTypesDataset(SdeDataset):
    data: dict[int, PML.EveTypesLocalized]

    @classmethod
    def from_sde(cls, sde_records: SDERecordsTD) -> Self:
        """Create an EveTypesDataset instance from SDE records."""
        if sde_records.build_number is None or sde_records.release_date is None:
            raise ValueError("SDE Reader must have build number and release date.")
        result = cls(
            build_number=sde_records.build_number,
            release_date=sde_records.release_date,
            data={},
        )
        for record in sde_records.eve_types():
            item = PML.EveTypesLocalized.from_sde(record)
            result.data[item.key] = item
        return result
