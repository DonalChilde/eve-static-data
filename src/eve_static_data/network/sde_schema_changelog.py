import asyncio
from typing import Any

from yaml import safe_load

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
