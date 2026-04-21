# Planned Refactors


- Implement a sqlite database to store the sde data.
- each dataset's tables will be self contained, to make it easy to adjust for future sde changes.
- Data is loaded to the database from the pydantic records, but retrieved from the database as vanilla dataclasses.
- Database access functions for each record type, plus the localized records. Minimal filtering supported by the access function, like is_published.
- derived datasets, will become custom access functions, like meta_level. Maybe market path?. can be generated as table rows after database import. Some others like `def blueprints_manufacturing()` Maybe leave most of that to the user....
- pydantic code becomes focused on import from json, and validation. Can always use type adaptor with the dataclasses if we need serialization.



## Next!

- yaml sde now primary SDE source.
- Two data sources for access, one a database, the other yaml-to-json files.
- Offer a cli bulk yaml to json command
- Access offers loader
  - take directory
  - functions access by dataset name, discovers and loads yaml/json.
  - access has same interface with file based and database backing.
  - Loads from file with root loader, delivers Dataset
- Do yaml-to-json file based access first, then finish database.
- For simplicity, The common interface between database and file based access will be limited to mostly full dataset loads. the exceptions will be is_published, and localized data. When implememted, the database will offer more filtered loading, like subsets.
- derived datasets are pulled from database. not a thing for full dataset loads.
- app does not store sde data, as cli interface works just fine when provided an sde directory, and the api can be called with any directory.