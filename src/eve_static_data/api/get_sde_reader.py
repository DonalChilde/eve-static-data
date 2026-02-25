"""reader.py - Get an SDEReader instance for a specific build number."""

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.settings import get_settings


def reader(build_number: int | None = None) -> SdeReader:
    """Get an SDEReader instance for a specific build number.

    Checks the data directory for available SDE builds and returns an SDEReader for the
    specified build number. If no build number is provided, it will return an SDEReader
    for the most recent build.

    Args:
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.

    Returns:
        An instance of SdeReader for the specified build number.

    Raises:
        FileNotFoundError: If the SDE data for the specified build number is not found.
        ValueError: If the specified build number is not available.
    """
    settings = get_settings()
    available_builds = settings.available_builds()
    if not available_builds:
        raise FileNotFoundError(
            f"No SDE data found in data directory {settings.data_path}. Please import SDE data first."
        )
    if build_number is None:
        build_number = settings.latest_build()
    elif build_number not in available_builds:
        raise ValueError(
            f"Specified build number {build_number} is not available. Available builds: {available_builds}"
        )
    sde_path = settings.build_data_sde_dir(build_number)
    return SdeReader(sde_path)
