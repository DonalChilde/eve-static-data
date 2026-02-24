"""functions for working with SDE data in the app directory."""

import logging
import shutil
import tempfile
import zipfile
from copy import deepcopy
from pathlib import Path
from time import perf_counter

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models import derived as derived_models
from eve_static_data.models.datasets import localized_pydantic as LDS
from eve_static_data.models.datasets.sde_dataset_files import DerivedDatasetFiles
from eve_static_data.sde_data.validation import validate_and_save_validation_results
from eve_static_data.settings import get_settings

logger = logging.getLogger(__name__)


def available_builds(data_path: Path) -> list[int]:
    """Get a list of available build numbers.

    From the data_path, sde builds are expected to be subdirectories named with the
    build number, e.g. "1234567". This function will check for the presence of a "_sde.jsonl"
    file in each build directory and return a list of all available build numbers.

    Args:
        data_path: The path to the app data directory.
    """
    build_directories = [
        d for d in data_path.iterdir() if d.is_dir() and d.name.isdigit()
    ]
    valid_builds: list[int] = []
    for build_dir in build_directories:
        sde_info_file = build_dir / "_sde.jsonl"
        if sde_info_file.exists():
            valid_builds.append(int(build_dir.name))
    return valid_builds


def path_to_sde(build_number: int | None = None) -> Path:
    """Get the path to the SDE.

    If a build number is provided, the path will be constructed using the build number,
    otherwise it will be the most recent build.
    """
    build_data_dir = path_to_build_data_dir(build_number)
    sde_path = build_data_dir / "sde"
    if not sde_path.exists():
        raise FileNotFoundError(f"SDE data not found at {sde_path}")
    return sde_path


def path_to_derived(build_number: int | None = None) -> Path:
    """Get the path to the derived datasets for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.

    Returns:
        The path to the derived datasets for the specified build number.
    """
    build_data_dir = path_to_build_data_dir(build_number)
    derived_path = build_data_dir / "derived"
    if not derived_path.exists():
        raise FileNotFoundError(
            f"Derived datasets for build {build_number} not found at {derived_path}"
        )
    return derived_path


def path_to_validation(build_number: int | None = None) -> Path:
    """Get the path to the validation results for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
    """
    build_data_dir = path_to_build_data_dir(build_number)
    validation_path = build_data_dir / "validation"
    if not validation_path.exists():
        raise FileNotFoundError(
            f"Validation results for build {build_number} not found at {validation_path}"
        )
    return validation_path


def initialize_build_data(build_number: int) -> None:
    """Initialize the build data directory for a specific build number.

    This function will create the necessary directory structure for the specified build number,
    including the "sde", "validation", and "derived" subdirectories.

    Args:
        build_number: The build number to initialize the data for.
    """
    settings = get_settings()
    data_path = Path(settings.data_path)
    build_data_dir = data_path / str(build_number)
    if build_data_dir.exists():
        raise FileExistsError(
            f"Data directory for build {build_number} already exists at {build_data_dir}"
        )
    build_data_dir.mkdir(parents=True, exist_ok=False)
    (build_data_dir / "sde").mkdir(parents=True, exist_ok=False)
    (build_data_dir / "validation").mkdir(parents=True, exist_ok=False)
    (build_data_dir / "derived").mkdir(parents=True, exist_ok=False)
    logger.info(
        f"Initialized data directory for build {build_number} at {build_data_dir}"
    )


def path_to_build_data_dir(build_number: int | None = None) -> Path:
    """Get the path to the build data directory for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
    """
    settings = get_settings()
    data_path = Path(settings.data_path)
    available_builds_list = available_builds(data_path)
    if not available_builds_list:
        raise FileNotFoundError("No SDE builds found in the data directory.")
    if build_number is None:
        build_number = max(available_builds_list)
    elif build_number not in available_builds_list:
        raise ValueError(
            f"Build number {build_number} not found. Available builds: {available_builds_list}"
        )
    build_data_dir = data_path / str(build_number)
    if not build_data_dir.exists():
        raise FileNotFoundError(
            f"SDE data for build {build_number} not found at {build_data_dir}"
        )
    return build_data_dir


