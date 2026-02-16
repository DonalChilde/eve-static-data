# EVE Static Data Roadmap

EVE Static Data is a cli program used to download, validate, and export the EVE static dataset.

## Features

 - [x] Check for the latest available version of the SDE, ref build number and release date.
 - [x] Download and display the SDE schema changelog.
 - [x] Download the SDE and save to file.
 - [x] Generate and save a summary of the available fields in the datasets, used in TypedDict schema generation.
 - [] Offer a pydantic schema for the SDE.
 - [] Offer a TypedDict schema for the SDE.
 - [] Validate the SDE against a Pydantic schema.
   - [] Create a Pydantic representaion of the SDE dataset.
     - [] Note that some datasets can be marked as non validating, due to the complexity of the data.
   - [] collect data on the validation status of the SDE
     - [] display data in the terminal.
     - [] Save validation data to a json file.
     - [] Generate and save a text vlidation report.
 - [x] Provide an api to iterate over the jsonl records, loaded as TypedDicts.
 - [] Provide an api to iterate over the jsonl records, loaded as Pydantic models.
 - [] Offer export of json data from pydantic models.
 - [] Offer an export of localized SDE data as a pydantic backed set of JSON files.
   - [] Offer lazy loading dataset access api.
   - [] Include some derived datasets for convenience, 
     - [] Market path
     - [] Location names - eg station names as displayed in game, asteroid belts names, etc.
     - [] Combined type data table for easy spreadsheet lookups.
   - [] Limited CSV export of some data as appropriate.

### In Progress

- Validation
  - enhance the validation data collection data format.
    - use pydantic models to make it easy to save to json.
    - collect record counts per dataset.
    - collect build number and release date.
  - Define a list of non-validated datasets.
  - Functions to detect missing or additional datasets.


## Future possible features

- Sqlite database of full SDE