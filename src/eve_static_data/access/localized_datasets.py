"""Functions for loading localized datasets from an unpacked SDE directory."""

from pathlib import Path

from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.pydantic import localized_datasets as LDS
from eve_static_data.models.pydantic import localized_records as LPM
from eve_static_data.models.type_defs import Lang


class LocalizedDatasetLoader:
    """Loader for localized datasets from an unpacked SDE directory."""

    def __init__(self, sde_path: Path):
        """Loader for localized datasets from an unpacked SDE directory."""
        self.sde_path = sde_path

    def ancestries(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.AncestriesLocalizedDataset:
        """Load the ancestries localized dataset for the specified language."""
        return ancestries_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def categories(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.CategoriesLocalizedDataset:
        """Load the categories localized dataset for the specified language."""
        return categories_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def eve_types(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.EveTypesLocalizedDataset:
        """Load the eve types localized dataset for the specified language."""
        return eve_types_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def groups(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.GroupsLocalizedDataset:
        """Load the groups localized dataset for the specified language."""
        return groups_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_regions(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.MapRegionsLocalizedDataset:
        """Load the map regions localized dataset for the specified language."""
        return map_regions_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_solar_systems(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.MapSolarSystemsLocalizedDataset:
        """Load the map solar systems localized dataset for the specified language."""
        return map_solar_systems_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def market_groups(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.MarketGroupsLocalizedDataset:
        """Load the market groups localized dataset for the specified language."""
        return market_groups_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def meta_groups(
        self,
        lang: Lang = "en",
        only_published: bool = True,
        skip_validation_failures: bool = False,
    ) -> LDS.MetaGroupsLocalizedDataset:
        """Load the meta groups localized dataset for the specified language."""
        return meta_groups_localized(
            sde_path=self.sde_path,
            lang=lang,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )


# --------------------------------------------------------------------------------------
# The following functions are for loading localized datasets directly without using the loader class.
# --------------------------------------------------------------------------------------


def ancestries_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.AncestriesLocalizedDataset:
    """Load the ancestries localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)

    records = LPM.read_records(
        sde_path,
        LPM.AncestriesLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.AncestriesLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def categories_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.CategoriesLocalizedDataset:
    """Load the categories localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.CategoriesLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.CategoriesLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def eve_types_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.EveTypesLocalizedDataset:
    """Load the eve types localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.EveTypesLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.EveTypesLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def groups_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.GroupsLocalizedDataset:
    """Load the groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.GroupsLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.GroupsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def map_regions_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.MapRegionsLocalizedDataset:
    """Load the map regions localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.MapRegionsLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.MapRegionsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def map_solar_systems_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.MapSolarSystemsLocalizedDataset:
    """Load the map solar systems localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.MapSolarSystemsLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.MapSolarSystemsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def market_groups_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.MarketGroupsLocalizedDataset:
    """Load the market groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.MarketGroupsLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.MarketGroupsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def meta_groups_localized(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> LDS.MetaGroupsLocalizedDataset:
    """Load the meta groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    records = LPM.read_records(
        sde_path,
        LPM.MetaGroupsLocalized,
        only_published=only_published,
        lang=lang,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.MetaGroupsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset
