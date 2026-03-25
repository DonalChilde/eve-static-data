"""Eve Static Data Package."""

from pathlib import Path

from typer import get_app_dir

from eve_static_data.esd_loader import ESDLoader
from eve_static_data.esd_tools import EsdTools

__author__ = "Chad Lowe"
__author_email__ = "pfmsoft.dev@gmail.com"
__app_name__ = "Eve Static Data"
__version__ = "0.2.1"
__license__ = "MIT"
__url__ = "https://github.com/DonalChilde/eve-static-data"
__description__ = "A terminal interface for Eve Online Static Data downloading and use."

NAMESPACE = "pfmsoft"
APPLICATION_NAME = "esi-static-data"
DEFAULT_APP_DIR = Path(get_app_dir(f"{NAMESPACE}-{APPLICATION_NAME}"))
USER_AGENT = f"{__app_name__}/{__version__} (+{__url__})"
AFTER_BUILD_NUMBER: int = 0
RELEASE_DATE: str = "Set Me"


__all__ = [
    "ESDLoader",
    "EsdTools",
]
