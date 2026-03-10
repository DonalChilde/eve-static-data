# """functions for working with SDE data in the app directory."""

# import logging
# import shutil
# import tempfile
# import zipfile
# from copy import deepcopy
# from pathlib import Path
# from time import perf_counter

# from eve_static_data.access.sde_reader import SdeReader
# from eve_static_data.helpers import app_data as AD
# from eve_static_data.models import derived as derived_models
# from eve_static_data.models.datasets import localized_pydantic as LDS
# from eve_static_data.models.datasets.sde_dataset_files import DerivedDatasetFiles

# logger = logging.getLogger(__name__)


# def import_zipped_sde(zip_file_path: Path, data_path: Path) -> int:
#     """Import SDE data from a zipped file.

#     This function will unzip the provided zip file to a temporary directory, validate the presence of the expected
#     "_sde.jsonl" file, and then copy the relevant JSONL files to the appropriate location in the data directory.

#     Args:
#         zip_file_path: The path to the zipped SDE data file.
#         data_path: The path to the data directory.

#     Returns:
#         The build number of the imported SDE data.
#     """
#     with tempfile.TemporaryDirectory() as temp_dir:
#         temp_path = Path(temp_dir)

#         # Unzip the file to the temporary directory
#         with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
#             zip_ref.extractall(temp_path)
#         if not (temp_path / "_sde.jsonl").exists():
#             raise FileNotFoundError(
#                 f"_sde.jsonl file not found in the unzipped SDE data at {temp_path}. Is this a valid SDE zip file?"
#             )
#         return import_unzipped_sde(temp_path, data_path=data_path)


# def import_unzipped_sde(unzipped_path: Path, data_path: Path) -> int:
#     """Import SDE data from an unzipped directory.

#     This function will validate the presence of the expected "_sde.jsonl" file in the provided directory, and then
#     copy the relevant JSONL files to the appropriate location in the data directory.

#     Args:
#         unzipped_path: The path to the unzipped SDE data directory.
#         data_path: The path to the data directory.

#     Returns:
#         The build number of the imported SDE data.
#     """
#     if not unzipped_path.exists() or not unzipped_path.is_dir():
#         raise FileNotFoundError(
#             f"Unzipped SDE data directory not found at {unzipped_path}"
#         )
#     if not (unzipped_path / "_sde.jsonl").exists():
#         raise FileNotFoundError(
#             f"_sde.jsonl file not found in the unzipped SDE data at {unzipped_path}. Is "
#             "this a valid SDE data directory?"
#         )
#     reader = SdeReader(unzipped_path)

#     if reader.build_number is None:
#         raise ValueError(
#             f"Build number not found in _sde.jsonl file at {unzipped_path / '_sde.jsonl'}"
#         )
#     build_number = reader.build_number
#     AD.init_dirs(data_path, build_number)
#     build_sde_dir = AD.sde_dir(data_path, build_number)

#     # Copy JSONL files from unzipped directory to the appropriate location in the data directory
#     for file in unzipped_path.glob("*.jsonl"):
#         target_file = build_sde_dir / file.name
#         if target_file.exists():
#             raise FileExistsError(
#                 f"Target file {target_file} already exists. Cannot copy {file} to {target_file}"
#             )
#         shutil.copy(file, target_file)

#     return build_number


# def generate_derived_datasets_for_build(
#     data_path: Path, build_number: int, localized: str = "en"
# ) -> None:
#     """Generate derived datasets for a specific build number.

#     This function will read the SDE data for the specified build number, generate the derived datasets, and save them
#     to the appropriate location in the data directory.

#     Args:
#         data_path: The path to the data directory.
#         build_number: The build number for which to generate derived datasets.
#         localized: The localization to use for the derived datasets. Defaults to "en".
#     """
#     sde_dir = AD.sde_dir(data_path, build_number)
#     derived_dir = AD.derived_dir(data_path, build_number)
#     generate_derived_datasets(sde_dir, derived_dir, localized=localized)


# # TODO move this function to a more generic location,
# # to devide up app and general functions.
# def generate_derived_datasets(
#     sde_path: Path, dir_out: Path, localized: str = "en"
# ) -> None:
#     """Generate derived datasets for a specific build number.

#     This function will read the SDE data for the specified build number, generate the derived datasets, and save them
#     to the appropriate location in the data directory.

#     Args:
#         sde_path: The path to the SDE data directory.
#         dir_out: The directory where the derived datasets should be saved.
#         localized: The localization to use for the derived datasets. Defaults to "en".
#     """
#     logger.info(f"Generating derived datasets for SDE data at {sde_path}")
#     start = perf_counter()
#     reader = SdeReader(sde_path)
#     categories_dataset = LDS.CategoriesLocalizedDataset.from_sde(
#         reader, localized=localized
#     )
#     groups_dataset = LDS.GroupsLocalizedDataset.from_sde(reader, localized=localized)
#     map_regions_dataset = LDS.MapRegionsLocalizedDataset.from_sde(
#         reader, localized=localized
#     )
#     map_solarsystem_dataset = LDS.MapSolarSystemsLocalizedDataset.from_sde(
#         reader, localized=localized
#     )
#     market_groups_dataset = LDS.MarketGroupsLocalizedDataset.from_sde(
#         reader, localized=localized
#     )
#     meta_groups_dataset = LDS.MetaGroupsLocalizedDataset.from_sde(
#         reader, localized=localized
#     )
#     eve_types_dataset = LDS.EveTypesLocalizedDataset.from_sde(
#         reader, localized=localized
#     )

#     # MarketPathsDataset
#     market_paths_dataset = derived_models.MarketPathsDataset.from_dataset(
#         market_groups_dataset
#     )
#     market_paths_dataset.save_to_disk(
#         dir_out / DerivedDatasetFiles.MARKET_PATHS.localized(localized),
#     )

#     # NormalizedEveTypesDataset
#     normalized_eve_types_dataset = (
#         derived_models.NormalizedEveTypesDataset.from_datasets(
#             eve_types_dataset,
#             groups_dataset,
#             categories_dataset,
#             market_groups_dataset,
#             meta_groups_dataset,
#         )
#     )
#     normalized_eve_types_dataset.save_to_disk(
#         dir_out / DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(localized),
#     )

#     # NormalizedEveTypesPublishedDataset
#     normalized_eve_types_published_dataset = deepcopy(normalized_eve_types_dataset)
#     for key, record in list(normalized_eve_types_published_dataset.data.items()):
#         if not record.published:
#             normalized_eve_types_published_dataset.data.pop(key)
#     normalized_eve_types_published_dataset.save_to_disk(
#         dir_out
#         / DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(localized),
#     )

#     # RegionNamesDataset
#     region_names_dataset = derived_models.RegionNames.from_datasets(map_regions_dataset)
#     region_names_dataset.save_to_disk(
#         dir_out / DerivedDatasetFiles.REGION_NAMES.localized(localized),
#     )

#     # SystemNamesDataset
#     system_names_dataset = derived_models.SystemNames.from_datasets(
#         map_solarsystem_dataset
#     )
#     system_names_dataset.save_to_disk(
#         dir_out / DerivedDatasetFiles.SYSTEM_NAMES.localized(localized),
#     )
#     logger.info(
#         f"Derived datasets generated and saved to {dir_out} in {perf_counter() - start:.4f} seconds"
#     )
