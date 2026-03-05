"""Functions for retrieving information about the latest available EVE Static Data Export (SDE) build."""

import json
from pathlib import Path
from typing import TypedDict

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import download_json


class SdeLatestInfo(TypedDict):
    _key: str
    buildNumber: int
    releaseDate: str


async def current_sde_info(url: str) -> SdeLatestInfo:
    """Get the latest SDE Build information from the configured SDE source."""
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    info_json, _ = await download_json(url=url, headers=headers)
    return info_json


async def save_current_sde_info(
    url: str, file_path: Path, overwrite: bool = False
) -> SdeLatestInfo:
    """Get the latest SDE Build information and save it to a file."""
    if not overwrite and file_path.exists():
        raise FileExistsError(
            f"File {file_path} already exists. Set overwrite=True to overwrite."
        )
    file_path.parent.mkdir(parents=True, exist_ok=True)
    info = await current_sde_info(url)
    with open(file_path, "w") as f:
        json.dump(info, f, indent=2)
    return info
