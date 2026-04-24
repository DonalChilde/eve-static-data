# """Functions for exploring the types of data in the SDE."""

# import json
# from collections.abc import Iterable
# from pathlib import Path
# from typing import Any, TypedDict

# from eve_static_data.helpers.dict_diagnostics import (
#     RecursiveKeyInfo,
#     collect_dict_keys_and_types_recursive,
# )

# type TypeName = str
# type TypeCount = int
# type DictTypes = dict[TypeName, TypeCount]
# type DictKey = str
# type KeyInfo = dict[DictKey, DictTypes]


# class DatasetKeyInfo(TypedDict):
#     count: int
#     key_info: KeyInfo


# class DictField:
#     name: str
#     type_str: str
#     is_optional: bool


# class RecursiveKeyInfo(TypedDict):
#     dict_count: int
#     source_info: str
#     key_info: KeyInfo


# def collect_dict_keys_and_types_recursive(
#     dict_data: Iterable[tuple[dict[str, Any], int]], source_info: str
# ) -> RecursiveKeyInfo:
#     """Recursively analyze dictionaries and return all keys with their associated value types.

#     This function examines an iterable of dictionaries and recursively processes nested
#     dictionaries and lists. For each key encountered at any level, it tracks the types
#     of values associated with that key and counts their occurrences.

#     Args:
#         dict_data: An iterable of dictionaries to analyze recursively.
#         source_info: A string providing source information for the dataset.

#     Returns:
#         A dictionary where each key (from any nesting level) maps to a dictionary
#         of type names and their occurrence counts. Nested paths are represented
#         with dot notation (e.g., "parent.child.grandchild").
#     """
#     key_info: KeyInfo = {}
#     dict_count = 0

#     def process_value(key_path: str, value: object) -> None:
#         """Process a single value and update key_info recursively.

#         Args:
#             key_path: The dot-separated path to this key (e.g., "parent.child").
#             value: The value to process.
#         """
#         type_name = type(value).__name__

#         # Initialize key_path in key_info if not present
#         if key_path not in key_info:
#             key_info[key_path] = {}

#         # Initialize type_name count if not present
#         if type_name not in key_info[key_path]:
#             key_info[key_path][type_name] = 0

#         # Increment count for this type
#         key_info[key_path][type_name] += 1

#         # Recursively process nested structures
#         if isinstance(value, dict):
#             for nested_key, nested_value in value.items():  # type: ignore
#                 nested_path = f"{key_path}.{nested_key}" if key_path else nested_key  # type: ignore
#                 process_value(nested_path, nested_value)  # type: ignore
#         elif isinstance(value, list):
#             for item in value:  # type: ignore
#                 # For lists, we process each item but keep the same key_path
#                 # to indicate this is a list of items at this path
#                 if isinstance(item, (dict, list)):
#                     process_value(key_path, item)  # type: ignore

#     # Process each dictionary in the input iterable
#     for entry, line_number in dict_data:
#         _ = line_number
#         if isinstance(entry, dict):  # type: ignore
#             dict_count += 1
#             for key, value in entry.items():
#                 process_value(key, value)
#     result: RecursiveKeyInfo = {
#         "dict_count": dict_count,
#         "source_info": source_info,
#         "key_info": key_info,
#     }

#     return result


# def get_sde_type_sigs(
#     input_path: Path, build_number: str
# ) -> dict[str, RecursiveKeyInfo]:
#     """Scan the JSONL files in the sde directory and return the type signature information for each file."""
#     jsonl_files = sorted(list(input_path.glob("*.jsonl")))
#     sde_type_info: dict[str, RecursiveKeyInfo] = {}

#     def read_jsonl_dicts(file_path: Path) -> Iterable[tuple[dict[str, Any], int]]:
#         """Read a JSONL file and yield dictionaries with their line numbers."""
#         with open(file_path) as f:
#             for line_number, line in enumerate(f, start=1):
#                 yield (json.loads(line), line_number)

#     for jsonl_file in jsonl_files:
#         type_info = collect_dict_keys_and_types_recursive(
#             dict_data=read_jsonl_dicts(jsonl_file),
#             source_info=f"{jsonl_file.name} (build {build_number})",
#         )
#         sde_type_info[jsonl_file.name] = type_info
#     return sde_type_info
