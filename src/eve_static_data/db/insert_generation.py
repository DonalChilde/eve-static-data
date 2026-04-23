"""Functions to insert pydantic validated records.

The tables are defined in SQL files in the table_sql directory.

Datasets with only a top level table can be inserted with executemany and a
generator that yields tuples of the record fields.

Datasets with a main table and sub_tables can be inserted with a loop that executes
the appropriate SQL statements for each record and its related sub_tables. The main
table should be inserted first, followed by any related sub_tables.
"""

# NOTE: Deprecated. Moving to inserts from a different data model.

# The INSERT statements in this module should match the table definitions in the table_sql files.
# The functions should be named after the table they insert into, and should take a connection
# and an iterable of pydantic records as arguments. The functions should use the connection
# to execute SQL statements that insert the records into the appropriate tables.
# The functions should also handle the insertion of any sub_tables that are related to the main table.

import sqlite3
from collections.abc import Iterable

from eve_static_data.models.common import Lang
from eve_static_data.models.pydantic import records as pydantic_records

LANGS: set[Lang] = {"en", "de", "fr", "ja", "ru", "zh", "ko", "es"}


def agent_types(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.AgentTypes]
) -> None:
    """Insert records into the agent_types table."""

    with connection as conn:
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT INTO agent_types (agent_types_id, name) VALUES (?, ?);",
            ((record.key, record.name) for record in records),
        )


def agents_in_space(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.AgentsInSpace]
) -> None:
    """Insert records into the agents_in_space table."""
    with connection as conn:
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT INTO agents_in_space (agents_in_space_id, dungeonID, solarSystemID, spawnPointID, typeID) VALUES (?, ?, ?, ?, ?);",
            (
                (
                    record.key,
                    record.dungeonID,
                    record.solarSystemID,
                    record.spawnPointID,
                    record.typeID,
                )
                for record in records
            ),
        )


def ancestries(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.Ancestries]
) -> None:
    """Insert records into the ancestries table."""
    with connection as conn:
        cursor = conn.cursor()
        for record in records:
            cursor.execute(
                "INSERT INTO ancestries (ancestries_id, bloodlineID, charisma, iconID, intelligence, memory, perception, shortDescription, willpower) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
                (
                    record.key,
                    record.bloodlineID,
                    record.charisma,
                    record.iconID,
                    record.intelligence,
                    record.memory,
                    record.perception,
                    record.shortDescription,
                    record.willpower,
                ),
            )
            for lang in LANGS:
                cursor.execute(
                    "INSERT INTO ancestries_localized (parent_id, lang, localized_name, localized_description) VALUES (?, ?, ?, ?);",
                    (
                        record.key,
                        lang,
                        getattr(record.name, lang),
                        getattr(record.description, lang),
                    ),
                )


def bloodlines(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.Bloodlines]
) -> None:
    """Insert records into the bloodlines table."""
    with connection as conn:
        cursor = conn.cursor()
        for record in records:
            cursor.execute(
                "INSERT INTO bloodlines (bloodline_id,charisma, corporationID,iconID, intelligence, memory, perception, raceID, willpower) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                (
                    record.key,
                    record.charisma,
                    record.corporationID,
                    record.iconID,
                    record.intelligence,
                    record.memory,
                    record.perception,
                    record.raceID,
                    record.willpower,
                ),
            )
            for lang in LANGS:
                cursor.execute(
                    "INSERT INTO bloodlines_localized (parent_id, lang, localized_name, localized_description) VALUES (?, ?, ?, ?);",
                    (
                        record.key,
                        lang,
                        getattr(record.name, lang),
                        getattr(record.description, lang),
                    ),
                )


def blueprints(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.Blueprints]
) -> None:
    """Insert records into the blueprints table."""
    activity_types = (
        "copying",
        "invention",
        "manufacturing",
        "reaction",
        "research_material",
        "research_time",
    )

    with connection as conn:
        cursor = conn.cursor()
        for record in records:
            cursor.execute(
                "INSERT INTO blueprints (blueprints_id, blueprintTypeID, maxProductionLimit) VALUES (?, ?, ?);",
                (record.key, record.blueprintTypeID, record.maxProductionLimit),
            )

            for activity_type in activity_types:
                activity: pydantic_records.Blueprints_Activity | None = getattr(
                    record.activities, activity_type
                )
                if activity is None:
                    continue

                cursor.execute(
                    "INSERT INTO blueprint_activities (blueprint_id, activity_type, activity_time) VALUES (?, ?, ?);",
                    (record.key, activity_type, activity.time),
                )
                activity_id = cursor.lastrowid
                if activity_id is None:
                    msg = "Failed to create blueprint activity row"
                    raise sqlite3.DatabaseError(msg)

                if activity.materials is not None:
                    cursor.executemany(
                        "INSERT INTO activity_materials (activity_id, typeID, quantity) VALUES (?, ?, ?);",
                        (
                            (activity_id, material.typeID, material.quantity)
                            for material in activity.materials
                        ),
                    )

                if activity.skills is not None:
                    cursor.executemany(
                        "INSERT INTO activity_skills (activity_id, typeID, skill_level) VALUES (?, ?, ?);",
                        (
                            (activity_id, skill.typeID, skill.level)
                            for skill in activity.skills
                        ),
                    )

                if activity.products is not None:
                    cursor.executemany(
                        "INSERT INTO activity_products (activity_id, typeID, quantity, probability) VALUES (?, ?, ?, ?);",
                        (
                            (
                                activity_id,
                                product.typeID,
                                product.quantity,
                                product.probability,
                            )
                            for product in activity.products
                        ),
                    )
