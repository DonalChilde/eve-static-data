"""Functions to retrieve records from the database and return them as dataclass models."""

import sqlite3
from collections.abc import Iterable
from typing import Any

from eve_static_data.models.common import Lang
from eve_static_data.models.pydantic import yaml_records as pydantic_records

LANGS: set[Lang] = {"en", "de", "fr", "ja", "ru", "zh", "ko", "es"}
ACTIVITIES: set[str] = {
    "copying",
    "invention",
    "manufacturing",
    "reaction",
    "research_material",
    "research_time",
}
# from typing import TypeVar

# T = TypeVar("T")


def chunked[T](items: Iterable[T], size: int = 999) -> Iterable[list[T]]:
    """Yield successive chunks of `size` from `items`."""
    chunk_list: list[T] = list(items)
    for i in range(0, len(chunk_list), size):
        yield chunk_list[i : i + size]


def placeholders[T](chunk: list[T]) -> str:
    """Return a SQL placeholder string for a chunk, e.g. '?,?,?'."""
    return ",".join("?" * len(chunk))


def fetch_id_chunked_rows(
    cursor: sqlite3.Cursor, query: str, fetch_ids: Iterable[int]
) -> list[tuple[Any, ...]]:
    """Fetch rows from the database in chunks to avoid hitting SQLite's parameter limit.

    Example query:
    `SELECT blueprints_id, blueprintTypeID, maxProductionLimit FROM blueprints WHERE blueprints_id IN ({placeholders});`
    """
    rows: list[tuple[Any, ...]] = []
    for chunk in chunked(fetch_ids):
        cursor.execute(query.format(id_placeholders=placeholders(chunk)), chunk)
        rows.extend(cursor.fetchall())
    return rows


def fetch_rows(cursor: sqlite3.Cursor, query: str) -> list[tuple[Any, ...]]:
    """Fetch all rows from the database for a given query."""
    cursor.execute(query)
    return cursor.fetchall()


from dataclasses import dataclass, field


@dataclass
class Query:
    table: str
    columns: list[str]
    filters: dict[str, Any] = field(default_factory=dict[str, Any])
    id_column: str | None = None

    def _base(self) -> str:
        cols = ", ".join(self.columns)
        return f"SELECT {cols} FROM {self.table}"

    def build(self, chunk: list[int] | None = None) -> tuple[str, list[Any]]:
        """Return (sql, params) ready to pass to cursor.execute().

        Args:
            chunk: Optional list of id values to filter by. If None, no id filter is applied.
        """
        if chunk is not None and self.id_column is None:
            raise ValueError("id_column must be set when filtering by ids")
        clauses: list[str] = []
        params: list[Any] = []

        if chunk is not None:
            clauses.append(f"{self.id_column} IN ({placeholders(chunk)})")
            params.extend(chunk)

        for col, val in self.filters.items():
            clauses.append(f"{col} = ?")
            params.append(val)

        sql = self._base()
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        sql += ";"

        return sql, params


def execute_query(
    cursor: sqlite3.Cursor,
    query: Query,
    fetch_ids: Iterable[int] | None = None,
) -> list[tuple[Any, ...]]:
    """Execute a Query, optionally chunked by fetch_ids.

    Args:
        cursor: Database cursor to execute the query.
        query: Query object defining the table, columns, and filters.
        fetch_ids: Optional iterable of id values to filter by. If None, retrieves all records.

    Raises:
        ValueError: If fetch_ids is provided but query.id_column is not set.
    """
    if fetch_ids is None:
        sql, params = query.build()
        cursor.execute(sql, params)
        return cursor.fetchall()

    rows: list[tuple[Any, ...]] = []
    for chunk in chunked(list(fetch_ids)):
        sql, params = query.build(chunk)
        cursor.execute(sql, params)
        rows.extend(cursor.fetchall())
    return rows


