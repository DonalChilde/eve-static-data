"""reader.py - Get an SDEReader instance for a specific build number."""

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.sde_data import path_to_sde


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
    sde_path = path_to_sde(build_number)
    return SdeReader(sde_path)
