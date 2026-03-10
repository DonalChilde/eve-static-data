"""Functions for retrieving the SDE changelog for a specific build number."""

from string import Template

from eve_static_data import USER_AGENT
from eve_static_data.helpers import app_data as AD
from eve_static_data.helpers.aiohttp.download_files import download_text


async def get_sde_data_changelog(url_template: str, build_number: int) -> str:
    """Get the SDE changelog from the configured SDE source.

    The SDE changelog is a JSONL file that contains a list of changes for a build.
    The record with key _meta contains lastBuildNumber, referring to the previous SDE.
    """
    url = Template(url_template).substitute(build_number=build_number)
    headers = {"User-Agent": USER_AGENT}
    changelog, _ = await download_text(url=url, headers=headers)
    return changelog


# async def save_sde_data_changelog(
#     url_template: str, build_number: int, file_path: Path, overwrite: bool = False
# ) -> str:
#     """Get the SDE changelog for a specific build number and save it to a JSONL file."""
#     if not overwrite and file_path.exists():
#         raise FileExistsError(
#             f"File {file_path} already exists. Set overwrite=True to overwrite."
#         )
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     changelog = await get_sde_data_changelog(url_template, build_number)
#     with open(file_path, "w") as f:
#         f.write(changelog)
#     return changelog
