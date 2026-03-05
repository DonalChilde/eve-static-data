"""Functions for retrieving the SDE schema changelog."""

from typing import Any

from yaml import safe_load

from eve_static_data import USER_AGENT
from eve_static_data.helpers.aiohttp.download_files import download_text


async def get_sde_schema_changelog(url: str) -> dict[str, Any]:
    """Get the SDE schema changelog from the configured SDE source."""
    headers = {"User-Agent": USER_AGENT}
    changelog, _ = await download_text(url=url, headers=headers)
    return safe_load(changelog)


# async def save_sde_schema_changelog(
#     url: str, file_path: Path, overwrite: bool = False
# ) -> dict[str, Any]:
#     """Get the SDE schema changelog and save it to a YAML file."""
#     if not overwrite and file_path.exists():
#         raise FileExistsError(
#             f"File {file_path} already exists. Set overwrite=True to overwrite."
#         )
#     file_path.parent.mkdir(parents=True, exist_ok=True)
#     changelog = await get_sde_schema_changelog(url)
#     with open(file_path, "w") as f:
#         f.write(safe_dump(changelog))
#     return changelog
