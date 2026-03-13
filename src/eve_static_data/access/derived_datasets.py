"""Datasets derived from the SDE and localized datasets.

Subsets or combinations of data in a more useful or quicker loading form.

For best performance, generate these once, and save them to disk.
"""

from pathlib import Path

from eve_static_data.access import localized_datasets as LDA
from eve_static_data.access import sde_datasets as SDA
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames
from eve_static_data.models.type_defs import Lang


def market_paths(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> MarketPathsDataset:
    """Load the market paths dataset for the specified language."""
    market_groups = LDA.market_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    market_paths = MarketPathsDataset.from_dataset(market_groups)
    return market_paths


def normalized_eve_types(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> NormalizedEveTypesDataset:
    """Load the normalized eve types dataset for the specified language."""
    eve_types = LDA.eve_types_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    categories = LDA.categories_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    groups = LDA.groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    meta_groups = LDA.meta_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    market_groups = LDA.market_groups_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    normalized_eve_types = NormalizedEveTypesDataset.from_datasets(
        eve_types_dataset=eve_types,
        categories_dataset=categories,
        groups_dataset=groups,
        meta_groups_dataset=meta_groups,
        market_groups_dataset=market_groups,
    )
    return normalized_eve_types


def region_names(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> RegionNames:
    """Load the region names dataset for the specified language."""
    map_regions = LDA.map_regions_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    region_names = RegionNames.from_datasets(map_regions)
    return region_names


def system_names(
    sde_path: Path,
    lang: Lang,
    only_published: bool = True,
    skip_validation_failures: bool = False,
) -> SystemNames:
    """Load the system names dataset for the specified language."""
    map_solar_systems = LDA.map_solar_systems_localized(
        sde_path,
        lang,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    system_names = SystemNames.from_datasets(map_solar_systems)
    return system_names
