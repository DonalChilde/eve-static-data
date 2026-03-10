"""Functions for downloading EVE Static Data Export (SDE) data."""

from pathlib import Path
from typing import Literal

from eve_static_data import USER_AGENT
from eve_static_data.helpers import app_data as AD
from eve_static_data.helpers.aiohttp.download_files import download_bytes_to_file


async def download_sde_to_file(
    url_template_str: str,
    build_number: int,
    variant: Literal["jsonl", "yaml"],
    output_path: Path,
    overwrite: bool = False,
) -> None:
    """Download the SDE data and save it to a file."""
    url = AD.sde_download_url(
        url_template_str=url_template_str, build_number=build_number, variant=variant
    )
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    if output_path.exists() and not overwrite:
        raise FileExistsError(
            f"File {output_path} already exists and overwrite is False."
        )

    await download_bytes_to_file(
        url=url, headers=headers, file_path=output_path, overwrite=overwrite
    )