def import_zipped_sde(zip_file_path: Path) -> None:
    """Import SDE data from a zipped file.

    This function will unzip the provided zip file to a temporary directory, validate the presence of the expected
    "_sde.jsonl" file, and then copy the relevant JSONL files to the appropriate location in the data directory.

    Args:
        zip_file_path: The path to the zipped SDE data file.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Unzip the file to the temporary directory
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(temp_path)
        if not (temp_path / "_sde.jsonl").exists():
            raise FileNotFoundError(
                f"_sde.jsonl file not found in the unzipped SDE data at {temp_path}. Is this a valid SDE zip file?"
            )
        import_unzipped_sde(temp_path)


def import_unzipped_sde(unzipped_path: Path) -> None:
    """Import SDE data from an unzipped directory.

    This function will validate the presence of the expected "_sde.jsonl" file in the provided directory, and then
    copy the relevant JSONL files to the appropriate location in the data directory.

    Args:
        unzipped_path: The path to the unzipped SDE data directory.
    """
    if not unzipped_path.exists() or not unzipped_path.is_dir():
        raise FileNotFoundError(
            f"Unzipped SDE data directory not found at {unzipped_path}"
        )
    if not (unzipped_path / "_sde.jsonl").exists():
        raise FileNotFoundError(
            f"_sde.jsonl file not found in the unzipped SDE data at {unzipped_path}. Is "
            "this a valid SDE data directory?"
        )
    reader = SdeReader(unzipped_path)

    if reader.build_number is None:
        raise ValueError(
            f"Build number not found in _sde.jsonl file at {unzipped_path / '_sde.jsonl'}"
        )
    build_number = reader.build_number
    initialize_build_data(build_number)
    build_data_dir = path_to_build_data_dir(build_number)
    build_sde_dir = path_to_sde(build_number)
    build_validation_dir = path_to_validation(build_number)
    build_derived_dir = path_to_derived(build_number)
    # Copy JSONL files from unzipped directory to the appropriate location in the data directory
    for file in unzipped_path.glob("*.jsonl"):
        target_file = build_sde_dir / file.name
        if target_file.exists():
            raise FileExistsError(
                f"Target file {target_file} already exists. Cannot copy {file} to {target_file}"
            )
        shutil.copy(file, target_file)
    # validate datasets, write validation results to validation directory
    validate_and_save_validation_results(SdeReader(build_sde_dir), build_validation_dir)
    # generate derived datasets, write to derived directory (not implemented here)
    generate_derived_datasets(build_sde_dir, build_derived_dir)
    logger.info(
        f"SDE data for build {build_number} successfully imported to {build_data_dir}"
    )


def generate_derived_datasets(
    sde_path: Path, dir_out: Path, localized: str = "en"
) -> None:
    """Generate derived datasets for a specific build number.

    This function will read the SDE data for the specified build number, generate the derived datasets, and save them
    to the appropriate location in the data directory.

    Args:
        sde_path: The path to the SDE data directory.
        dir_out: The directory where the derived datasets should be saved.
        localized: The localization to use for the derived datasets. Defaults to "en".
    """
    logger.info(f"Generating derived datasets for SDE data at {sde_path}")
    start = perf_counter()
    reader = SdeReader(sde_path)
    categories_dataset = LDS.CategoriesLocalizedDataset.from_sde(
        reader, localized=localized
    )
    groups_dataset = LDS.GroupsLocalizedDataset.from_sde(reader, localized=localized)
    map_regions_dataset = LDS.MapRegionsLocalizedDataset.from_sde(
        reader, localized=localized
    )
    map_solarsystem_dataset = LDS.MapSolarSystemsLocalizedDataset.from_sde(
        reader, localized=localized
    )
    market_groups_dataset = LDS.MarketGroupsLocalizedDataset.from_sde(
        reader, localized=localized
    )
    meta_groups_dataset = LDS.MetaGroupsLocalizedDataset.from_sde(
        reader, localized=localized
    )
    eve_types_dataset = LDS.EveTypesLocalizedDataset.from_sde(
        reader, localized=localized
    )

    # MarketPathsDataset
    market_paths_dataset = derived_models.MarketPathsDataset.from_dataset(
        market_groups_dataset
    )
    market_paths_dataset.save_to_disk(
        dir_out / DerivedDatasetFiles.MARKET_PATHS.localized(localized),
    )

    # NormalizedEveTypesDataset
    normalized_eve_types_dataset = (
        derived_models.NormalizedEveTypesDataset.from_datasets(
            eve_types_dataset,
            groups_dataset,
            categories_dataset,
            market_groups_dataset,
            meta_groups_dataset,
        )
    )
    normalized_eve_types_dataset.save_to_disk(
        dir_out / DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(localized),
    )

    # NormalizedEveTypesPublishedDataset
    normalized_eve_types_published_dataset = deepcopy(normalized_eve_types_dataset)
    for key, record in list(normalized_eve_types_published_dataset.data.items()):
        if not record.published:
            normalized_eve_types_published_dataset.data.pop(key)
    normalized_eve_types_published_dataset.save_to_disk(
        dir_out
        / DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(localized),
    )

    # RegionNamesDataset
    region_names_dataset = derived_models.RegionNames.from_datasets(map_regions_dataset)
    region_names_dataset.save_to_disk(
        dir_out / DerivedDatasetFiles.REGION_NAMES.localized(localized),
    )

    # SystemNamesDataset
    system_names_dataset = derived_models.SystemNames.from_datasets(
        map_solarsystem_dataset
    )
    system_names_dataset.save_to_disk(
        dir_out / DerivedDatasetFiles.SYSTEM_NAMES.localized(localized),
    )
    logger.info(
        f"Derived datasets generated and saved to {dir_out} in {perf_counter() - start:.4f} seconds"
    )
