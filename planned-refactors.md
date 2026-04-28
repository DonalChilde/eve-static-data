# Planned Refactors

## NOW

### FIXME
- unpack forces a check for _sde.jsonl, this should be more flexible.

### Add
- functions to detect and load all the _sde variants, used to get buildNumber etc, and to be a quick check that the SDE data exists.



## Next!

### jsonl based validation
- Fully implement jsonl based validation using the current report structure.
- Refactor to use the current yaml record format, localized field access. `_key` field solutions? Dont try to hard to force out pydantic classes, the yaml solution is superior.
- make an access loader?

### Implement a sqlite database to store the sde data.
- each dataset's tables will be self contained, to make it easy to adjust for future sde changes.
- Data is loaded to the database from the pydantic records, but retrieved from the database as vanilla dataclasses.
- Database access functions for each record type, plus the localized records. Minimal filtering supported by the access function, like is_published.
- offer a limited number of derived data function calls.


