from pathlib import Path

from ..access.pydantic_lazy_loader import LocalizedLazyLoader
from ..access.raw_json_td import RawJsonFileAccess


def get_pydantic_lazy_loader(
    sde_dir: Path, lang: str = "en", only_published: bool = True
) -> LocalizedLazyLoader:
    raw_access = RawJsonFileAccess(sde_dir=sde_dir)
    localized_access = LocalizedLazyLoader(
        access=raw_access, lang=lang, only_published=only_published
    )
    return localized_access
