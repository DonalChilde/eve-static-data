"""SQLite helper functions for eve-sd persistence.

This module centralizes low-level database operations, including connection
creation, schema bootstrap, record writes, and query helpers for both integer
and string-keyed datasets.
"""

import logging
import sqlite3
from collections.abc import Iterable
from contextlib import contextmanager
from typing import Any
from uuid import uuid4
from warnings import deprecated

from pfmsoft.eve_sd.db import models as db_models
from pfmsoft.eve_sd.helpers.package_resource import load_package_resource_text
from pfmsoft.eve_sd.helpers.sde_metadata import SdeMetadata, SdeVariant, SourceMedia

logger = logging.getLogger(__name__)

_table_def_parent = "pfmsoft.eve_sd.db"
_table_def_sql = "table_defs.sql"

INLINE_FILTER_LIMIT = 500
"""Threshold for choosing inline IN filtering vs temporary-table joins.

When a key filter has fewer than this many items, query helpers use an inline
``IN (...)`` clause. For larger sets, helpers create a temporary key table and
join against it to avoid very large SQL statements.
"""


def load_table_definitions() -> str:
    """Load the packaged SQL script for creating the database schema.

    Returns:
        The contents of the SQL script as a string.
    """
    return load_package_resource_text(_table_def_parent, _table_def_sql)


def write_int_records(
    connection: sqlite3.Connection,
    *,
    records: Iterable[db_models.DatasetRecordIntBase],
) -> None:
    """Write integer-keyed records into ``DatasetRecordsInt``.

    Args:
        connection: Open SQLite database connection.
        records: Iterable of integer-keyed database record models.
    """
    with connection:
        connection.executemany(
            """
                INSERT INTO DatasetRecordsInt (record_key, dataset_name, record_bytes)
                VALUES (?, ?, ?)
                ON CONFLICT(record_key, dataset_name) DO UPDATE SET record_bytes=excluded.record_bytes
                """,
            (
                (record.record_key, record.dataset_name, record.record)
                for record in records
            ),
        )


def write_str_records(
    connection: sqlite3.Connection,
    *,
    records: Iterable[db_models.DatasetRecordStrBase],
) -> None:
    """Write string-keyed records into ``DatasetRecordsStr``.

    Args:
        connection: Open SQLite database connection.
        records: Iterable of string-keyed database record models.
    """
    with connection:
        connection.executemany(
            """
                INSERT INTO DatasetRecordsStr (record_key, dataset_name, record_bytes)
                VALUES (?, ?, ?)
                ON CONFLICT(record_key, dataset_name) DO UPDATE SET record_bytes=excluded.record_bytes
                """,
            (
                (record.record_key, record.dataset_name, record.record)
                for record in records
            ),
        )


def write_key_type(
    connection: sqlite3.Connection,
    *,
    dataset_name: str,
    key_type: str,
) -> None:
    """Write or update a dataset key type.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset table/logical name.
        key_type: Key type label, either ``"int"`` or ``"str"``.

    Raises:
        ValueError: If ``key_type`` is not supported.
    """
    if key_type not in ("int", "str"):
        raise ValueError("key_type must be either 'int' or 'str'.")
    with connection:
        connection.execute(
            """
                INSERT INTO DatasetKeyType (dataset_name, key_type)
                VALUES (?, ?)
                ON CONFLICT(dataset_name) DO UPDATE SET key_type=excluded.key_type
                """,
            (dataset_name, key_type),
        )


def write_key_types(
    connection: sqlite3.Connection,
    *,
    dataset_key_types: dict[str, str],
) -> None:
    """Write or update key types for multiple datasets.

    Args:
        connection: Open SQLite database connection.
        dataset_key_types: Mapping of dataset name to key type.
    """
    with connection:
        connection.executemany(
            """
                INSERT INTO DatasetKeyType (dataset_name, key_type)
                VALUES (?, ?)
                ON CONFLICT(dataset_name) DO UPDATE SET key_type=excluded.key_type
                """,
            (
                (dataset_name, key_type)
                for dataset_name, key_type in dataset_key_types.items()
            ),
        )


