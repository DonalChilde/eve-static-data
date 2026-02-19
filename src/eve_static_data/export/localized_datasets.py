from copy import deepcopy
from pathlib import Path

from eve_static_data.access.sde_records_td import SDERecordsTD
from eve_static_data.models import localized_datasets as LDS
from eve_static_data.models.localized_dataset_files import LocalizedDatasetFiles
from eve_static_data.models.market_path import MarketPathsDataset
from eve_static_data.models.normalized_eve_type import NormalizedEveTypesDataset


def export_localized_datasets(
    sde_records: SDERecordsTD, output_dir: Path, overwrite: bool = False
) -> None:
    """Export localized datasets to JSON files."""
    ancestries_dataset = LDS.AncestriesDataset.from_sde(sde_records)
    ancestries_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.ANCESTRIES, overwrite=overwrite
    )

    blueprints_dataset = LDS.BlueprintsDataset.from_sde(sde_records)
    blueprints_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.BLUEPRINTS, overwrite=overwrite
    )

    categories_dataset = LDS.CategoriesDataset.from_sde(sde_records)
    categories_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.CATEGORIES, overwrite=overwrite
    )

    groups_dataset = LDS.GroupsDataset.from_sde(sde_records)
    groups_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.GROUPS, overwrite=overwrite
    )

    map_regions_dataset = LDS.MapRegionsDataset.from_sde(sde_records)
    map_regions_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.MAP_REGIONS, overwrite=overwrite
    )

    map_solarsystem_dataset = LDS.MapSolarSystemsDataset.from_sde(sde_records)
    map_solarsystem_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.MAP_SOLARSYSTEMS, overwrite=overwrite
    )

    market_groups_dataset = LDS.MarketGroupsDataset.from_sde(sde_records)
    market_groups_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.MARKET_GROUPS, overwrite=overwrite
    )

    meta_groups_dataset = LDS.MetaGroupsDataset.from_sde(sde_records)
    meta_groups_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.META_GROUPS, overwrite=overwrite
    )

    type_materials_dataset = LDS.TypeMaterialsDataset.from_sde(sde_records)
    type_materials_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.TYPE_MATERIALS, overwrite=overwrite
    )

    eve_types_dataset = LDS.EveTypesDataset.from_sde(sde_records)
    eve_types_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.EVE_TYPES, overwrite=overwrite
    )

    # ------------------------------------------
    # Derived datasets
    # ------------------------------------------

    market_paths_dataset = MarketPathsDataset.from_dataset(market_groups_dataset)
    market_paths_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.MARKET_PATHS, overwrite=overwrite
    )

    normalized_eve_types_dataset = NormalizedEveTypesDataset.from_datasets(
        eve_types_dataset=eve_types_dataset,
        groups_dataset=groups_dataset,
        categories_dataset=categories_dataset,
        market_groups_dataset=market_groups_dataset,
        meta_groups_dataset=meta_groups_dataset,
    )
    normalized_eve_types_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.NORMALIZED_EVE_TYPES, overwrite=overwrite
    )

    normalized_eve_types_published_dataset = deepcopy(normalized_eve_types_dataset)
    for key, record in list(normalized_eve_types_published_dataset.data.items()):
        if not record.published:
            normalized_eve_types_published_dataset.data.pop(key)
    normalized_eve_types_published_dataset.save_to_disk(
        output_dir / LocalizedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED,
        overwrite=overwrite,
    )
