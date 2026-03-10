"""An incomplete set of models for localized SDE datasets.

More models to be added as needed for use.
"""

from pathlib import Path
from typing import Self

from pydantic import BaseModel

from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic import localized_records as LPM
from eve_static_data.models.type_defs import Lang
from eve_static_data.transformers import LocalizationTransformer


class SdeDatasetLocalized(BaseModel):
    build_number: int
    release_date: str
    lang: Lang

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create an instance of SdeDataset from a JSONL file."""
        raise NotImplementedError("This method should be implemented in a subclass.")


class AncestriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.AncestriesLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.AncestriesLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create an AncestriesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.AncestriesLocalized] = {}
        for index, record in LPM.AncestriesLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class CategoriesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.CategoriesLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.CategoriesLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a CategoriesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.CategoriesLocalized] = {}
        for index, record in LPM.CategoriesLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class GroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.GroupsLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.GroupsLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a GroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.GroupsLocalized] = {}
        for index, record in LPM.GroupsLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class MapRegionsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapRegionsLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.MapRegionsLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a MapRegionsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MapRegionsLocalized] = {}
        for index, record in LPM.MapRegionsLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class MapSolarSystemsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MapSolarSystemsLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.MapSolarSystemsLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a MapSolarSystemsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MapSolarSystemsLocalized] = {}
        for index, record in LPM.MapSolarSystemsLocalized.transform(
            file_path, localizer
        ):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class MarketGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MarketGroupsLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.MarketGroupsLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a MarketGroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MarketGroupsLocalized] = {}
        for index, record in LPM.MarketGroupsLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class MetaGroupsLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.MetaGroupsLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.MetaGroupsLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create a MetaGroupsLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.MetaGroupsLocalized] = {}
        for index, record in LPM.MetaGroupsLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
            records=records,
        )


class EveTypesLocalizedDataset(SdeDatasetLocalized):
    records: dict[int, LPM.EveTypesLocalized]

    @classmethod
    def get_localizer(cls, lang: Lang) -> LocalizationTransformer:
        """Get a localizer for this dataset and the specified language."""
        return LPM.EveTypesLocalized.get_transformer(lang)

    @classmethod
    def from_jsonl_file(
        cls,
        file_path: Path | str,
        build_number: int,
        release_date: str,
        localizer: LocalizationTransformer,
    ) -> Self:
        """Create an EveTypesLocalizedDataset instance from a JSONL file."""
        records: dict[int, LPM.EveTypesLocalized] = {}
        for index, record in LPM.EveTypesLocalized.transform(file_path, localizer):
            _ = index
            if record is not None:
                records[record.key] = record
        return cls(
            build_number=build_number,
            release_date=release_date,
            lang=localizer.lang,
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
