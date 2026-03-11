"""Code for validating SDE datasets against the TypedDict schema."""

import json
import logging
from pathlib import Path
from time import perf_counter

from pydantic import BaseModel

from eve_static_data.helpers.jsonl_reader import read_jsonl_file
from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk
from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic.records import LOOKUP as pydantic_model_lookup
from eve_static_data.sde_type_sigs import get_sde_type_sigs
from eve_static_data.transformers import ModelLoader, ModelValidationErrorRecord

logger = logging.getLogger(__name__)


class DatasetStats(BaseModel):
    """Statistics about a dataset."""

    dataset_name: str
    model_name: str
    file_path: Path
    total_records: int
    invalid_records: int
    error_records: dict[int, ModelValidationErrorRecord]
    published_records_with_errors: list[int] = []
    line_record_not_published: set[int]


class SDEValidationResult(BaseModelToDisk):
    """The result of validating an SDE dataset."""

    build_number: int | None = None
    release_date: str | None = None
    dataset_stats: dict[str, DatasetStats] = {}


def validate_dataset_records(
    input_path: Path, dataset: SdeDatasetFiles
) -> DatasetStats:
    """Validate a dataset against its pydantic model."""
    file_path = input_path / dataset.as_jsonl()
    model = pydantic_model_lookup.get(dataset, None)
    stats = DatasetStats(
        dataset_name=dataset.value,
        model_name=model.__name__ if model is not None else "None",
        file_path=file_path,
        total_records=0,
        invalid_records=0,
        error_records={},
        line_record_not_published=set(),
        published_records_with_errors=[],
    )

    if model is None:
        msg = (
            f"No pydantic model found for dataset {dataset.value}, skipping validation."
        )
        logger.warning(msg)
        stats.invalid_records += 1
        stats.error_records[0] = ModelValidationErrorRecord(
            model="NONE",
            line_number=0,
            data="",
            error_messages=[msg],
        )
        return stats
    transformer = ModelLoader(
        model=model, only_published=False, skip_validation_failures=True
    )
    for index, record in read_jsonl_file(file_path, transformer=transformer):
        stats.total_records = index
        if record is None:
            stats.invalid_records += 1
    stats.error_records = transformer.validation_errors
    stats.line_record_not_published = transformer.line_record_not_published
    stats.published_records_with_errors = list(
        set(stats.error_records.keys()) - stats.line_record_not_published
    )

    return stats


def validate_sde_datasets(input_path: Path) -> SDEValidationResult:
    """Validate all datasets in the SDE against their pydantic models."""
    logger.info("Starting SDE validation against pydantic models.")
    sde_info = load_sde_info(input_path)
    validation_result = SDEValidationResult(
        build_number=sde_info["buildNumber"],
        release_date=sde_info["releaseDate"],
        dataset_stats={},
    )
    for dataset in SdeDatasetFiles:
        validation_result.dataset_stats[dataset.value] = validate_dataset_records(
            input_path, dataset
        )
    return validation_result


class FileCheckResult(BaseModel):
    """The result of checking for dataset files."""

    sde_path: Path
    existing_file_count: int
    existing_files: set[Path]
    expected_files: set[Path]
    missing_files: set[Path]
    extra_files: set[Path]


def check_for_dataset_files(input_path: Path) -> FileCheckResult:
    """Check if the expected dataset files are present in the SDE path."""
    existing_files = set(p for p in input_path.iterdir() if p.is_file())
    expected_files = set(input_path / dataset.as_jsonl() for dataset in SdeDatasetFiles)
    return FileCheckResult(
        sde_path=input_path,
        existing_file_count=len(existing_files),
        existing_files=existing_files,
        expected_files=expected_files,
        missing_files=expected_files - existing_files,
        extra_files=existing_files - expected_files,
    )


def validate_and_save_results(input_path: Path, output_path: Path) -> None:
    """Validate the SDE datasets and save the results to disk.

    This will perform the following validations:
    - Check for the presence of expected dataset files and report any missing or extra files.
    - Validate the records in each dataset against their corresponding pydantic models
        and report any validation errors.
    - Generate type signature information for all the JSONL files in the input_path directory.
    """
    sde_info = load_sde_info(input_path)
    logger.info(
        f"Validating SDE datasets for build {sde_info['buildNumber']} and saving results to {output_path}"
    )

    start = perf_counter()

    # Generate and save type signature definitions for the SDE datasets.
    sde_sigs = get_sde_type_sigs(
        input_path=input_path, build_number=str(sde_info["buildNumber"])
    )
    output_file = output_path / f"sde_type_sig-{sde_info['buildNumber']}.json"
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(sde_sigs, f, indent=2, sort_keys=True)
    logger.info(
        f"SDE type signature definitions saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
    )

    # Check for expected dataset files and save results.
    file_check_result = check_for_dataset_files(input_path)
    output_file = output_path / f"dataset_file_check_{sde_info['buildNumber']}.json"
    with output_file.open("w", encoding="utf-8") as f:
        f.write(file_check_result.model_dump_json(indent=2))
    logger.info(
        f"Dataset file check results saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
    )

    # Validate datasets against pydantic models and save results.
    pydantic_validation_result = validate_sde_datasets(input_path)
    output_file = (
        output_path
        / f"pydantic_model_validation_{pydantic_validation_result.build_number}.json"
    )
    pydantic_validation_result.save_to_disk(output_file)
    logger.info(
        f"SDE pydantic model validation results saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
    )

    logger.info(
        f"Finished validating SDE datasets and saving results to {output_path} in {perf_counter() - start:.4f} seconds."
    )
