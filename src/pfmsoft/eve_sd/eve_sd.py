"""Eve-SD public api."""

from pathlib import Path
from sqlite3 import Connection
from types import TracebackType
from typing import Self

from pfmsoft.eve_snippets.sqlite3.connection_helpers import db_connection_manager

from pfmsoft.eve_sd.db.query import DatasetDbQuery
from pfmsoft.eve_sd.protocols import DatasetDbQueryProtocol


class EveSdDbQueryManager:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path
        self._connection: Connection | None = None
        self._connection_cm = None
        self._query: DatasetDbQueryProtocol | None = None

    def __enter__(self) -> Self:
        # Enter the database connection context manager and store the connection.
        self._connection_cm = db_connection_manager(self.database_path)
        self._connection = self._connection_cm.__enter__()
        self._query = DatasetDbQuery(self._connection)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        # Exit the database connection context manager if it was created.
        self._query = None
        if self._connection_cm is not None:
            self._connection_cm.__exit__(exc_type, exc_value, traceback)
            self._connection_cm = None
        self._connection = None

    @property
    def query(self) -> DatasetDbQueryProtocol:
        """Return the database query object."""
        if self._query is None:
            raise RuntimeError(
                "Database query is not available. Ensure you are using the context manager."
            )
        return self._query