def agent_types(
    cursor: sqlite3.Cursor,
    fetch_ids: Iterable[int] | None = None,
) -> list[pydantic_records.AgentTypes]:
    """Retrieve records from the agent_types table and return them as pydantic models."""
    query = Query(
        table="agent_types",
        columns=["agent_types_id", "agent_name"],
        id_column="agent_types_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    results: list[pydantic_records.AgentTypes] = []
    for row in rows:
        results.append(pydantic_records.AgentTypes(agent_types_id=row[0], name=row[1]))
    return results


def agents_in_space(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[pydantic_records.AgentsInSpace]:
    """Retrieve records from the agents_in_space table and return them as pydantic models."""
    query = Query(
        table="agents_in_space",
        columns=[
            "agents_in_space_id",
            "dungeonID",
            "solarSystemID",
            "spawnPointID",
            "typeID",
        ],
        id_column="agents_in_space_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    results: list[pydantic_records.AgentsInSpace] = []
    for row in rows:
        results.append(
            pydantic_records.AgentsInSpace(
                agents_in_space_id=row[0],
                dungeonID=row[1],
                solarSystemID=row[2],
                spawnPointID=row[3],
                typeID=row[4],
            )
        )
    return results


def ancestries_localized_fields(
    cursor: sqlite3.Cursor,
    lang: Lang | None = None,
    fetch_ids: Iterable[int] | None = None,
) -> list[tuple[int, Lang, str, str]]:
    """Retrieve localized name and description for an ancestries record.

    Args:
        cursor: Database cursor to execute the query.
        lang: Optional language code to filter results by. If None, retrieves all languages.
        fetch_ids: Optional iterable of ancestries_id values to filter results by. If None, retrieves all records.
    """
    query = Query(
        table="ancestries_localized",
        columns=["ancestries_id", "lang", "localized_name", "localized_description"],
        filters={"lang": lang} if lang else {},
        id_column="ancestries_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def ancestries(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[pydantic_records.Ancestries]:
    """Retrieve records from the ancestries table and return them as pydantic models."""
    ancestries_query = Query(
        table="ancestries",
        columns=[
            "ancestries_id",
            "bloodlineID",
            "charisma",
            "iconID",
            "intelligence",
            "memory",
            "perception",
            "shortDescription",
            "willpower",
        ],
        id_column="ancestries_id",
    )
    ancestries_rows = execute_query(cursor, ancestries_query, fetch_ids)
    localized_fetch_ids = [row[0] for row in ancestries_rows] if fetch_ids else None
    localized_query = Query(
        table="ancestries_localized",
        columns=["ancestries_id", "lang", "localized_name", "localized_description"],
        id_column="ancestries_id",
    )
    localized_rows = execute_query(cursor, localized_query, localized_fetch_ids)
    # index localized rows by ancestries_id for quick lookup
    localized_dict: dict[int, list[tuple[Any, ...]]] = {}
    for row in localized_rows:
        localized_dict.setdefault(row[0], []).append(row)
    results: list[pydantic_records.Ancestries] = []
    for row in ancestries_rows:
        localized_rows_for_parent = localized_dict.get(row[0], [])
        localized_names: dict[str, str] = {}
        localized_descriptions: dict[str, str] = {}
        for localized_row in localized_rows_for_parent:
            localized_names[localized_row[1]] = localized_row[2]
            localized_descriptions[localized_row[1]] = localized_row[3]
        name = pydantic_records.LocalizedString(**localized_names)
        description = pydantic_records.LocalizedString(**localized_descriptions)

        results.append(
            pydantic_records.Ancestries(
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
        )
    return results


def bloodlines_localized_fields(
    cursor: sqlite3.Cursor,
    lang: Lang | None = None,
    fetch_ids: Iterable[int] | None = None,
) -> list[tuple[int, Lang, str, str]]:
    """Retrieve localized name and description for a bloodlines record.

    Args:
        cursor: Database cursor to execute the query.
        lang: Optional language code to filter results by. If None, retrieves all languages.
        fetch_ids: Optional iterable of bloodlines_id values to filter results by. If None, retrieves all records.
    """
    query = Query(
        table="bloodlines_localized",
        columns=["bloodlines_id", "lang", "localized_name", "localized_description"],
        filters={"lang": lang} if lang else {},
        id_column="bloodlines_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def bloodlines(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[pydantic_records.Bloodlines]:
    """Retrieve records from the bloodlines table and return them as pydantic models."""
    bloodlines_query = Query(
        table="bloodlines",
        columns=[
            "bloodlines_id",
            "charisma",
            "corporationID",
            "iconID",
            "intelligence",
            "memory",
            "perception",
            "raceID",
            "willpower",
        ],
        id_column="bloodlines_id",
    )
    bloodlines_rows = execute_query(cursor, bloodlines_query, fetch_ids)
    localized_ids = [row[0] for row in bloodlines_rows] if fetch_ids else None
    localized_query = Query(
        table="bloodlines_localized",
        columns=["bloodlines_id", "lang", "localized_name", "localized_description"],
        id_column="bloodlines_id",
    )
    localized_rows = execute_query(cursor, localized_query, localized_ids)
    # index localized rows by bloodlines_id for quick lookup
    localized_dict: dict[int, list[tuple[Any, ...]]] = {}
    for row in localized_rows:
        localized_dict.setdefault(row[0], []).append(row)
    results: list[pydantic_records.Bloodlines] = []
    for row in bloodlines_rows:
        localized_rows_for_parent = localized_dict.get(row[0], [])
        localized_names: dict[str, str] = {}
        localized_descriptions: dict[str, str] = {}
        for localized_row in localized_rows_for_parent:
            localized_names[localized_row[1]] = localized_row[2]
            localized_descriptions[localized_row[1]] = localized_row[3]
        name = pydantic_records.LocalizedString(**localized_names)
        description = pydantic_records.LocalizedString(**localized_descriptions)

        results.append(
            pydantic_records.Bloodlines(
                bloodlines_id=row[0],
                charisma=row[1],
                corporationID=row[2],
                iconID=row[3],
                intelligence=row[4],
                memory=row[5],
                perception=row[6],
                raceID=row[7],
                willpower=row[8],
                name=name,
                description=description,
            )
        )
    return results


def blueprints_activities(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[tuple[int, int, str, int]]:
    """Retrieve records from the blueprint_activities table."""
    query = Query(
        table="blueprint_activities",
        columns=[
            "blueprint_activity_id",
            "blueprint_id",
            "activity_type",
            "activity_time",
        ],
        id_column="blueprint_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def blueprint_activity_materials(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[tuple[int, int, int, int]]:
    """Retrieve records from the blueprint_activity_materials table."""
    query = Query(
        table="blueprint_activity_materials",
        columns=["activity_material_id", "blueprint_activity_id", "typeID", "quantity"],
        id_column="blueprint_activity_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def blueprint_activity_skills(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[tuple[int, int, int, int]]:
    """Retrieve records from the blueprint_activity_skills table."""
    query = Query(
        table="blueprint_activity_skills",
        columns=["activity_skill_id", "blueprint_activity_id", "typeID", "skill_level"],
        id_column="blueprint_activity_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def blueprint_activity_products(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[tuple[int, int, int, int, float]]:
    """Retrieve records from the blueprint_activity_products table."""
    query = Query(
        table="blueprint_activity_products",
        columns=[
            "activity_product_id",
            "blueprint_activity_id",
            "typeID",
            "quantity",
            "probability",
        ],
        id_column="blueprint_activity_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def blueprints(
    cursor: sqlite3.Cursor,
) -> list[pydantic_records.Blueprints]:
    """Retrieve records from the blueprints table and return them as pydantic models."""
    blueprints_query = Query(
        table="blueprints",
        columns=["blueprints_id", "blueprintTypeID", "maxProductionLimit"],
        id_column="blueprints_id",
    )
    blueprints_rows = execute_query(cursor, blueprints_query)
    blueprints_ids = [row[0] for row in blueprints_rows]
    blueprints_activities_rows = blueprints_activities(cursor, blueprints_ids)
    blueprints_activities_ids = [row[0] for row in blueprints_activities_rows]
    # index blueprint activities by blueprint_id for quick lookup when retrieving materials, skills, and products
    activity_rows_by_blueprint: dict[int, list[tuple[Any, ...]]] = {}
    for row in blueprints_activities_rows:
        activity_rows_by_blueprint.setdefault(row[1], []).append(row)
    materials_rows = blueprint_activity_materials(cursor, blueprints_activities_ids)
    skills_rows = blueprint_activity_skills(cursor, blueprints_activities_ids)
    products_rows = blueprint_activity_products(cursor, blueprints_activities_ids)
    # index materials, skills, and products by blueprint_activity_id for quick lookup
    materials_rows_by_activity_id: dict[int, list[tuple[Any, ...]]] = {}
    for row in materials_rows:
        materials_rows_by_activity_id.setdefault(row[1], []).append(row)
    skills_rows_by_activity_id: dict[int, list[tuple[Any, ...]]] = {}
    for row in skills_rows:
        skills_rows_by_activity_id.setdefault(row[1], []).append(row)
    products_rows_by_activity_id: dict[int, list[tuple[Any, ...]]] = {}
    for row in products_rows:
        products_rows_by_activity_id.setdefault(row[1], []).append(row)
    results: list[pydantic_records.Blueprints] = []
    for row in blueprints_rows:
        blueprint_id = row[0]
        blueprintTypeID = row[1]
        maxProductionLimit = row[2]

        activity_rows_for_blueprint = activity_rows_by_blueprint.get(blueprint_id, [])
        activities: dict[str, pydantic_records.Blueprints_Activity | None] = {
            k: None for k in ACTIVITIES
        }
        for activity_row in activity_rows_for_blueprint:
            activity_id = activity_row[0]
            materials_rows_for_activity = materials_rows_by_activity_id.get(
                activity_id, []
            )
            materials: list[pydantic_records.Materials] | None = None
            for material_row in materials_rows_for_activity:
                if materials is None:
                    materials = []
                materials.append(
                    pydantic_records.Materials(
                        typeID=material_row[2],
                        quantity=material_row[3],
                    )
                )
            skills_rows_for_activity = skills_rows_by_activity_id.get(activity_id, [])
            skills: list[pydantic_records.Skills] | None = None
            for skill_row in skills_rows_for_activity:
                if skills is None:
                    skills = []
                skills.append(
                    pydantic_records.Skills(
                        typeID=skill_row[2],
                        level=skill_row[3],
                    )
                )
            products_rows_for_activity = products_rows_by_activity_id.get(
                activity_id, []
            )
            products: list[pydantic_records.Blueprints_Products] | None = None
            for product_row in products_rows_for_activity:
                if products is None:
                    products = []
                products.append(
                    pydantic_records.Blueprints_Products(
                        typeID=product_row[2],
                        quantity=product_row[3],
                        probability=product_row[4],
                    )
                )
            activities[activity_row[2]] = pydantic_records.Blueprints_Activity(
                time=activity_row[3],
                materials=materials,
                skills=skills,
                products=products,
            )
        results.append(
            pydantic_records.Blueprints(
                blueprints_id=blueprint_id,
                blueprintTypeID=blueprintTypeID,
                maxProductionLimit=maxProductionLimit,
                activities=pydantic_records.Blueprints_Activities(**activities),
            )
        )
    return results


def categories_localized_fields(
    cursor: sqlite3.Cursor,
    lang: Lang | None = None,
    fetch_ids: Iterable[int] | None = None,
) -> list[tuple[int, Lang, str]]:
    """Retrieve localized name for a categories record.

    Args:
        cursor: Database cursor to execute the query.
        lang: Optional language code to filter results by. If None, retrieves all languages.
        fetch_ids: Optional iterable of categories_id values to filter results by. If None, retrieves all records.
    """
    query = Query(
        table="categories_localized",
        columns=["categories_id", "lang", "localized_name"],
        filters={"lang": lang} if lang else {},
        id_column="categories_id",
    )
    rows = execute_query(cursor, query, fetch_ids)
    return rows


def categories(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[pydantic_records.Categories]:
    """Retrieve records from the categories table and return them as pydantic models."""
    categories_query = Query(
        table="categories",
        columns=["categories_id", "iconID", "published"],
        id_column="categories_id",
    )
    categories_rows = execute_query(cursor, categories_query, fetch_ids)
    localized_fetch_ids = [row[0] for row in categories_rows] if fetch_ids else None
    localized_query = Query(
        table="categories_localized",
        columns=["categories_id", "lang", "localized_name"],
        id_column="categories_id",
    )
    localized_rows = execute_query(cursor, localized_query, localized_fetch_ids)
    # index localized rows by categories_id for quick lookup
    localized_dict: dict[int, list[tuple[Any, ...]]] = {}
    for row in localized_rows:
        localized_dict.setdefault(row[0], []).append(row)
    results: list[pydantic_records.Categories] = []
    for row in categories_rows:
        categories_id = row[0]
        localized_rows_for_parent = localized_dict.get(categories_id, [])
        localized_names: dict[str, str] = {}
        for localized_row in localized_rows_for_parent:
            localized_names[localized_row[1]] = localized_row[2]
        name = pydantic_records.LocalizedString(**localized_names)
        results.append(
            pydantic_records.Categories(
                categories_id=categories_id,
                iconID=row[1],
                published=bool(row[2]),
                name=name,
            )
        )
    return results


def certificates(
    cursor: sqlite3.Cursor, fetch_ids: Iterable[int] | None = None
) -> list[pydantic_records.Certificates]:
    """Retrieve records from the certificates table and return them as pydantic models."""
    certificates_query = Query(
        table="certificates",
        columns=["certificates_id", "groupID"],
        id_column="certificates_id",
    )
    certificates_rows = execute_query(cursor, certificates_query, fetch_ids)
    certificates_ids = [row[0] for row in certificates_rows]
    localized_query = Query(
        table="certificates_localized",
        columns=["certificates_id", "lang", "localized_name", "localized_description"],
        id_column="certificates_id",
    )
    localized_rows = execute_query(cursor, localized_query, certificates_ids)
    # index localized rows by certificates_id for quick lookup
    localized_dict: dict[int, list[tuple[Any, ...]]] = {}
    for row in localized_rows:
        localized_dict.setdefault(row[0], []).append(row)
    skill_types_query = Query(
        table="certificates_skill_type",
        columns=[
            "certificates_skill_type_id",
            "certificates_id",
            "basic_lvl",
            "standard_lvl",
            "improved_lvl",
            "advanced_lvl",
            "elite_lvl",
        ],
        id_column="certificates_id",
    )
    skill_types_rows = execute_query(cursor, skill_types_query, certificates_ids)
    skill_types_by_certificate_id: dict[int, list[tuple[Any, ...]]] = {}
    for row in skill_types_rows:
        skill_types_by_certificate_id.setdefault(row[1], []).append(row)
    recommended_for_query = Query(
        table="certificates_recommended_for",
        columns=["certificates_id", "value_int"],
        id_column="certificates_id",
    )
    recommended_for_rows = execute_query(
        cursor, recommended_for_query, certificates_ids
    )
    recommended_for_by_certificate_id: dict[int, list[int]] = {}
    for row in recommended_for_rows:
        recommended_for_by_certificate_id.setdefault(row[0], []).append(row[1])
    results: list[pydantic_records.Certificates] = []
    for row in certificates_rows:
        certificate_id = row[0]
        localized_rows_for_parent = localized_dict.get(certificate_id, [])
        localized_names: dict[str, str] = {}
        localized_descriptions: dict[str, str] = {}
        for localized_row in localized_rows_for_parent:
            localized_names[localized_row[1]] = localized_row[2]
            localized_descriptions[localized_row[1]] = localized_row[3]
        name = pydantic_records.LocalizedString(**localized_names)
        description = pydantic_records.LocalizedString(**localized_descriptions)
        skill_types_rows_for_certificate = skill_types_by_certificate_id.get(
            certificate_id, []
        )
        skill_types: dict[int, pydantic_records.Certificates_SkillType] | None = None
        for skill_type_row in skill_types_rows_for_certificate:
            if skill_types is None:
                skill_types = {}
            skill_types[skill_type_row[0]] = pydantic_records.Certificates_SkillType(
                basic=skill_type_row[2],
                standard=skill_type_row[3],
                improved=skill_type_row[4],
                advanced=skill_type_row[5],
                elite=skill_type_row[6],
            )
        results.append(
            pydantic_records.Certificates(
                certificates_id=certificate_id,
                groupID=row[1],
                name=name,
                description=description,
                skillTypes=skill_types if skill_types else {},
                recommendedFor=recommended_for_by_certificate_id.get(
                    certificate_id, []
                ),
            )
        )
    return results
