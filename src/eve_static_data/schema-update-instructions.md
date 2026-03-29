# Steps for updating the eve-static-data code with a new schema.

## Download and validate the new SDE dataset.

## New dataset.

- reference the textual report, check for new dataset files.
- Reference the new file type def in sde_type_sig.json
- Add a new model to models.pydantic.records
- Add file-to-model lookup entry in models.pydantic.records
- Add a new model to models.pydantic.datasets
- Add file-to-model lookup entry in models.pydantic.datasets
- Add an entry to models.dataset_filenames.SdeDatasetFiles
- Add access function, and loader entry in access.sde_datasets  

- If a localizable record, 
  - add model to models.pydantic.localized.records
  - add file-to-model lookup entry
  - add model to models.pydantic.localized_datasets
  - add file-to-model lookup entry
  - add access function and loader function in access.sde_datasets

- rerun validation report and check for errors
- update AFTER_BUILD_NUMBER and RELEASE_DATE IN `__init__.py` using values from schema_changelog.yaml
