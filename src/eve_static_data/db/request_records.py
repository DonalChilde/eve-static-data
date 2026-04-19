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
    cursor.execute("SELECT agent_types_id, name FROM agent_types;")
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
