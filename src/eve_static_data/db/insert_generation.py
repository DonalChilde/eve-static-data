"""Functions to insert pydantic validated records."""

import sqlite3
from collections.abc import Iterable
from dataclasses import dataclass
from typing import TypedDict

from eve_static_data.models.pydantic import records as pydantic_records


@dataclass(slots=True)
class LocStrings:
    language: str
    field_name: str
    loc_text: str


@dataclass(slots=True)
class LocalField:
    field_name: str
    localized_string: pydantic_records.LocalizedString


def _collect_loc_strings(fields: Iterable[LocalField]) -> list[LocStrings]:
    """Collect localized strings from the given fields."""
    loc_strings: list[LocStrings] = []
    for field in fields:
        for language, loc_text in field.localized_string.model_dump().items():
            loc_strings.append(
                LocStrings(
                    language=language, field_name=field.field_name, loc_text=loc_text
                )
            )
    return loc_strings


def agent_types(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.AgentTypes]
) -> None:
    """Insert records into the agent_types table."""
    with connection as conn:
        cursor = conn.cursor()
        for record in records:
            cursor.execute(
                "INSERT INTO agent_types (agent_types_id, name) VALUES (?, ?);",
                (record.key, record.name),
            )


def agents_in_space(
    connection: sqlite3.Connection, records: Iterable[pydantic_records.AgentsInSpace]
) -> None:
    """Insert records into the agents_in_space table."""
    with connection as conn:
        cursor = conn.cursor()
        for record in records:
            cursor.execute(
                "INSERT INTO agents_in_space (agents_in_space_id, dungeonID, solarSystemID, spawnPointID, typeID) VALUES (?, ?, ?, ?, ?);",
                (
                    record.key,
                    record.dungeonID,
                    record.solarSystemID,
                    record.spawnPointID,
                    record.typeID,
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
            loc_fields = [
                LocalField(field_name="name", localized_string=record.name),
                LocalField(
                    field_name="description", localized_string=record.description
                ),
            ]
            loc_strings = _collect_loc_strings(loc_fields)
            for loc_string in loc_strings:
                cursor.execute(
                    "INSERT INTO ancestries_localized (parent_id, lang, localized_name, localized_description) VALUES (?, ?, ?, ?);",
                    (
                        record.key,
                        loc_string.language,
                        loc_string.field_name,
                        loc_string.loc_text,
                    ),
                )
            # FIXME this does not match table def.
