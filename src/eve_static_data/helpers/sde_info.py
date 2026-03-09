import json
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
    """
    sde_info_path = input_path / "_sde.jsonl"
    if not sde_info_path.exists():
        raise FileNotFoundError(f"_sde.jsonl file not found at {input_path}.")
    with open(sde_info_path) as f:
        first_line = f.readline()
        sde_info = json.loads(first_line)
    return SdeInfo(**sde_info)
