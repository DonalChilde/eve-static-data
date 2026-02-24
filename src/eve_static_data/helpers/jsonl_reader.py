"""Helper function to read JSONL files."""

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any


def read_jsonl_dicts(
    file_path: Path, encoding: str = "utf-8"
) -> Iterable[tuple[dict[str, Any], int]]:
    """Read a JSONL file and yield each line as a JSON object.

    Args:
        file_path (Path): The path to the JSONL file.
        encoding (str): The file encoding. Default is 'utf-8'.

    Yields:
        tuple[dict[str, Any], int]: A tuple containing the JSON object from each line of the file and its line number.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        JSONDecodeError: If a line in the file is not valid JSON.
    """
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    with file_path.open("r", encoding=encoding) as f:
        for index, line in enumerate(f, start=1):
            yield json.loads(line), index
