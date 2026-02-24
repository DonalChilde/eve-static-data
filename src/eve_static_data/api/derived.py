"""loaders for derived datasets."""

from eve_static_data.models.datasets.sde_dataset_files import DerivedDatasetFiles
from eve_static_data.models.derived.market_path import MarketPathsDataset
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
