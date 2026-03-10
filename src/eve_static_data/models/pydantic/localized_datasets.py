"""An incomplete set of models for localized SDE datasets.

More models to be added as needed for use.
"""

from pathlib import Path
from typing import Self

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import localized_records as LPM
from eve_static_data.models.type_defs import Lang


class SdeDatasetLocalized(BaseModel):
    build_number: int
    release_date: str
    lang: Lang

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create an instance of SdeDataset from a JSONL file."""
        raise NotImplementedError("This method should be implemented in a subclass.")


class AncestriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.AncestriesLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create an AncestriesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.AncestriesLocalized] = {}
        for record, index in LPM.AncestriesLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class CategoriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.CategoriesLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a CategoriesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.CategoriesLocalized] = {}
        for record, index in LPM.CategoriesLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class GroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.GroupsLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a GroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.GroupsLocalized] = {}
        for record, index in LPM.GroupsLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class MapRegionsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapRegionsLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a MapRegionsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MapRegionsLocalized] = {}
        for record, index in LPM.MapRegionsLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class MapSolarSystemsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapSolarSystemsLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a MapSolarSystemsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MapSolarSystemsLocalized] = {}
        for record, index in LPM.MapSolarSystemsLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class MarketGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MarketGroupsLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a MarketGroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MarketGroupsLocalized] = {}
        for record, index in LPM.MarketGroupsLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class MetaGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MetaGroupsLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create a MetaGroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MetaGroupsLocalized] = {}
        for record, index in LPM.MetaGroupsLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


class EveTypesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.EveTypesLocalized]

    @classmethod
    def from_jsonl_file(
        cls, file_path: Path | str, build_number: int, release_date: str, lang: Lang
    ) -> Self:
        """Create an EveTypesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.EveTypesLocalized] = {}
        for record, index in LPM.EveTypesLocalized.localize(file_path, lang):
            _ = index
            records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=lang,
            records=records,
        )


LOOKUP: dict[SdeDatasetFiles, type[SdeDatasetLocalized]] = {
    SdeDatasetFiles.ANCESTRIES: AncestriesLocalizedDataset,
    SdeDatasetFiles.CATEGORIES: CategoriesLocalizedDataset,
    SdeDatasetFiles.GROUPS: GroupsLocalizedDataset,
    SdeDatasetFiles.MAP_REGIONS: MapRegionsLocalizedDataset,
    SdeDatasetFiles.MAP_SOLAR_SYSTEMS: MapSolarSystemsLocalizedDataset,
    SdeDatasetFiles.MARKET_GROUPS: MarketGroupsLocalizedDataset,
    SdeDatasetFiles.META_GROUPS: MetaGroupsLocalizedDataset,
    SdeDatasetFiles.TYPES: EveTypesLocalizedDataset,
}
