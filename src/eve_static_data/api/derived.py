"""loaders for derived datasets."""

from eve_static_data.models.datasets.sde_dataset_files import DerivedDatasetFiles
from eve_static_data.models.derived.market_path import MarketPathsDataset
from eve_static_data.models.derived.normalized_eve_type import NormalizedEveTypesDataset
from eve_static_data.models.derived.region_names import RegionNames
from eve_static_data.models.derived.system_names import SystemNames
from eve_static_data.sde_data.available_builds import path_to_derived


def market_paths(
    build_number: int | None = None, localized: str = "en"
) -> MarketPathsDataset:
    """Get the file path for the market data derived dataset for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
        localized: The localization to use for the dataset. Defaults to "en".

    Returns:
        An instance of MarketPathsDataset for the specified build number.
    """
    derived_path = path_to_derived(build_number)
    dataset_path = derived_path / DerivedDatasetFiles.MARKET_PATHS.localized(localized)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Market paths dataset for build {build_number} not found at {dataset_path}"
        )
    return MarketPathsDataset.load_from_disk(dataset_path)


def normalized_eve_types(
    build_number: int | None = None, localized: str = "en"
) -> NormalizedEveTypesDataset:
    """Get the file path for the normalized eve types derived dataset for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
        localized: The localization to use for the dataset. Defaults to "en".

    Returns:
        An instance of NormalizedEveTypesDataset for the specified build number.
    """
    derived_path = path_to_derived(build_number)
    dataset_path = derived_path / DerivedDatasetFiles.NORMALIZED_EVE_TYPES.localized(
        localized
    )
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Normalized Eve types dataset for build {build_number} not found at {dataset_path}"
        )
    return NormalizedEveTypesDataset.load_from_disk(dataset_path)


def normalized_eve_types_published(
    build_number: int | None = None, localized: str = "en"
) -> NormalizedEveTypesDataset:
    """Get the file path for the normalized eve types published derived dataset for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
        localized: The localization to use for the dataset. Defaults to "en".

    Returns:
        An instance of NormalizedEveTypesDataset for the specified build number.
    """
    derived_path = path_to_derived(build_number)
    dataset_path = (
        derived_path
        / DerivedDatasetFiles.NORMALIZED_EVE_TYPES_PUBLISHED.localized(localized)
    )
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Normalized Eve types published dataset for build {build_number} not found at {dataset_path}"
        )
    return NormalizedEveTypesDataset.load_from_disk(dataset_path)


def region_names(build_number: int | None = None, localized: str = "en") -> RegionNames:
    """Get the file path for the region names derived dataset for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
        localized: The localization to use for the dataset. Defaults to "en".

    Returns:
        An instance of RegionNames for the specified build number.
    """
    derived_path = path_to_derived(build_number)
    dataset_path = derived_path / DerivedDatasetFiles.REGION_NAMES.localized(localized)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Region names dataset for build {build_number} not found at {dataset_path}"
        )
    return RegionNames.load_from_disk(dataset_path)


def system_names(build_number: int | None = None, localized: str = "en") -> SystemNames:
    """Get the file path for the system names derived dataset for a specific build number.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.
        localized: The localization to use for the dataset. Defaults to "en".

    Returns:
        An instance of SystemNames for the specified build number.
    """
    derived_path = path_to_derived(build_number)
    dataset_path = derived_path / DerivedDatasetFiles.SYSTEM_NAMES.localized(localized)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"System names dataset for build {build_number} not found at {dataset_path}"
        )
    return SystemNames.load_from_disk(dataset_path)
