"""Eve SD Package."""

from importlib.metadata import version

from pfmsoft.eve_sd.eve_sd import EveSdDbQueryManager

__author__ = "Chad Lowe"
__author_email__ = "pfmsoft.dev@gmail.com"
__app_name__ = "pfmsoft-eve-sd"
__version__ = version(__app_name__)
__license__ = "MIT"
__url__ = "https://github.com/DonalChilde/pfmsoft-eve-sd"
__description__ = "A CLI and API for Eve Online Static Data downloading and use."

from pfmsoft.eve_sd.sde_tools import SDETools

__all__ = [
    "EveSdDbQueryManager",
    "SDETools",
]
