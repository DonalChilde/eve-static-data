"""Generate schema reports from SDE dataset files."""

from collections.abc import Iterable
from pathlib import Path

from pfmsoft.eve_snippets import json_io, yaml_io

from pfmsoft.eve_sd.helpers.sde_metadata import load_sde_metadata
from pfmsoft.eve_sd.schema_inspection.models import SchemaReport
from pfmsoft.eve_sd.schema_inspection.report import DatasetInput, build_schema_report


def get_jsonl_schema_report(sde_directory: Path) -> SchemaReport:
    """Generate a schema report from all JSONL datasets in a directory."""
    sde_metadata = load_sde_metadata(sde_directory)

    def dataset_input_generator() -> Iterable[DatasetInput]:
        for dataset_file in sde_directory.glob("*.jsonl"):
            dataset_name = dataset_file.stem
            data = {x["_key"]: x for x in json_io.jsonl_load_path(dataset_file)}
            yield DatasetInput(
                dataset_name=dataset_name,
                dataset_data=data,
                sde_metadata=sde_metadata,
            )

    return build_schema_report(
        datasets=dataset_input_generator(),
        sde_metadata=sde_metadata,
        dataset_source=str(sde_directory),
    )


def get_yaml_schema_report(sde_directory: Path) -> SchemaReport:
    """Generate a schema report from all YAML datasets in a directory."""
    sde_metadata = load_sde_metadata(sde_directory)

    def dataset_input_generator() -> Iterable[DatasetInput]:
        for dataset_file in sde_directory.glob("*.yaml"):
            dataset_name = dataset_file.stem
            data = yaml_io.safe_load_path(dataset_file)
            yield DatasetInput(
                dataset_name=dataset_name,
                dataset_data=data,
                sde_metadata=sde_metadata,
            )

    return build_schema_report(
        datasets=dataset_input_generator(),
        sde_metadata=sde_metadata,
        dataset_source=str(sde_directory),
    )


def get_json_schema_report(sde_directory: Path) -> SchemaReport:
    """Generate a schema report from all JSON datasets in a directory.

    This is used when the original yaml or jsonl datasets have been converted
    to JSON dicts.
    """
    sde_metadata = load_sde_metadata(sde_directory)

    def dataset_input_generator() -> Iterable[DatasetInput]:
        for dataset_file in sde_directory.glob("*.json"):
            dataset_name = dataset_file.stem
            data = json_io.json_load_path(dataset_file)
            yield DatasetInput(
                dataset_name=dataset_name,
                dataset_data=data,
                sde_metadata=sde_metadata,
            )

    return build_schema_report(
        datasets=dataset_input_generator(),
        sde_metadata=sde_metadata,
        dataset_source=str(sde_directory),
    )
