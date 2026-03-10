"""Generate derived datasets for a specific build number."""

import logging
from copy import deepcopy
from pathlib import Path
from time import perf_counter

from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.dataset_filenames import (
    DerivedDatasetFiles,
    SdeDatasetFiles,
)
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames
from eve_static_data.models.pydantic import localized_datasets as LDS
from eve_static_data.models.type_defs import Lang

logger = logging.getLogger(__name__)


def generate_derived_datasets(
    input_path: Path, output_path: Path, lang: Lang = "en"
) -> None:
    """Generate derived datasets for a specific build number.

    This function will read the SDE data for the specified build number, generate the derived datasets, and save them
    to the appropriate location in the data directory.

    Args:
        input_path: The path to the SDE data directory.
        output_path: The directory where the derived datasets should be saved.
        lang: The localization to use for the derived datasets. Defaults to "en".
    """
    logger.info(f"Generating derived datasets for SDE data at {input_path}")
    if not input_path.is_dir():
        raise ValueError(f"Input path {input_path} is not a directory.")
    if output_path.is_file():
        raise ValueError(f"Output path {output_path} is a file, expected a directory.")
    start = perf_counter()
    sde_info = load_sde_info(input_path)

    # Load localized datasets needed to create the derived datasets.
    categories_file = input_path / SdeDatasetFiles.CATEGORIES.as_jsonl()
    categories_localier = LDS.CategoriesLocalizedDataset.get_localizer(lang)
    categories_dataset = LDS.CategoriesLocalizedDataset.from_jsonl_file(
        file_path=categories_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=categories_localier,
    )
    groups_file = input_path / SdeDatasetFiles.GROUPS.as_jsonl()
    groups_localizer = LDS.GroupsLocalizedDataset.get_localizer(lang)
    groups_dataset = LDS.GroupsLocalizedDataset.from_jsonl_file(
        file_path=groups_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=groups_localizer,
    )
    map_regions_file = input_path / SdeDatasetFiles.MAP_REGIONS.as_jsonl()
    map_regions_localizer = LDS.MapRegionsLocalizedDataset.get_localizer(lang)
    map_regions_dataset = LDS.MapRegionsLocalizedDataset.from_jsonl_file(
        file_path=map_regions_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=map_regions_localizer,
    )
    map_solarsystem_file = input_path / SdeDatasetFiles.MAP_SOLAR_SYSTEMS.as_jsonl()
    map_solarsystem_localizer = LDS.MapSolarSystemsLocalizedDataset.get_localizer(lang)
    map_solarsystem_dataset = LDS.MapSolarSystemsLocalizedDataset.from_jsonl_file(
        file_path=map_solarsystem_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=map_solarsystem_localizer,
    )
    market_groups_file = input_path / SdeDatasetFiles.MARKET_GROUPS.as_jsonl()
    market_groups_localizer = LDS.MarketGroupsLocalizedDataset.get_localizer(lang)
    market_groups_dataset = LDS.MarketGroupsLocalizedDataset.from_jsonl_file(
        file_path=market_groups_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=market_groups_localizer,
    )
    meta_groups_file = input_path / SdeDatasetFiles.META_GROUPS.as_jsonl()
    meta_groups_localizer = LDS.MetaGroupsLocalizedDataset.get_localizer(lang)
    meta_groups_dataset = LDS.MetaGroupsLocalizedDataset.from_jsonl_file(
        file_path=meta_groups_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=meta_groups_localizer,
    )
    eve_types_file = input_path / SdeDatasetFiles.TYPES.as_jsonl()
    eve_types_localizer = LDS.EveTypesLocalizedDataset.get_localizer(lang)
    eve_types_dataset = LDS.EveTypesLocalizedDataset.from_jsonl_file(
        file_path=eve_types_file,
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        localizer=eve_types_localizer,
    )

    # MarketPathsDataset
    market_paths_dataset = MarketPathsDataset.from_dataset(market_groups_dataset)
    market_paths_file = output_path / DerivedDatasetFiles.MARKET_PATHS.localized(lang)
    market_paths_file.parent.mkdir(parents=True, exist_ok=True)
    market_paths_file.write_text(market_paths_dataset.model_dump_json(indent=2))

    # NormalizedEveTypesDataset
    normalized_eve_types_dataset = NormalizedEveTypesDataset.from_datasets(
        eve_types_dataset,
        groups_dataset,
        categories_dataset,
        market_groups_dataset,
        meta_groups_dataset,
    )
    normalized_eve_types_file = (
        output_path / DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(lang)
    )
    normalized_eve_types_file.parent.mkdir(parents=True, exist_ok=True)
    normalized_eve_types_file.write_text(
        normalized_eve_types_dataset.model_dump_json(indent=2)
    )

    # NormalizedEveTypesPublishedDataset
    normalized_eve_types_published_dataset = deepcopy(normalized_eve_types_dataset)
    for key, record in list(normalized_eve_types_published_dataset.records.items()):
        if not record.published:
            normalized_eve_types_published_dataset.records.pop(key)
    normalized_eve_types_published_file = (
        output_path / DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(lang)
    )
    normalized_eve_types_published_file.parent.mkdir(parents=True, exist_ok=True)
    normalized_eve_types_published_file.write_text(
        normalized_eve_types_published_dataset.model_dump_json(indent=2)
    )

    # RegionNamesDataset
    region_names_dataset = RegionNames.from_datasets(map_regions_dataset)
    region_names_file = output_path / DerivedDatasetFiles.REGION_NAMES.localized(lang)
    region_names_file.parent.mkdir(parents=True, exist_ok=True)
    region_names_file.write_text(region_names_dataset.model_dump_json(indent=2))

    # SystemNamesDataset
    system_names_dataset = SystemNames.from_datasets(map_solarsystem_dataset)
    system_names_file = output_path / DerivedDatasetFiles.SYSTEM_NAMES.localized(lang)
    system_names_file.parent.mkdir(parents=True, exist_ok=True)
    system_names_file.write_text(system_names_dataset.model_dump_json(indent=2))
    logger.info(
        f"Derived datasets generated and saved to {output_path} in {perf_counter() - start:.4f} seconds"
    )
