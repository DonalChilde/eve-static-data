from pathlib import Path
from sqlite3 import Connection
from types import TracebackType
from typing import Self

from pfmsoft.eve_snippets.sqlite3.connection_helpers import db_connection_manager

from pfmsoft.eve_sd.db.query import DatasetDbQuery


class EveSdDbQueryManager:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self._connection: Connection | None = None

    def __enter__(self) -> Self:
        # Enter the database connection context manager and store the connection.
        self._connection = db_connection_manager(self.database_path).__enter__()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        # Exit the database connection context manager if it was created.
        if self._connection is not None:
            self._connection.__exit__(exc_type, exc_value, traceback)
