# NOTE these tests use a deprecated insert_records module that is being replaced by a new
# insert_generation module. The tests will be deleted once the new module is fully
# implemented and tested. They are left as an example, the decision to reimplement similar
# tests for the new module will be made once the new module is further along in development.


# """Tests for SQLite insert helpers."""

# import sqlite3
# from pathlib import Path

# from eve_static_data.db.insert_records import blueprints
# from eve_static_data.models.pydantic import records as pydantic_records


# def _blueprints_schema() -> str:
#     """Return the SQL schema used by the blueprint insert helper."""
#     # FIXME use importlib.resources to load this from src/eve_static_data/db/table_sql/blueprints.sql instead of hardcoding it here
#     repo_root = Path(__file__).resolve().parents[3]
#     return (
#         repo_root / "src" / "eve_static_data" / "db" / "table_sql" / "blueprints.sql"
#     ).read_text(encoding="utf-8")


# def test_blueprints_insert_writes_parent_and_activity_rows() -> None:
#     """Blueprint inserts should create parent, activity, and child rows."""
#     connection = sqlite3.connect(":memory:")
#     connection.executescript(_blueprints_schema())

#     record = pydantic_records.Blueprints(
#         _key=1001,
#         blueprintTypeID=2002,
#         maxProductionLimit=3003,
#         activities={
#             "manufacturing": {
#                 "time": 60,
#                 "materials": [
#                     {"typeID": 34, "quantity": 5},
#                     {"typeID": 35, "quantity": 7},
#                 ],
#                 "products": [
#                     {"typeID": 36, "quantity": 1, "probability": None},
#                 ],
#                 "skills": [
#                     {"typeID": 3380, "level": 4},
#                 ],
#             },
#             "copying": {
#                 "time": 120,
#             },
#         },
#     )

#     blueprints(connection, [record])

#     assert connection.execute(
#         "SELECT blueprints_id, blueprintTypeID, maxProductionLimit FROM blueprints"
#     ).fetchall() == [(1001, 2002, 3003)]
#     assert connection.execute(
#         "SELECT blueprint_id, activity_type, activity_time FROM blueprint_activities ORDER BY activity_type"
#     ).fetchall() == [(1001, "copying", 120), (1001, "manufacturing", 60)]
#     assert connection.execute(
#         "SELECT typeID, quantity FROM blueprint_activity_materials ORDER BY typeID"
#     ).fetchall() == [(34, 5), (35, 7)]
#     assert connection.execute(
#         "SELECT typeID, skill_level FROM blueprint_activity_skills"
#     ).fetchall() == [(3380, 4)]
#     assert connection.execute(
#         "SELECT typeID, quantity, probability FROM blueprint_activity_products"
#     ).fetchall() == [(36, 1, None)]


# def test_blueprints_insert_skips_empty_optional_child_lists() -> None:
#     """Activities without optional child collections should not create child rows."""
#     connection = sqlite3.connect(":memory:")
#     connection.executescript(_blueprints_schema())

#     record = pydantic_records.Blueprints(
#         _key=4004,
#         blueprintTypeID=5005,
#         maxProductionLimit=6006,
#         activities={
#             "research_time": {
#                 "time": 30,
#             },
#         },
#     )

#     blueprints(connection, [record])

#     assert connection.execute(
#         "SELECT blueprint_id, activity_type, activity_time FROM blueprint_activities"
#     ).fetchall() == [(4004, "research_time", 30)]
#     assert connection.execute(
#         "SELECT COUNT(*) FROM blueprint_activity_materials"
#     ).fetchone() == (0,)
#     assert connection.execute(
#         "SELECT COUNT(*) FROM blueprint_activity_skills"
#     ).fetchone() == (0,)
#     assert connection.execute(
#         "SELECT COUNT(*) FROM blueprint_activity_products"
#     ).fetchone() == (0,)
