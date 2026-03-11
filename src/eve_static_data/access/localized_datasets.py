"""Functions for loading localized datasets from an unpacked SDE directory."""

from pathlib import Path

from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.pydantic import localized_datasets as LDS
from eve_static_data.models.pydantic import localized_records as LPM
from eve_static_data.models.type_defs import Lang


def ancestries_localized(
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.AncestriesLocalizedDataset:
    """Load the ancestries localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.AncestriesLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
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
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.CategoriesLocalizedDataset:
    """Load the categories localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.CategoriesLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.CategoriesLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def groups_localized(
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.GroupsLocalizedDataset:
    """Load the groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.GroupsLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
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
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.MapRegionsLocalizedDataset:
    """Load the map regions localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.MapRegionsLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
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
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.MapSolarSystemsLocalizedDataset:
    """Load the map solar systems localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.MapSolarSystemsLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
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
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.MarketGroupsLocalizedDataset:
    """Load the market groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.MarketGroupsLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
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
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.MetaGroupsLocalizedDataset:
    """Load the meta groups localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.MetaGroupsLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.MetaGroupsLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset


def eve_types_localized(
    sde_path: Path, lang: Lang, only_published: bool = True
) -> LDS.EveTypesLocalizedDataset:
    """Load the eve types localized dataset for the specified language."""
    sde_info = load_sde_info(sde_path)
    model = LPM.EveTypesLocalized
    records = LPM.read_records(
        sde_path, model, only_published=only_published, lang=lang
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = LDS.EveTypesLocalizedDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        lang=lang,
        records=records_dict,
    )
    return dataset
