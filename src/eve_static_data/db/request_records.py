"""Functions to retrieve records from the database and return them as dataclass models."""

import sqlite3
from collections.abc import Iterable

from eve_static_data.models.pydantic import yaml_records as pydantic_records
from eve_static_data.models.type_defs import Lang

LANGS: set[Lang] = {"en", "de", "fr", "ja", "ru", "zh", "ko", "es"}


def agent_types(
    connection: sqlite3.Connection,
) -> Iterable[pydantic_records.AgentTypes]:
    """Retrieve records from the agent_types table and return them as pydantic models."""
    cursor = connection.cursor()
    cursor.execute("SELECT agent_types_id, agent_name FROM agent_types;")
    for row in cursor:
        yield pydantic_records.AgentTypes(agent_types_id=row[0], name=row[1])


def agents_in_space(
    connection: sqlite3.Connection,
) -> Iterable[pydantic_records.AgentsInSpace]:
    """Retrieve records from the agents_in_space table and return them as pydantic models."""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT agents_in_space_id, dungeonID, solarSystemID, spawnPointID, typeID FROM agents_in_space;"
    )
    for row in cursor:
        yield pydantic_records.AgentsInSpace(
            agents_in_space_id=row[0],
            dungeonID=row[1],
            solarSystemID=row[2],
            spawnPointID=row[3],
            typeID=row[4],
        )


def ancestries(
    connection: sqlite3.Connection,
) -> Iterable[pydantic_records.Ancestries]:
    """Retrieve records from the ancestries table and return them as pydantic models."""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT ancestries_id, bloodlineID, charisma, iconID, intelligence, memory, perception, shortDescription, willpower FROM ancestries;"
    )
    for row in cursor:
        cursor_localized = connection.cursor()
        cursor_localized.execute(
            "SELECT lang,localized_name, localized_description FROM ancestries_localized WHERE parent_id = ?;",
            (row[0],),
        )
        localized_names: dict[str, str] = {}
        localized_descriptions: dict[str, str] = {}
        for localized_row in cursor_localized:
            localized_names[localized_row[0]] = localized_row[1]
            localized_descriptions[localized_row[0]] = localized_row[2]
        name = pydantic_records.LocalizedString(**localized_names)
        description = pydantic_records.LocalizedString(**localized_descriptions)

        yield pydantic_records.Ancestries(
            ancestries_id=row[0],
            bloodlineID=row[1],
            charisma=row[2],
            iconID=row[3],
            intelligence=row[4],
            memory=row[5],
            perception=row[6],
            shortDescription=row[7],
            willpower=row[8],
            name=name,
            description=description,
        )


def bloodlines(
    connection: sqlite3.Connection,
) -> Iterable[pydantic_records.Bloodlines]:
    """Retrieve records from the bloodlines table and return them as pydantic models."""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT bloodlines_id, charisma, corporationID, iconID, intelligence, memory, perception, raceID, willpower FROM bloodlines;"
    )
    for row in cursor:
        cursor_localized = connection.cursor()
        cursor_localized.execute(
            "SELECT lang,localized_name, localized_description FROM bloodlines_localized WHERE parent_id = ?;",
            (row[0],),
        )
        localized_names: dict[str, str] = {}
        localized_descriptions: dict[str, str] = {}
        for localized_row in cursor_localized:
            localized_names[localized_row[0]] = localized_row[1]
            localized_descriptions[localized_row[0]] = localized_row[2]
        name = pydantic_records.LocalizedString(**localized_names)
        description = pydantic_records.LocalizedString(**localized_descriptions)

        yield pydantic_records.Bloodlines(
            bloodlines_id=row[0],
            charisma=row[1],
            corporationID=row[2],
            description=description,
            iconID=row[3],
            intelligence=row[4],
            memory=row[5],
            name=name,
            perception=row[6],
            raceID=row[7],
            willpower=row[8],
        )
