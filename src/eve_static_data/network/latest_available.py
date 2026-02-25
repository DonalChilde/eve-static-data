import asyncio
import json
from pathlib import Path
from typing import TypedDict

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import download_json
from eve_static_data.settings import get_settings


class SdeLatestInfo(TypedDict):
    _key: str
    buildNumber: int
    releaseDate: str


def current_sde_info() -> SdeLatestInfo:
    """Get the latest SDE Build information from the configured SDE source."""
    settings = get_settings()
    url = settings.resolve_sde_latest_info_url()
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    info_json, _ = asyncio.run(download_json(url=url, headers=headers))
    return info_json


def save_current_sde_info(file_path: Path, overwrite: bool = False) -> SdeLatestInfo:
    """Get the latest SDE Build information and save it to a file."""
    if not overwrite and file_path.exists():
        raise FileExistsError(
            f"File {file_path} already exists. Set overwrite=True to overwrite."
        )
    file_path.parent.mkdir(parents=True, exist_ok=True)
    info = current_sde_info()
    with open(file_path, "w") as f:
        json.dump(info, f, indent=2)
    return info
