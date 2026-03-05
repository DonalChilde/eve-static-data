"""Functions for exploring the types of data in the SDE."""

from pathlib import Path

from eve_static_data.helpers.dict_diagnostics import (
    RecursiveKeyInfo,
    collect_dict_keys_and_types_recursive,
)
from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts


def sde_type_info(dir_path: Path, build_number: str) -> dict[str, RecursiveKeyInfo]:
    """Load and return the SDE info as a dictionary."""
    # TODO this can be made more generic, and added to the general dict_diagnostics module
    # as a utility function for loading and analyzing dicts from jsonl files in a directory.
    jsonl_files = sorted(list(dir_path.glob("*.jsonl")))
    sde_type_info: dict[str, RecursiveKeyInfo] = {}
    for jsonl_file in jsonl_files:
        type_info = collect_dict_keys_and_types_recursive(
            dict_data=read_jsonl_dicts(jsonl_file),
            source_info=f"{jsonl_file.name} (build {build_number})",
        )
        sde_type_info[jsonl_file.name] = type_info
    return sde_type_info
