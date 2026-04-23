from eve_static_data.models import yaml_datasets, yaml_records
from eve_static_data.models.dataset_filenames import SdeDatasetFiles
# TODO write code to validate SDE YAML datasets against the yaml datamodel.

# Validation should report on:
# - files present/missing in the SDE directory, compared to the expected file represented by SdeDatasetFiles
# - the flavor of dataset file - yaml or json (json is exported from the original yaml file, this might happen pre-validation) validation should accept both sources.
# - load the dataset file via json.load or yaml.safe_load as appropriate.
#    - the resulting object should be a dict.
#    - iterate through the dict and validate individual records against the RootModels found in yaml_datasets.
#    - report failed records with SdeDatasetFile, top level key, and error messages.
# - validation creates a dict of information that can be used to create a markdown report of results. Both the dict, and the markdown report should be saved to disc.
