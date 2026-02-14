"""Functions for importing jsonl files into the database."""

import logging
from dataclasses import dataclass

from sqlalchemy import Engine
from sqlalchemy.orm import Session

import eve_static_data.models.db as DBM
from eve_static_data.access.raw_json_td_protocol import RawJsonTDProtocol

logger = logging.getLogger(__name__)
from time import perf_counter


@dataclass
class ImportResult:
    """The result of an import operation."""

    count: int
    duration: float


def sde_info(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add SDE information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 1
        raw = data.sde_info()
        sde_info = DBM.SdeInfo(
            key=raw["_key"],
            buildNumber=raw["buildNumber"],
            releaseDate=raw["releaseDate"],
        )
        session.add(sde_info)
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(f"Imported {count} sde_info records in {duration:.2f} seconds.")
        return ImportResult(count=count, duration=duration)


def agents_in_space(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add agents in space information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 0
        for raw in data.agents_in_space():
            agent = DBM.AgentsInSpace(
                key=raw["_key"],
                dungeonID=raw["dungeonID"],
                solarSystemID=raw["solarSystemID"],
                spawnPointID=raw["spawnPointID"],
                typeID=raw["typeID"],
            )
            session.add(agent)
            count += 1
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(
            f"Imported {count} agents_in_space records in {duration:.2f} seconds."
        )
        return ImportResult(count=count, duration=duration)


def agent_types(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add agent types information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 0
        for raw in data.agent_types():
            agent_type = DBM.AgentTypes(
                key=raw["_key"],
                name=raw["name"],
            )
            session.add(agent_type)
            count += 1
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(f"Imported {count} agent_types records in {duration:.2f} seconds.")
        return ImportResult(count=count, duration=duration)


def ancestries(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add ancestries information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 0
        for raw in data.ancestries():
            ancestry_name = DBM.Ancestries_Name(
                en=raw["name"]["en"],
                de=raw["name"]["de"],
                fr=raw["name"]["fr"],
                ja=raw["name"]["ja"],
                zh=raw["name"]["zh"],
                ru=raw["name"]["ru"],
                ko=raw["name"]["ko"],
                es=raw["name"]["es"],
            )
            ancestry_description = DBM.Ancestries_Description(
                en=raw["description"]["en"],
                de=raw["description"]["de"],
                fr=raw["description"]["fr"],
                ja=raw["description"]["ja"],
                zh=raw["description"]["zh"],
                ru=raw["description"]["ru"],
                ko=raw["description"]["ko"],
                es=raw["description"]["es"],
            )
            ancestry = DBM.Ancestries(
                key=raw["_key"],
                bloodlineID=raw["bloodlineID"],
                charisma=raw["charisma"],
                name=ancestry_name,
                description=ancestry_description,
                iconID=raw.get("iconID"),
                intelligence=raw["intelligence"],
                memory=raw["memory"],
                perception=raw["perception"],
                willpower=raw["willpower"],
                shortDescription=raw.get("shortDescription"),
            )

            session.add(ancestry)
            count += 1
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(f"Imported {count} ancestries records in {duration:.2f} seconds.")
        return ImportResult(count=count, duration=duration)
