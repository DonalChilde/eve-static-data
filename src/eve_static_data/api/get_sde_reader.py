"""reader.py - Get an SDEReader instance for a specific build number."""

from pathlib import Path

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.helpers import app_data as AD


def reader(data_path: Path, build_number: int | None = None) -> SdeReader:
    """Get an SDEReader instance for a specific build number.

    Checks the data directory for available SDE builds and returns an SDEReader for the
    specified build number. If no build number is provided, it will return an SDEReader
    for the most recent build.

    Args:
        data_path: The path to the directory containing the SDE data.
        build_number: The build number of the SDE data to read. If None, the most recent build will be used.


    Returns:
        An instance of SdeReader for the specified build number.

    Raises:
        FileNotFoundError: If the SDE data for the specified build number is not found.
        ValueError: If the specified build number is not available.
    """
    available_builds = AD.available_builds(data_path)
    if not available_builds:
        raise FileNotFoundError(
            f"No SDE data found in data directory {data_path}. Please import SDE data first."
        )
    if build_number is None:
        build_number = AD.latest_build(data_path)
    elif build_number not in available_builds:
        raise ValueError(
            f"Specified build number {build_number} is not available. Available builds: {available_builds}"
        )
    sde_path = AD.sde_dir(data_path, build_number)
    return SdeReader(sde_path)
