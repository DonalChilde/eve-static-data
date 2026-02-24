import asyncio

from eve_static_data import USER_AGENT
from eve_static_data.helpers.simple_download_async import download_text
from eve_static_data.settings import get_settings


def get_sde_data_changelog(build_number: int) -> str:
    """Get the SDE changelog from the configured SDE source.

    The SDE changelog is a JSONL file that contains a list of changes for each build.
    The record with key _meta contains lastBuildNumber, referring to the previous SDE.
    """
    settings = get_settings()
    url = settings.resolve_sde_changes_url(build_number=build_number)
    user_agent = USER_AGENT
    headers = {"User-Agent": user_agent} if user_agent else None
    changelog, _ = asyncio.run(download_text(url=url, headers=headers))
    return changelog
