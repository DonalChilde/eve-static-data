"""Helper functions for database operations."""

import logging
import sqlite3
from contextlib import contextmanager

logger = logging.getLogger(__name__)


@contextmanager
def transaction(conn: sqlite3.Connection):
    """Wrap a block in an explicit transaction.

    Commits on clean exit, rolls back on any exception.

    sqlite3.connect() has autocommit behaviour that changed in 3.12 and was
    further clarified in 3.14 (PEP 249-compliant isolation_level=None gives
    you a pure manual-commit mode). Using an explicit context manager here
    keeps intent clear regardless of the default.
    """
    try:
        conn.execute("BEGIN")
        yield conn
        conn.execute("COMMIT")
    except Exception as e:
        logger.error("Transaction failed. %s", e, exc_info=e)
        conn.execute("ROLLBACK")
        raise


def read_only_uri(db_path: str) -> str:
    """Construct a read-only URI for the given database path."""
    return f"file:{db_path}?mode=ro"


def read_write_uri(db_path: str) -> str:
    """Construct a read-write URI for the given database path."""
    return f"file:{db_path}?mode=rwc"


def create_read_only_connection(db_path: str) -> sqlite3.Connection:
    """Create a read-only connection to the database at the given path."""
    uri = read_only_uri(db_path)
    connection = sqlite3.connect(uri, uri=True)
    connection.row_factory = sqlite3.Row
    return connection


def create_read_write_connection(db_path: str) -> sqlite3.Connection:
    """Create a read-write connection to the database at the given path."""
    uri = read_write_uri(db_path)
    # Use the transaction context manager.
    connection = sqlite3.connect(uri, uri=True, autocommit=True)
    connection.row_factory = sqlite3.Row
    return connection
