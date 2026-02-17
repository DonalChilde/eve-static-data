# EVE Static Data Roadmap

EVE Static Data is a cli program used to download, validate, and export the EVE static dataset.

## Features

- [x] Check for the latest available version of the SDE, ref build number and release date.
- [x] Download and display the SDE schema changelog.
- [x] Download the SDE and save to file.
- [x] Generate and save a summary of the available fields in the datasets, used in TypedDict schema generation.
- [x] Offer a pydantic schema for the SDE.
- [x] Offer a TypedDict schema for the SDE.
- [x] Validate the SDE against a Pydantic schema.
  - [x] Create a Pydantic representaion of the SDE dataset.
  - [x] collect data on the validation status of the SDE
    - [x] display data in the terminal.
    - [x] Save validation data to a json file.
- [x] Provide an api to iterate over the jsonl records, loaded as TypedDicts.
- [x] Provide an api to iterate over the jsonl records, loaded as Pydantic models.
- [] Offer export of json data from pydantic models.
- [] Offer an export of localized SDE data as a pydantic backed set of JSON files.
  - [] Offer lazy loading dataset access api.
  - [] Include some derived datasets for convenience,
    - [] Market path
    - [] Location names - eg station names as displayed in game, asteroid belts names, etc.
    - [] Combined type data table for easy spreadsheet lookups.
  - [] Limited CSV export of some data as appropriate.

### In Progress

- Make a subset of data available for export, expand as needed.
  - Localized
  - Useful derived datasets
  - lazy loader

## Future possible features

- Sqlite database of full SDE
