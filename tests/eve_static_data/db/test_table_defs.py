"""Tests for SQLite schema generation in table_defs."""

import re

from eve_static_data.db import table_defs


def _table_names(sql_statements: list[str]) -> list[str]:
    """Extract table names from CREATE TABLE statements."""
    names: list[str] = []
    pattern = re.compile(r"CREATE TABLE IF NOT EXISTS\s+([a-z0-9_]+)")
    for statement in sql_statements:
        match = pattern.search(statement)
        if match:
            names.append(match.group(1))
    return names


def test_schema_contains_main_table_with_surrogate_primary_key() -> None:
    """Main tables should have surrogate autoincrement primary keys."""
    target = "agents_in_space"
    matching = [
        stmt
        for stmt in table_defs.CREATE_TABLE_STATEMENTS
        if stmt.startswith(f"CREATE TABLE IF NOT EXISTS {target}")
    ]
    assert len(matching) == 1
    assert "id INTEGER PRIMARY KEY AUTOINCREMENT" in matching[0]
    assert "source_key INTEGER" in matching[0]


def test_schema_creates_localization_tables() -> None:
    """LocalizedString fields should generate localization tables."""
    table_names = _table_names(table_defs.CREATE_TABLE_STATEMENTS)
    assert "ancestries_name_localized" in table_names
    assert "ancestries_description_localized" in table_names


def test_schema_creates_junction_tables_for_list_fields() -> None:
    """List fields should generate parent-scoped junction tables."""
    table_names = _table_names(table_defs.CREATE_TABLE_STATEMENTS)
    assert "blueprints_activities" in table_names
    assert "blueprints_activity_materials" in table_names


def test_schema_tables_are_alphabetized() -> None:
    """Generated table statements should be sorted alphabetically."""
    table_names = _table_names(table_defs.CREATE_TABLE_STATEMENTS)
    assert table_names == sorted(table_names)


def test_source_key_index_exists() -> None:
    """Source-key index should exist for tables with a key field."""
    assert (
        "CREATE INDEX IF NOT EXISTS idx_agents_in_space_source_key "
        "ON agents_in_space (source_key);" in table_defs.CREATE_INDEX_STATEMENTS
    )
