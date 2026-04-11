# """Functions for downloading EVE Static Data Export (SDE) data."""

# from pathlib import Path
# from string import Template
# from typing import Any, Literal, TypedDict

# from yaml import safe_load

# from eve_static_data import USER_AGENT
# from eve_static_data.helpers.aiohttp.download_files import (
#     download_bytes_to_file,
#     download_json,
#     download_text,
# )

# SDE_URL_TEMPLATE: str = "https://developers.eveonline.com/static-data/tranquility/eve-online-static-data-${build_number}-${variant}.zip"
# DATA_CHANGES_URL_TEMPLATE: str = "https://developers.eveonline.com/static-data/tranquility/changes/${build_number}.jsonl"
# SCHEMA_CHANGELOG_URL: str = (
#     "https://developers.eveonline.com/static-data/tranquility/schema-changelog.yaml"
# )
# LATEST_INFO_URL: str = (
#     "https://developers.eveonline.com/static-data/tranquility/latest.jsonl"
# )

# # FIXME deprecate this code in favor of SDETools. Rioght now it is used by the validate functions
# # and those functions need to be refactored.


# class SdeLatestInfo(TypedDict):
#     _key: str
#     buildNumber: int
#     releaseDate: str


# async def download_sde_to_file(
#     build_number: int,
#     output_path: Path,
#     file_name: str | None = None,
#     url_template_str: str = SDE_URL_TEMPLATE,
#     variant: Literal["jsonl", "yaml"] = "jsonl",
#     overwrite: bool = False,
# ) -> Path:
#     """Download the SDE data and save it to a file.

#     Args:
#         build_number: The build number of the SDE to download.
#         output_path: The directory to save the downloaded SDE file to.
#         file_name: The name of the file to save the SDE data to. If not provided, the
#             file name will be extracted from the URL.
#         url_template_str: The URL template to download the SDE data file.
#         variant: The variant of the SDE data to download, either "jsonl" or "yaml". Defaults to "jsonl".
#         overwrite: Whether to overwrite the output file if it already exists. Defaults to False.
#     """
#     url = Template(url_template_str).substitute(
#         build_number=build_number, variant=variant
#     )
#     # get the filename from the url if not provided
#     if file_name is None:
#         file_name = url.split("/")[-1]
#     file_path = output_path / file_name
#     user_agent = USER_AGENT
#     headers = {"User-Agent": user_agent}
#     if file_path.is_dir():
#         raise IsADirectoryError(f"File path {file_path} is a directory.")
#     if file_path.is_file() and not overwrite:
#         raise FileExistsError(
#             f"File {file_path} already exists and overwrite is False."
#         )

#     _ = await download_bytes_to_file(
#         url=url, headers=headers, file_path=file_path, overwrite=overwrite
#     )
#     return file_path


# async def get_sde_data_changes(
#     build_number: int,
#     url_template: str = DATA_CHANGES_URL_TEMPLATE,
# ) -> str:
#     """Get the SDE data changes from the configured SDE source.

#     The SDE data changes is a JSONL file that contains a list of changes for a build.
#     The record with key _meta contains lastBuildNumber, referring to the previous SDE.
#     """
#     url = Template(url_template).substitute(build_number=build_number)
#     headers = {"User-Agent": USER_AGENT}
#     changes, _ = await download_text(url=url, headers=headers)
#     return changes


# async def get_sde_schema_changelog(url: str = SCHEMA_CHANGELOG_URL) -> str:
#     """Get the SDE schema changelog from the configured SDE source."""
#     headers = {"User-Agent": USER_AGENT}
#     changelog, _ = await download_text(url=url, headers=headers)
#     return changelog


# def deserialize_sde_schema_changelog(changelog_text: str) -> dict[str, Any]:
#     """Deserialize the SDE schema changelog from YAML text."""
#     return safe_load(changelog_text)


# async def current_sde_info(url: str = LATEST_INFO_URL) -> SdeLatestInfo:
#     """Get the latest SDE Build information from EVE Online."""
#     headers = {"User-Agent": USER_AGENT}
#     info_json, _ = await download_json(url=url, headers=headers)
#     return info_json
