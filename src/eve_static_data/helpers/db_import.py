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


def bloodlines(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add bloodlines information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 0
        for raw in data.bloodlines():
            bloodline_name = DBM.Bloodlines_Name(
                en=raw["name"]["en"],
                de=raw["name"]["de"],
                fr=raw["name"]["fr"],
                ja=raw["name"]["ja"],
                zh=raw["name"]["zh"],
                ru=raw["name"]["ru"],
                ko=raw["name"]["ko"],
                es=raw["name"]["es"],
            )
            bloodline_description = DBM.Bloodlines_Description(
                en=raw["description"]["en"],
                de=raw["description"]["de"],
                fr=raw["description"]["fr"],
                ja=raw["description"]["ja"],
                zh=raw["description"]["zh"],
                ru=raw["description"]["ru"],
                ko=raw["description"]["ko"],
                es=raw["description"]["es"],
            )
            bloodline = DBM.Bloodlines(
                key=raw["_key"],
                raceID=raw["raceID"],
                charisma=raw["charisma"],
                name=bloodline_name,
                description=bloodline_description,
                iconID=raw.get("iconID"),
                intelligence=raw["intelligence"],
                memory=raw["memory"],
                perception=raw["perception"],
                willpower=raw["willpower"],
            )

            session.add(bloodline)
            count += 1
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(f"Imported {count} bloodlines records in {duration:.2f} seconds.")
        return ImportResult(count=count, duration=duration)


def blueprints(engine: Engine, data: RawJsonTDProtocol) -> ImportResult:
    """Add blueprints information to the database."""
    start = perf_counter()
    with Session(engine) as session:
        count = 0
        for raw in data.blueprints():
            if raw_copying := raw["activities"].get("copying"):
                copying = DBM.Blueprints_Copying(
                    time=raw_copying["time"],
                )
                for material in raw_copying.get("materials", []):
                    copying.materials.append(
                        DBM.Blueprints_Copying_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_copying.get("skills", []):
                    copying.skills.append(
                        DBM.Blueprints_Copying_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_copying.get("products", []):
                    copying.products.append(
                        DBM.Blueprints_Copying_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                copying = None
            if raw_invention := raw["activities"].get("invention"):
                invention = DBM.Blueprints_Invention(
                    time=raw_invention["time"],
                )
                for material in raw_invention.get("materials", []):
                    invention.materials.append(
                        DBM.Blueprints_Invention_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_invention.get("skills", []):
                    invention.skills.append(
                        DBM.Blueprints_Invention_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_invention.get("products", []):
                    invention.products.append(
                        DBM.Blueprints_Invention_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                invention = None
            if raw_manufacturing := raw["activities"].get("manufacturing"):
                manufacturing = DBM.Blueprints_Manufacturing(
                    time=raw_manufacturing["time"],
                )
                for material in raw_manufacturing.get("materials", []):
                    manufacturing.materials.append(
                        DBM.Blueprints_Manufacturing_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_manufacturing.get("skills", []):
                    manufacturing.skills.append(
                        DBM.Blueprints_Manufacturing_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_manufacturing.get("products", []):
                    manufacturing.products.append(
                        DBM.Blueprints_Manufacturing_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                manufacturing = None
            if raw_reaction := raw["activities"].get("reaction"):
                reaction = DBM.Blueprints_Reaction(
                    time=raw_reaction["time"],
                )
                for material in raw_reaction.get("materials", []):
                    reaction.materials.append(
                        DBM.Blueprints_Reaction_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_reaction.get("skills", []):
                    reaction.skills.append(
                        DBM.Blueprints_Reaction_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_reaction.get("products", []):
                    reaction.products.append(
                        DBM.Blueprints_Reaction_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                reaction = None
            if raw_reseaarch_material := raw["activities"].get("research_material"):
                research_material = DBM.Blueprints_Research_Material(
                    time=raw_reseaarch_material["time"],
                )
                for material in raw_reseaarch_material.get("materials", []):
                    research_material.materials.append(
                        DBM.Blueprints_Research_Material_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_reseaarch_material.get("skills", []):
                    research_material.skills.append(
                        DBM.Blueprints_Research_Material_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_reseaarch_material.get("products", []):
                    research_material.products.append(
                        DBM.Blueprints_Research_Material_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                research_material = None
            if raw_research_time := raw["activities"].get("research_time"):
                research_time = DBM.Blueprints_Research_Time(
                    time=raw_research_time["time"],
                )
                for material in raw_research_time.get("materials", []):
                    research_time.materials.append(
                        DBM.Blueprints_Research_Time_Materials(
                            typeID=material["typeID"],
                            quantity=material["quantity"],
                        )
                    )
                for skill in raw_research_time.get("skills", []):
                    research_time.skills.append(
                        DBM.Blueprints_Research_Time_Skills(
                            typeID=skill["typeID"],
                            level=skill["level"],
                        )
                    )
                for product in raw_research_time.get("products", []):
                    research_time.products.append(
                        DBM.Blueprints_Research_Time_Products(
                            typeID=product["typeID"],
                            quantity=product["quantity"],
                            probability=product.get("probability"),
                        )
                    )
            else:
                research_time = None
            blueprint = DBM.Blueprints(
                key=raw["_key"],
                blueprintTypeID=raw["blueprintTypeID"],
                maxProductionLimit=raw["maxProductionLimit"],
                copying=copying,
                invention=invention,
                manufacturing=manufacturing,
                reaction=reaction,
                research_material=research_material,
                research_time=research_time,
            )
            session.add(blueprint)
            count += 1
        session.commit()
        end = perf_counter()
        duration = end - start
        logger.info(f"Imported {count} blueprints records in {duration:.2f} seconds.")
        return ImportResult(count=count, duration=duration)