def write_serialization_format(
    connection: sqlite3.Connection,
    *,
    serialization_format: db_models.SerializationFormat,
) -> None:
    """Write the active serialization format to ``DatabaseSettings``.

    Args:
        connection: Open SQLite database connection.
        serialization_format: Record serialization format used by this database.
    """
    with connection:
        connection.execute(
            """
                INSERT INTO DatabaseSettings (row_id, serialization_format)
                VALUES (1, ?)
                ON CONFLICT(row_id) DO UPDATE SET serialization_format=excluded.serialization_format
                """,
            (serialization_format.value,),
        )


def query_key_types(connection: sqlite3.Connection) -> dict[str, str]:
    """Read key types for all datasets.

    Args:
        connection: Open SQLite database connection.

    Returns:
        Mapping of dataset name to key type.
    """
    with connection:
        cursor = connection.execute("SELECT dataset_name, key_type FROM DatasetKeyType")
        return {row["dataset_name"]: row["key_type"] for row in cursor}


# Note: this currently returns a plain mapping; a typed settings model may be
# introduced in a future refactor.
def query_database_settings(connection: sqlite3.Connection) -> dict[str, Any]:
    """Read persisted database settings.

    Args:
        connection: Open SQLite database connection.

    Returns:
        Settings mapping, currently containing ``serialization_format`` when set.
    """
    with connection:
        cursor = connection.execute(
            "SELECT serialization_format FROM DatabaseSettings WHERE row_id = 1"
        )
        row = cursor.fetchone()
        if row is None:
            return {}
        return {"serialization_format": row["serialization_format"]}


def query_int_keys(connection: sqlite3.Connection, *, dataset_name: str) -> set[int]:
    """Read all integer record keys for one dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.

    Returns:
        Set of integer keys present for the dataset.
    """
    with connection:
        cursor = connection.execute(
            """
                SELECT record_key
                FROM DatasetRecordsInt
                WHERE dataset_name = ?
                """,
            (dataset_name,),
        )
        return {row["record_key"] for row in cursor}


def query_str_keys(connection: sqlite3.Connection, *, dataset_name: str) -> set[str]:
    """Read all string record keys for one dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.

    Returns:
        Set of string keys present for the dataset.
    """
    with connection:
        cursor = connection.execute(
            """
                SELECT record_key
                FROM DatasetRecordsStr
                WHERE dataset_name = ?
                """,
            (dataset_name,),
        )
        return {row["record_key"] for row in cursor}


def query_dataset_record_count(
    connection: sqlite3.Connection, *, dataset_name: str, key_type: str
) -> int:
    """Read record count for a dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to count.
        key_type: Dataset key type, either ``"int"`` or ``"str"``.

    Returns:
        Number of records for the dataset.

    Raises:
        ValueError: If ``key_type`` is not supported.
    """
    match key_type:
        case "int":
            table_name = "DatasetRecordsInt"
        case "str":
            table_name = "DatasetRecordsStr"
        case _:
            raise ValueError(f"Unsupported key type: {key_type}")
    with connection:
        cursor = connection.execute(
            f"""
                SELECT COUNT(*) AS record_count
                FROM {table_name}
                WHERE dataset_name = ?
                """,
            (dataset_name,),
        )
        row = cursor.fetchone()
        if row is None:
            return 0
        return int(row["record_count"])


