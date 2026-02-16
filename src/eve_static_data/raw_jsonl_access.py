# """Access the SDE stored as raw JSONL files."""

# from collections.abc import Iterable
# from pathlib import Path
# from typing import Any

# from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts

# from .sde_access_protocol import SdeAccessProtocol, SdeFileNames


# class RawJsonFileAccess(SdeAccessProtocol):
#     def __init__(self, sde_directory: Path) -> None:
#         """Initialize the RawJsonAccess with the SDE directory."""
#         self.sde_directory = sde_directory
#         _sde_path = self.sde_directory / SdeFileNames.SDE_INFO
#         if not _sde_path.exists():
#             raise FileNotFoundError(f"SDE info file not found at {_sde_path}")

#     def jsonl_iter(self, sde_file: SdeFileNames) -> Iterable[dict[str, Any]]:
#         """Get an iterator over the JSON objects in a JSONL SDE file.

#         Args:
#             sde_file: The SDE file to read.

#         Returns:
#             An iterator over the JSON objects in the file.
#         """
#         file_path = self.sde_directory / sde_file
#         if not file_path.exists():
#             raise FileNotFoundError(f"SDE file not found at {file_path}")
#         return read_jsonl_dicts(file_path)

#     def sde_info(self) -> dict[str, str | int]:
#         """Get the SDE info as a dictionary."""
#         info = next(iter(self.jsonl_iter(SdeFileNames.SDE_INFO)))
#         return info
