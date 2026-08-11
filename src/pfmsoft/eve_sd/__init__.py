"""Eve SD Package."""

from importlib.metadata import version
from typing import Any

__author__ = "Chad Lowe"
__author_email__ = "pfmsoft.dev@gmail.com"
__app_name__ = "pfmsoft-eve-sd"
__version__ = version(__app_name__)
__license__ = "MIT"
__url__ = "https://github.com/DonalChilde/pfmsoft-eve-sd"
__description__ = "A CLI and API for Eve Online Static Data downloading and use."

type Record = dict[str | int, Any]
"""Type alias for a record from an EVE SDE dataset."""
type IntKeyedRecord = tuple[int, Record]
"""Type alias for a record from an EVE SDE dataset with an integer key."""
type StrKeyedRecord = tuple[str, Record]
"""Type alias for a record from an EVE SDE dataset with a string key."""
type KeyedRecord = IntKeyedRecord | StrKeyedRecord
"""Type alias for a record from an EVE SDE dataset with either an integer or string key."""
type Dataset = dict[str | int, Record]
"""Type alias for an EVE SDE dataset, which is a mapping of keys to records."""
from pfmsoft.eve_sd.db.helpers import db_connection_manager
from pfmsoft.eve_sd.db.query import DatasetDbQuery
from pfmsoft.eve_sd.sde_tools import SDETools

__all__ = [
    "SDETools",
    "db_connection_manager",
    "DatasetDbQuery",
]
