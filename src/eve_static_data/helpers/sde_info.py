import json
import zipfile
from pathlib import Path
from typing import TypedDict


class SdeInfo(TypedDict):
    _key: str
    buildNumber: int
    releaseDate: str


def load_sde_info(input_path: Path) -> SdeInfo:
    """Get the SDE info from the given input path.

    The input_path usually points to a directory containing the SDE datasets for a specific
    build number, and should include a `_sde.jsonl` file with the SDE info. This function
    reads the first line of the `_sde.jsonl` file, which should contain the SDE info in
    JSON format, and returns it as an SdeInfo TypedDict.

    Example of the expected output from the `_sde.jsonl` file:
    {
        "_key": "sde",
        "buildNumber": 123456,
        "releaseDate": "2024-01-01"
    }

    Args:
        input_path: The path to the directory containing the SDE datasets and the `_sde.jsonl` file.

    Returns:
        An SdeInfo TypedDict containing the SDE info from the `_sde.jsonl` file.

    Raises:
        FileNotFoundError: If the `_sde.jsonl` file is not found at the given input path.
        json.JSONDecodeError: If the first line of the `_sde.jsonl` file is not valid JSON.
        KeyError: If the expected keys are not found in the JSON data.
    """
    sde_info_path = input_path / "_sde.jsonl"
    if not sde_info_path.exists():
        raise FileNotFoundError(f"_sde.jsonl file not found at {input_path}.")
    with open(sde_info_path) as f:
        first_line = f.readline()
        sde_info = json.loads(first_line)
    return SdeInfo(**sde_info)


def load_sde_info_from_zipfile(sde_zip_file: Path) -> SdeInfo:
    """Get the SDE info from the given SDE zip file.

    This function opens the given SDE zip file, looks for the `_sde.jsonl` file inside it,
    reads the first line of that file, which should contain the SDE info in JSON format, and
    returns it as an SdeInfo TypedDict.

    Args:
        sde_zip_file: The path to the SDE zip file.

    Returns:
        An SdeInfo TypedDict containing the SDE info from the `_sde.jsonl` file inside the zip file.

    Raises:
        FileNotFoundError: If the `_sde.jsonl` file is not found inside the zip file.
        json.JSONDecodeError: If the first line of the `_sde.jsonl` file is not valid JSON.
        KeyError: If the expected keys are not found in the JSON data.
    """
    with zipfile.ZipFile(sde_zip_file, "r") as zip_ref:
        with zip_ref.open("_sde.jsonl") as f:
            first_line = f.readline().decode("utf-8")
            sde_info = json.loads(first_line)
    return SdeInfo(**sde_info)
