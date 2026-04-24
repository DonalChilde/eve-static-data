# """Protocols for static data classes."""

# from pathlib import Path
# from typing import Literal, Protocol

# from eve_static_data import network


# class ESDToolsProtocol(Protocol):
#     """Tools for working with EVE Online static data."""

#     async def download(
#         self,
#         build_number: int,
#         output_path: Path,
#         variant: Literal["jsonl", "yaml"] = "jsonl",
#         overwrite: bool = False,
#     ) -> Path:
#         """Download the static data.

#         Args:
#             build_number: The build number of the SDE to download.
#             output_path: The directory to save the downloaded SDE file to.
#             variant: The variant of the SDE data to download, either "jsonl" or "yaml". Defaults to "jsonl".
#             overwrite: Whether to overwrite the output file if it already exists. Defaults to False.

#         Returns:
#             The path to the downloaded SDE file.
#         """
#         ...

#     def unpack(self, input_path: Path, output_path: Path) -> tuple[Path, int]:
#         """Unpack the static data.

#         Unzip the input file and save the unpacked data to `<output_path>/<build_number>/sde/`.

#         Checks for the presence of the _sde.jsonl file in the unpacked files. If the file is not
#         found, raises a FileNotFoundError.

#         Args:
#             input_path: The path to the static data jsonl zip file.
#             output_path: The path to the directory where the unpacked data should be saved.

#         Returns:
#             A tuple containing the path to the directory where the unpacked data is saved and the build number.
#         """
#         ...

#     async def validate(
#         self, sde_path: Path, output_path: Path, overwrite: bool = False
#     ) -> None:
#         """Validate the static data.

#         Save validation results to the <output_path> directory.


#         Checks for the presence of the <input_path>/_sde.jsonl file. If the file is not
#         found, raises a ValueError.


#         Results include:
#         - validation_report.json: A JSON file containing a summary of the validation results, including the number of records validated, the number of records that passed validation, and the number of records that failed validation.
#         - validation_errors.json: A JSON file containing a list of validation errors, including the record that failed validation and the reason for the failure.
#         - validation_summary.txt: A human-readable text file summarizing the validation results.
#         - sde_data_changelog.jsonl: A JSONL file containing the sde data changelog.
#         - sde_schema_changelog.yaml: A YAML file containing the schema changelog.

#         """
#         ...

#     async def fetch_data_changes(
#         self,
#         build_number: int,
#     ) -> str:
#         """Download the sde data changes for the given build number.

#         Raises a ValueError if the changes are not available for the given build number.

#         Args:
#             build_number: The build number of the static data.

#         Returns:
#             The text of the sde data changes in JSONL format.
#         """
#         ...

#     async def fetch_schema_changelog(self, build_number: int) -> str:
#         """Download the sde schema changelog for the given build number.

#         Raises a ValueError if the changelog is not available for the given build number.

#         Args:
#             build_number: The build number of the static data.

#         Returns:
#             The text of the sde schema changelog in YAML format.
#         """
#         ...

#     async def fetch_latest_sde_info(self) -> network.SdeLatestInfo:
#         """Download the latest sde info.

#         Returns:
#             A dictionary containing the latest sde info, including the latest build number and release date.
#         """
#         ...
