"""Functions to insert validated records from pydantic rootmodels."""

import sqlite3

from eve_static_data.models.pydantic import yaml_records as pydantic_records
from eve_static_data.models.type_defs import Lang

LANGS: set[Lang] = {"en", "de", "fr", "ja", "ru", "zh", "ko", "es"}


def agent_types(
    connection: sqlite3.Connection, records: pydantic_records.AgentTypesRoot
) -> None:
    """Insert records into the agent_types table."""
    with connection as conn:
        cursor = conn.cursor()
        for agent_types_id, record in records.root.items():
            cursor.execute(
                "INSERT INTO agent_types (agent_types_id, name) VALUES (?, ?);",
                (agent_types_id, record.name),
            )


def agents_in_space(
    connection: sqlite3.Connection, records: pydantic_records.AgentsInSpaceRoot
) -> None:
    """Insert records into the agents_in_space table."""
    with connection as conn:
        cursor = conn.cursor()
        for agents_in_space_id, record in records.root.items():
            cursor.execute(
                "INSERT INTO agents_in_space (agents_in_space_id, dungeonID, solarSystemID, spawnPointID, typeID) VALUES (?, ?, ?, ?, ?);",
                (
                    agents_in_space_id,
                    record.dungeonID,
                    record.solarSystemID,
                    record.spawnPointID,
                    record.typeID,
                ),
            )


def ancestries(
    connection: sqlite3.Connection, records: pydantic_records.AncestriesRoot
) -> None:
    """Insert records into the ancestries table."""
    with connection as conn:
        cursor = conn.cursor()
        for ancestries_id, record in records.root.items():
            cursor.execute(
                "INSERT INTO ancestries (ancestries_id, bloodlineID, charisma, iconID, intelligence, memory, perception, shortDescription, willpower) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);",
                (
                    ancestries_id,
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
                        ancestries_id,
                        lang,
                        getattr(record.name, lang),
                        getattr(record.description, lang),
                    ),
                )
