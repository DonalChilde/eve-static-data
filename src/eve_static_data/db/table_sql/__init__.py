"""SDE database table definitions.

Column names match the field names in the SDE files as much as possible.
columns names original to the table, or that needed to be altered are snake case.

This ends up being confusing, but there is value in having matching names as much as possible.

the `_key` fields in the jsonl files become `key` in the dataclass, and `<dataset>_id`
in the database. Underscore fields in python carry a different meaning, and cause serialization
issues when used on pydantic BaseModels. Key is also a reserved word in sql.
"""
