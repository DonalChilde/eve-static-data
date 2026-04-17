# Planned Refactors

- Remove pydantic localized datasets, as the localized records access will be through the sqlite database.
- Implement a sqlite database to store the sde data.
- each dataset's tables will be self contained, to make it easy to adjust for future sde changes.
- Data is loaded to the database from the pydantic records, but retrieved from the database as vanilla dataclasses.
- Database access functions for each record type, plus the localized records. Minimal filtering supported by the access function, like is_published.
- derived datasets, will become custom access functions, like meta_level. Maybe market path?. can be generated as table rows after database import. Some others like `def blueprints_manufacturing()` Maybe leave most of that to the user....
- pydantic code becomes focused on import from json, and validation. Can always use type adaptor with the dataclasses if we need serialization.

## Next!

- Write test functions to make a database, with some tbales, and load data. see how it flows.