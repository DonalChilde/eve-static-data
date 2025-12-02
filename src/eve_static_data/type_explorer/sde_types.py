from pathlib import Path

from eve_static_data.helpers.dict_diagnostics import (
    RecursiveKeyInfo,
    collect_dict_keys_and_types_recursive,
)
from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts


def sde_type_info(dir_path: Path, build_number: str) -> dict[str, RecursiveKeyInfo]:
    """Load and return the SDE info as a dictionary."""
    jsonl_files = dir_path.glob("*.jsonl")
    sde_type_info: dict[str, RecursiveKeyInfo] = {}
    for jsonl_file in jsonl_files:
        dicts = read_jsonl_dicts(jsonl_file)
        type_info = collect_dict_keys_and_types_recursive(
            dicts, source_info=f"{jsonl_file.name} (build {build_number})"
        )
        sde_type_info[jsonl_file.name] = type_info
    return sde_type_info
