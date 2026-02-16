"""Helper functions for downloading SDE raw data and changelog information."""

import asyncio
from pathlib import Path
from typing import Any, TypedDict

from yaml import safe_load

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import (
    download_file,
    download_json,
    download_text,
)
from eve_static_data.settings import get_settings


class SdeLatestInfo(TypedDict):
    _key: str
    buildNumber: int
    releaseDate: str


# TODO how to handle exceptions in the async download calls.


def get_sde_latest_info() -> SdeLatestInfo:
    """Get the latest SDE Build information from the configured SDE source."""
    settings = get_settings()
    url = settings.resolve_sde_latest_info_url()
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    info, _ = asyncio.run(download_json(url=url, headers=headers))
    return info


def get_sde_changelog() -> dict[str, Any]:
    """Get the SDE changelog from the configured SDE source."""
    settings = get_settings()
    url = settings.resolve_sde_changelog_url()
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    changelog, _ = asyncio.run(download_text(url=url, headers=headers))
    return safe_load(changelog)


def download_sde_to_file(
    build_number: int, variant: str, output_path: Path, overwrite: bool = False
) -> None:
    """Download the SDE data and save it to a file."""
    settings = get_settings()
    url = settings.resolve_sde_download_url(build_number=build_number, variant=variant)
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    headers = asyncio.run(
        download_file(
            url=url, headers=headers, file_path=output_path, overwrite=overwrite
        )
    )
    _ = headers