def query_int_records(
    connection: sqlite3.Connection,
    *,
    dataset_name: str,
    serialization_format: db_models.SerializationFormat,
    record_keys: set[int] | None = None,
) -> Iterable[db_models.DatasetRecordIntBase]:
    """Yield integer-keyed records for a dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.
        serialization_format: Serialization format of stored record bytes.
        record_keys: Optional key filter. When provided, only matching keys are
            returned.

    Yields:
        Integer-keyed record model instances.

    Notes:
        For small key filters, this uses an inline ``IN`` clause. For larger
        filters, it creates a temporary table and performs a join.

    Raises:
        ValueError: If ``serialization_format`` is not supported.
    """
    match serialization_format:
        case db_models.SerializationFormat.YAML:
            record_class = db_models.DatasetRecordIntYaml
        case db_models.SerializationFormat.JSON:
            record_class = db_models.DatasetRecordIntJson
        case db_models.SerializationFormat.PICKLE:
            record_class = db_models.DatasetRecordIntPickle
        case _:
            raise ValueError(
                f"Unsupported serialization format: {serialization_format}. Must be one of 'yaml', 'json', or 'pickle'."
            )
    if record_keys is None:
        with connection:
            cursor = connection.execute(
                """
                    SELECT record_key, dataset_name, record_bytes
                    FROM DatasetRecordsInt
                    WHERE dataset_name = ?
                    """,
                (dataset_name,),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
    elif len(record_keys) < INLINE_FILTER_LIMIT:
        with connection:
            cursor = connection.execute(
                f"""
                    SELECT record_key, dataset_name, record_bytes
                    FROM DatasetRecordsInt
                    WHERE dataset_name = ?
                    AND record_key IN ({",".join("?" for _ in record_keys)})
                    """,
                (dataset_name, *record_keys),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
    else:
        table_name = f"temp_keys_{uuid4().hex}"
        with connection:
            connection.execute(
                f"""
                    CREATE TEMPORARY TABLE {table_name} (
                        record_key INTEGER PRIMARY KEY
                    )
                    """,
            )
            connection.executemany(
                f"""
                    INSERT INTO {table_name} (record_key) VALUES (?)
                    """,
                ((key,) for key in record_keys),
            )
            cursor = connection.execute(
                f"""
                    SELECT r.record_key, r.dataset_name, r.record_bytes
                    FROM DatasetRecordsInt r
                    JOIN {table_name} k ON r.record_key = k.record_key
                    WHERE r.dataset_name = ?
                    """,
                (dataset_name,),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
            connection.execute(f"DROP TABLE {table_name}")


def query_int_records_page(
    connection: sqlite3.Connection,
    *,
    dataset_name: str,
    serialization_format: db_models.SerializationFormat,
    limit: int,
    offset: int,
) -> Iterable[db_models.DatasetRecordIntBase]:
    """Yield one page of integer-keyed records for a dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.
        serialization_format: Serialization format of stored record bytes.
        limit: Maximum number of records to return.
        offset: Starting offset for pagination.

    Yields:
        Integer-keyed record model instances.

    Raises:
        ValueError: If ``serialization_format`` is not supported.
    """
    match serialization_format:
        case db_models.SerializationFormat.YAML:
            record_class = db_models.DatasetRecordIntYaml
        case db_models.SerializationFormat.JSON:
            record_class = db_models.DatasetRecordIntJson
        case db_models.SerializationFormat.PICKLE:
            record_class = db_models.DatasetRecordIntPickle
        case _:
            raise ValueError(
                f"Unsupported serialization format: {serialization_format}. Must be one of 'yaml', 'json', or 'pickle'."
            )
    with connection:
        cursor = connection.execute(
            """
                SELECT record_key, dataset_name, record_bytes
                FROM DatasetRecordsInt
                WHERE dataset_name = ?
                ORDER BY record_key
                LIMIT ?
                OFFSET ?
                """,
            (dataset_name, limit, offset),
        )
        for row in cursor:
            yield record_class(
                record_key=row["record_key"],
                dataset_name=row["dataset_name"],
                record=row["record_bytes"],
            )


def query_str_records(
    connection: sqlite3.Connection,
    *,
    dataset_name: str,
    serialization_format: db_models.SerializationFormat,
    record_keys: set[str] | None = None,
) -> Iterable[db_models.DatasetRecordStrBase]:
    """Yield string-keyed records for a dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.
        serialization_format: Serialization format of stored record bytes.
        record_keys: Optional key filter. When provided, only matching keys are
            returned.

    Yields:
        String-keyed record model instances.

    Notes:
        For small key filters, this uses an inline ``IN`` clause. For larger
        filters, it creates a temporary table and performs a join.

    Raises:
        ValueError: If ``serialization_format`` is not supported.
    """
    match serialization_format:
        case db_models.SerializationFormat.YAML:
            record_class = db_models.DatasetRecordStrYaml
        case db_models.SerializationFormat.JSON:
            record_class = db_models.DatasetRecordStrJson
        case db_models.SerializationFormat.PICKLE:
            record_class = db_models.DatasetRecordStrPickle
        case _:
            raise ValueError(
                f"Unsupported serialization format: {serialization_format}. Must be one of 'yaml', 'json', or 'pickle'."
            )
    if record_keys is None:
        with connection:
            cursor = connection.execute(
                """
                    SELECT record_key, dataset_name, record_bytes
                    FROM DatasetRecordsStr
                    WHERE dataset_name = ?
                    """,
                (dataset_name,),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
    elif len(record_keys) < INLINE_FILTER_LIMIT:
        with connection:
            cursor = connection.execute(
                f"""
                    SELECT record_key, dataset_name, record_bytes
                    FROM DatasetRecordsStr
                    WHERE dataset_name = ?
                    AND record_key IN ({",".join("?" for _ in record_keys)})
                    """,
                (dataset_name, *record_keys),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
    else:
        table_name = f"temp_keys_{uuid4().hex}"
        with connection:
            connection.execute(
                f"""
                    CREATE TEMPORARY TABLE {table_name} (
                        record_key TEXT PRIMARY KEY
                    )
                    """,
            )
            connection.executemany(
                f"""
                    INSERT INTO {table_name} (record_key) VALUES (?)
                    """,
                ((key,) for key in record_keys),
            )
            cursor = connection.execute(
                f"""
                    SELECT r.record_key, r.dataset_name, r.record_bytes
                    FROM DatasetRecordsStr r
                    JOIN {table_name} k ON r.record_key = k.record_key
                    WHERE r.dataset_name = ?
                    """,
                (dataset_name,),
            )
            for row in cursor:
                yield record_class(
                    record_key=row["record_key"],
                    dataset_name=row["dataset_name"],
                    record=row["record_bytes"],
                )
            connection.execute(f"DROP TABLE {table_name}")


def query_str_records_page(
    connection: sqlite3.Connection,
    *,
    dataset_name: str,
    serialization_format: db_models.SerializationFormat,
    limit: int,
    offset: int,
) -> Iterable[db_models.DatasetRecordStrBase]:
    """Yield one page of string-keyed records for a dataset.

    Args:
        connection: Open SQLite database connection.
        dataset_name: Dataset name to query.
        serialization_format: Serialization format of stored record bytes.
        limit: Maximum number of records to return.
        offset: Starting offset for pagination.

    Yields:
        String-keyed record model instances.

    Raises:
        ValueError: If ``serialization_format`` is not supported.
    """
    match serialization_format:
        case db_models.SerializationFormat.YAML:
            record_class = db_models.DatasetRecordStrYaml
        case db_models.SerializationFormat.JSON:
            record_class = db_models.DatasetRecordStrJson
        case db_models.SerializationFormat.PICKLE:
            record_class = db_models.DatasetRecordStrPickle
        case _:
            raise ValueError(
                f"Unsupported serialization format: {serialization_format}. Must be one of 'yaml', 'json', or 'pickle'."
            )
    with connection:
        cursor = connection.execute(
            """
                SELECT record_key, dataset_name, record_bytes
                FROM DatasetRecordsStr
                WHERE dataset_name = ?
                ORDER BY record_key
                LIMIT ?
                OFFSET ?
                """,
            (dataset_name, limit, offset),
        )
        for row in cursor:
            yield record_class(
                record_key=row["record_key"],
                dataset_name=row["dataset_name"],
                record=row["record_bytes"],
            )


def write_sde_metadata(
    connection: sqlite3.Connection, *, sde_metadata: SdeMetadata
) -> None:
    """Write or update SDE metadata for the current dataset snapshot.

    Args:
        connection: Open SQLite database connection.
        sde_metadata: Parsed SDE metadata model.
    """
    with connection:
        connection.execute(
            """
                INSERT INTO SdeMetadata (buildNumber, releaseDate, source_format, source_media)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(buildNumber) DO UPDATE SET releaseDate=excluded.releaseDate, source_format=excluded.source_format, source_media=excluded.source_media
                """,
            (
                sde_metadata.buildNumber,
                sde_metadata.releaseDate,
                sde_metadata.variant,
                ".db",
            ),
        )


def query_sde_metadata(connection: sqlite3.Connection) -> SdeMetadata | None:
    """Read the most recently stored SDE metadata row.

    Args:
        connection: Open SQLite database connection.

    Returns:
        Latest SDE metadata, or ``None`` when metadata has not been written.
    """
    with connection:
        cursor = connection.execute(
            """
                SELECT buildNumber, releaseDate, source_format, source_media
                FROM SdeMetadata
                ORDER BY row_id DESC
                LIMIT 1
                """
        )
        row = cursor.fetchone()
        if row is None:
            return None
        return SdeMetadata(
            buildNumber=int(row["buildNumber"]),
            releaseDate=row["releaseDate"],
            variant=SdeVariant(row["source_format"]),
            source_media=SourceMedia(row["source_media"]),
        )
