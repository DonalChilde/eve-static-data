"""Tests for SQLite insert helpers."""

import sqlite3
from pathlib import Path

from eve_static_data.db.insert_generation import blueprints
from eve_static_data.models.pydantic import records as pydantic_records


def _blueprints_schema() -> str:
    """Return the SQL schema used by the blueprint insert helper."""
    repo_root = Path(__file__).resolve().parents[3]
    return (
        repo_root / "src" / "eve_static_data" / "db" / "table_sql" / "blueprints.sql"
    ).read_text(encoding="utf-8")


def test_blueprints_insert_writes_parent_and_activity_rows() -> None:
    """Blueprint inserts should create parent, activity, and child rows."""
    connection = sqlite3.connect(":memory:")
    connection.executescript(_blueprints_schema())

    record = pydantic_records.Blueprints(
        _key=1001,
        blueprintTypeID=2002,
        maxProductionLimit=3003,
        activities={
            "manufacturing": {
                "time": 60,
                "materials": [
                    {"typeID": 34, "quantity": 5},
                    {"typeID": 35, "quantity": 7},
                ],
                "products": [
                    {"typeID": 36, "quantity": 1, "probability": None},
                ],
                "skills": [
                    {"typeID": 3380, "level": 4},
                ],
            },
            "copying": {
                "time": 120,
            },
        },
    )

    blueprints(connection, [record])

    assert connection.execute(
        "SELECT blueprints_id, blueprintTypeID, maxProductionLimit FROM blueprints"
    ).fetchall() == [(1001, 2002, 3003)]
    assert connection.execute(
        "SELECT blueprint_id, activity_type, activity_time FROM blueprint_activities ORDER BY activity_type"
    ).fetchall() == [(1001, "copying", 120), (1001, "manufacturing", 60)]
    assert connection.execute(
        "SELECT typeID, quantity FROM activity_materials ORDER BY typeID"
    ).fetchall() == [(34, 5), (35, 7)]
    assert connection.execute(
        "SELECT typeID, skill_level FROM activity_skills"
    ).fetchall() == [(3380, 4)]
    assert connection.execute(
        "SELECT typeID, quantity, probability FROM activity_products"
    ).fetchall() == [(36, 1, None)]


def test_blueprints_insert_skips_empty_optional_child_lists() -> None:
    """Activities without optional child collections should not create child rows."""
    connection = sqlite3.connect(":memory:")
    connection.executescript(_blueprints_schema())

    record = pydantic_records.Blueprints(
        _key=4004,
        blueprintTypeID=5005,
        maxProductionLimit=6006,
        activities={
            "research_time": {
                "time": 30,
            },
        },
    )

    blueprints(connection, [record])

    assert connection.execute(
        "SELECT blueprint_id, activity_type, activity_time FROM blueprint_activities"
    ).fetchall() == [(4004, "research_time", 30)]
    assert connection.execute("SELECT COUNT(*) FROM activity_materials").fetchone() == (
        0,
    )
    assert connection.execute("SELECT COUNT(*) FROM activity_skills").fetchone() == (0,)
    assert connection.execute("SELECT COUNT(*) FROM activity_products").fetchone() == (
        0,
    )
