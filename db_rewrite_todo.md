# DB Rewrite Todo

Rewrite sde access to focus on importing to and using a sqlite db for sde access. See written goals as well.

- Pydantic validation of loaded jsonl entries
  - No need for localized pydantic models.
- CLI support for online SDE.
  - Check for latest available sde version. 
  - Check online version against current version.
  - Download and display changelog.
  - Download sde.
- Validate downloaded sde schema.
  - Check all expected files are available. Callout missing or extra files.
  - Use pydantic to validate data structures in each file.
- Import sde to sqlite db.
- Offer export of jsonl to json.
- Offer display of jsonl data via terminal.
- Offer display of pydantic definitions of data structures? Could also be in docs....
- API for access to sde db.
- Export of some pre-defined constructs, like a spreadsheet friendly, localized, market types table, and a locations name table.
- CLI access to db? Complicated to offer 100% access... consider for future.
- Make a dev doc with complete instructions on how to update for release of new schema sde data.
- make a script to generate a test data set from sde data. Generated data should be repeatable when using same sde.
This data can be used for pytest validation of the pydantic models.
- Update usage docs.
- Docs to include detailed sde format information and explainations, links to sde webpages, etc.