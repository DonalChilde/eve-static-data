"""Tests for eve_sd — the public API context manager and query interface."""

import sqlite3
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pytest

from pfmsoft.eve_sd.eve_sd import EveSdDbQueryManager
from pfmsoft.eve_sd.protocols import DatasetDbQueryProtocol


class TestEveSdDbQueryManagerInitialization:
    """Tests for EveSdDbQueryManager initialization."""

    def test_init_stores_database_path(self, tmp_path: Path) -> None:
        """Initialization stores the database path without opening it."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)
        assert manager.database_path == db_path

    def test_init_connection_is_none(self, tmp_path: Path) -> None:
        """Initialization leaves _connection as None."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)
        assert manager._connection is None

    def test_init_query_is_none(self, tmp_path: Path) -> None:
        """Initialization leaves _query as None."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)
        assert manager._query is None


class TestEveSdDbQueryManagerContextManager:
    """Tests for EveSdDbQueryManager context manager protocol."""

    def test_enter_returns_self(self, tmp_path: Path) -> None:
        """__enter__ returns self for use in with statement."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            result = manager.__enter__()

            assert result is manager

    def test_enter_opens_connection(self, tmp_path: Path) -> None:
        """__enter__ calls db_connection_manager and stores the connection."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            manager.__enter__()

            mock_cm.assert_called_once_with(db_path)
            assert manager._connection is mock_conn

    def test_enter_creates_query_object(self, tmp_path: Path) -> None:
        """__enter__ creates a DatasetDbQuery with the connection."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query_obj = MagicMock(spec=DatasetDbQueryProtocol)
            mock_query.return_value = mock_query_obj

            manager.__enter__()

            mock_query.assert_called_once_with(mock_conn)
            assert manager._query is mock_query_obj

    def test_exit_clears_query(self, tmp_path: Path) -> None:
        """__exit__ sets _query to None."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            manager.__enter__()
            manager.__exit__(None, None, None)

            assert manager._query is None

    def test_exit_calls_connection_exit(self, tmp_path: Path) -> None:
        """__exit__ calls __exit__ on the underlying connection."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            manager.__enter__()
            manager.__exit__(None, None, None)

            mock_conn.__exit__.assert_called_once_with(None, None, None)

    def test_exit_clears_connection(self, tmp_path: Path) -> None:
        """__exit__ sets _connection to None after exiting."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            manager.__enter__()
            manager.__exit__(None, None, None)

            assert manager._connection is None

    def test_exit_with_exception_info(self, tmp_path: Path) -> None:
        """__exit__ passes exception info to connection.__exit__."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)
        test_exception = ValueError("test error")
        exc_type = type(test_exception)

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            manager.__enter__()
            manager.__exit__(exc_type, test_exception, None)

            mock_conn.__exit__.assert_called_once_with(exc_type, test_exception, None)

    def test_context_manager_with_statement(self, tmp_path: Path) -> None:
        """The manager works correctly in a with statement."""
        db_path = tmp_path / "test.db"

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query_obj = MagicMock(spec=DatasetDbQueryProtocol)
            mock_query.return_value = mock_query_obj

            with EveSdDbQueryManager(db_path) as manager:
                assert manager._connection is mock_conn
                assert manager._query is mock_query_obj

            # After exiting, resources should be cleared
            assert manager._connection is None
            assert manager._query is None


class TestEveSdDbQueryManagerQueryProperty:
    """Tests for EveSdDbQueryManager.query property."""

    def test_query_property_returns_query_object(self, tmp_path: Path) -> None:
        """The query property returns the stored query object."""
        db_path = tmp_path / "test.db"

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query_obj = MagicMock(spec=DatasetDbQueryProtocol)
            mock_query.return_value = mock_query_obj

            with EveSdDbQueryManager(db_path) as manager:
                assert manager.query is mock_query_obj

    def test_query_property_raises_outside_context(self, tmp_path: Path) -> None:
        """Accessing query outside context manager raises RuntimeError."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        with pytest.raises(
            RuntimeError,
            match="Database query is not available. Ensure you are using the context manager.",
        ):
            _ = manager.query

    def test_query_property_raises_after_context_exit(self, tmp_path: Path) -> None:
        """Accessing query after context exit raises RuntimeError."""
        db_path = tmp_path / "test.db"

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            with EveSdDbQueryManager(db_path) as manager:
                pass  # Exit the context

            # Now try to access query property
            with pytest.raises(
                RuntimeError,
                match="Database query is not available. Ensure you are using the context manager.",
            ):
                _ = manager.query


class TestEveSdDbQueryManagerErrorHandling:
    """Tests for error handling and edge cases."""

    def test_multiple_enters_reinitializes(self, tmp_path: Path) -> None:
        """Multiple __enter__ calls reinitialize connection and query."""
        db_path = tmp_path / "test.db"

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn1 = MagicMock(spec=sqlite3.Connection)
            mock_conn2 = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.side_effect = [mock_conn1, mock_conn2]
            mock_query_obj1 = MagicMock(spec=DatasetDbQueryProtocol)
            mock_query_obj2 = MagicMock(spec=DatasetDbQueryProtocol)
            mock_query.side_effect = [mock_query_obj1, mock_query_obj2]

            manager = EveSdDbQueryManager(db_path)

            manager.__enter__()
            first_query = manager._query
            manager.__exit__(None, None, None)

            manager.__enter__()
            second_query = manager._query
            manager.__exit__(None, None, None)

            assert first_query is mock_query_obj1
            assert second_query is mock_query_obj2
            assert first_query is not second_query

    def test_exit_without_enter_does_not_crash(self, tmp_path: Path) -> None:
        """Calling __exit__ without __enter__ does not crash."""
        db_path = tmp_path / "test.db"
        manager = EveSdDbQueryManager(db_path)

        # Should not raise, connection is None so __exit__ just returns
        manager.__exit__(None, None, None)
        assert manager._connection is None

    def test_context_manager_returns_correct_type(self, tmp_path: Path) -> None:
        """Context manager __enter__ returns the correct type."""
        db_path = tmp_path / "test.db"

        with (
            patch("pfmsoft.eve_sd.eve_sd.db_connection_manager") as mock_cm,
            patch("pfmsoft.eve_sd.eve_sd.DatasetDbQuery") as mock_query,
        ):
            mock_conn = MagicMock(spec=sqlite3.Connection)
            mock_cm.return_value.__enter__.return_value = mock_conn
            mock_query.return_value = MagicMock(spec=DatasetDbQueryProtocol)

            with EveSdDbQueryManager(db_path) as manager:
                assert isinstance(manager, EveSdDbQueryManager)
