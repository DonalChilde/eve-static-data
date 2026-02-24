import asyncio
from pathlib import Path
from typing import Literal

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import download_file
from eve_static_data.settings import get_settings


def download_sde_to_file(
    build_number: int,
    variant: Literal["jsonl", "yaml"],
    output_path: Path,
    overwrite: bool = False,
) -> None:
    """Download the SDE data and save it to a file."""
    settings = get_settings()
    url = settings.resolve_sde_download_url(build_number=build_number, variant=variant)
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"File {output_path} already exists and overwrite is False."
        )
    headers = asyncio.run(
        download_file(
            url=url, headers=headers, file_path=output_path, overwrite=overwrite
        )
    )
    _ = headers
