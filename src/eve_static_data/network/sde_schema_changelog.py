import asyncio
from pathlib import Path
from typing import Any

from yaml import safe_dump, safe_load

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import download_text
from eve_static_data.settings import get_settings


def get_sde_schema_changelog() -> dict[str, Any]:
    """Get the SDE schema changelog from the configured SDE source."""
    settings = get_settings()
    url = settings.resolve_sde_schema_changelog_url()
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    changelog, _ = asyncio.run(download_text(url=url, headers=headers))
    return safe_load(changelog)


def save_sde_schema_changelog(
    file_path: Path, overwrite: bool = False
) -> dict[str, Any]:
    """Get the SDE schema changelog and save it to a YAML file."""
    if not overwrite and file_path.exists():
        raise FileExistsError(
            f"File {file_path} already exists. Set overwrite=True to overwrite."
        )
    file_path.parent.mkdir(parents=True, exist_ok=True)
    changelog = get_sde_schema_changelog()
    with open(file_path, "w") as f:
        f.write(safe_dump(changelog))
    return changelog
