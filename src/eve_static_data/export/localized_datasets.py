from copy import deepcopy
from pathlib import Path

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models.datasets import localized_pydantic as LDS
from eve_static_data.models.datasets import sde_pydantic as ED
from eve_static_data.models.datasets.exported_dataset_files import (
    DerivedLocalizedDatasetFiles,
    ExportedDatasetFiles,
    ExportedLocalizedDatasetFiles,
)
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset


def export_localized_datasets(
    reader: SdeReader, output_dir: Path, overwrite: bool = False
) -> None:
    """Export localized datasets to JSON files."""
    ancestries_dataset = LDS.AncestriesLocalizedDataset.from_sde(reader)
    ancestries_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.ANCESTRIES, overwrite=overwrite
    )

    blueprints_dataset = ED.BlueprintsDataset.from_sde(reader)
    blueprints_dataset.save_to_disk(
        output_dir / ExportedDatasetFiles.BLUEPRINTS, overwrite=overwrite
    )

    categories_dataset = LDS.CategoriesLocalizedDataset.from_sde(reader)
    categories_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.CATEGORIES, overwrite=overwrite
    )

    groups_dataset = LDS.GroupsLocalizedDataset.from_sde(reader)
    groups_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.GROUPS, overwrite=overwrite
    )

    map_regions_dataset = LDS.MapRegionsLocalizedDataset.from_sde(reader)
    map_regions_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.MAP_REGIONS, overwrite=overwrite
    )

    map_solarsystem_dataset = LDS.MapSolarSystemsLocalizedDataset.from_sde(reader)
    map_solarsystem_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.MAP_SOLARSYSTEMS, overwrite=overwrite
    )

    market_groups_dataset = LDS.MarketGroupsLocalizedDataset.from_sde(reader)
    market_groups_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.MARKET_GROUPS, overwrite=overwrite
    )

    meta_groups_dataset = LDS.MetaGroupsLocalizedDataset.from_sde(reader)
    meta_groups_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.META_GROUPS, overwrite=overwrite
    )

    type_materials_dataset = ED.TypeMaterialsDataset.from_sde(reader)
    type_materials_dataset.save_to_disk(
        output_dir / ExportedDatasetFiles.TYPE_MATERIALS, overwrite=overwrite
    )

    eve_types_dataset = LDS.EveTypesLocalizedDataset.from_sde(reader)
    eve_types_dataset.save_to_disk(
        output_dir / ExportedLocalizedDatasetFiles.EVE_TYPES, overwrite=overwrite
    )

    # ------------------------------------------
    # Derived datasets
    # ------------------------------------------

    market_paths_dataset = MarketPathsDataset.from_dataset(market_groups_dataset)
    market_paths_dataset.save_to_disk(
        output_dir / DerivedLocalizedDatasetFiles.MARKET_PATHS, overwrite=overwrite
    )

    normalized_eve_types_dataset = NormalizedEveTypesDataset.from_datasets(
        eve_types_dataset=eve_types_dataset,
        groups_dataset=groups_dataset,
        categories_dataset=categories_dataset,
        market_groups_dataset=market_groups_dataset,
        meta_groups_dataset=meta_groups_dataset,
    )
    normalized_eve_types_dataset.save_to_disk(
        output_dir / DerivedLocalizedDatasetFiles.NORMALIZED_EVE_TYPES,
        overwrite=overwrite,
    )

    normalized_eve_types_published_dataset = deepcopy(normalized_eve_types_dataset)
    for key, record in list(normalized_eve_types_published_dataset.data.items()):
        if not record.published:
            normalized_eve_types_published_dataset.data.pop(key)
    normalized_eve_types_published_dataset.save_to_disk(
        output_dir / DerivedLocalizedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED,
        overwrite=overwrite,
    )
