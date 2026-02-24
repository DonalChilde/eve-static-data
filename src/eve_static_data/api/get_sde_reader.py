"""reader.py - Get an SDEReader instance for a specific build number."""

from pathlib import Path

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
    sde_path = _path_to_sde(build_number)
    return SdeReader(sde_path)


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


def _path_to_sde(build_number: int | None = None) -> Path:
    """Get the path to the SDE.

    If a build number is provided, the path will be constructed using the build number,
    otherwise it will be the most recent build.
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
    sde_path = data_path / str(build_number)
    if not sde_path.exists():
        raise FileNotFoundError(
            f"SDE data for build {build_number} not found at {sde_path}"
        )
    return sde_path
