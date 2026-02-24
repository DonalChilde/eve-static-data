"""Code for validating SDE datasets against the TypedDict schema."""

import logging
from pathlib import Path
from typing import Any

from pydantic import BaseModel, TypeAdapter, ValidationError

from eve_static_data.access.sde_reader import SdeReader, SDERecordMetadata
from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk
from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles
from eve_static_data.models.datasets.sde_dataset_models import (
    dataset_pydantic_model_lookup,
    dataset_td_model_lookup,
)

logger = logging.getLogger(__name__)


class DatasetValidationRecord(BaseModel):
    """A record of a validation error for a dataset."""

    metadata: SDERecordMetadata
    data: dict[str, Any]
    error_message: str


class DatasetStats(BaseModel):
    """Statistics about a dataset."""

    dataset_name: str
    total_records: int
    invalid_records: int
    validation_errors: list[DatasetValidationRecord]


class SDEValidationResult(BaseModelToDisk):
    """The result of validating an SDE dataset."""

    build_number: int | None = None
    release_date: str | None = None
    dataset_stats: dict[str, DatasetStats] = {}


def validate_dataset_pydantic(
    access: SdeReader, dataset: SdeDatasetFiles
) -> DatasetStats:
    """Validate a dataset against its pydantic model."""
    stats = DatasetStats(
        dataset_name=dataset.value,
        total_records=0,
        invalid_records=0,
        validation_errors=[],
    )
    model = dataset_pydantic_model_lookup(dataset)
    for record, metadata in access.records(dataset):
        stats.total_records += 1
        try:
            # Validate the record against the pydantic model.
            _ = model.from_sde(record, metadata)
        except ValidationError as e:
            stats.invalid_records += 1
            stats.validation_errors.append(
                DatasetValidationRecord(
                    metadata=metadata,
                    data=record,
                    error_message=str(e),
                )
            )
    return stats


def validate_dataset_typeddict(
    reader: SdeReader, dataset: SdeDatasetFiles, file_name: str | None = None
) -> DatasetStats:
    """Validate a dataset against its TypedDict model."""
    stats = DatasetStats(
        dataset_name=dataset.value,
        total_records=0,
        invalid_records=0,
        validation_errors=[],
    )
    model = TypeAdapter(dataset_td_model_lookup(dataset))
    for record, metadata in reader.records(dataset, file_name=file_name):
        stats.total_records += 1
        try:
            # Validate the record against the TypedDict model.
            _ = model.validate_python(record, extra="forbid")
        except ValidationError as e:
            stats.invalid_records += 1
            stats.validation_errors.append(
                DatasetValidationRecord(
                    metadata=metadata,
                    data=record,
                    error_message=str(e),
                )
            )
    return stats


def validate_sde_pydantic(access: SdeReader) -> SDEValidationResult:
    """Validate all datasets in the SDE against their pydantic models."""
    logger.info("Starting SDE validation against pydantic models.")
    validation_result = SDEValidationResult(
        build_number=access.build_number,
        release_date=access.release_date,
        dataset_stats={},
    )
    for dataset in SdeDatasetFiles:
        validation_result.dataset_stats[dataset.value] = validate_dataset_pydantic(
            access, dataset
        )
    return validation_result


def validate_sde_typeddict(access: SdeReader) -> SDEValidationResult:
    """Validate all datasets in the SDE against their TypedDict models."""
    logger.info("Starting SDE validation against TypedDict models.")
    validation_result = SDEValidationResult(
        build_number=access.build_number,
        release_date=access.release_date,
        dataset_stats={},
    )
    for dataset in SdeDatasetFiles:
        validation_result.dataset_stats[dataset.value] = validate_dataset_typeddict(
            access, dataset
        )
    return validation_result


class FileCheckResult(BaseModelToDisk):
    """The result of checking for dataset files."""

    sde_path: Path
    existing_file_count: int
    existing_files: set[Path]
    expected_files: set[Path]
    missing_files: set[Path]
    extra_files: set[Path]


def check_for_dataset_files(sde_path: Path) -> FileCheckResult:
    """Check if the expected dataset files are present in the SDE path."""
    # missing_files: set[Path] = set()
    # extra_files: set[Path] = set()
    existing_files = set(p for p in sde_path.iterdir() if p.is_file())
    expected_files = set(sde_path / dataset.value for dataset in SdeDatasetFiles)
    # for existing_file in existing_files:
    #     if existing_file not in expected_files:
    #         extra_files.append(existing_file)
    # for expected_file in expected_files:
    #     if expected_file not in existing_files:
    #         missing_files.append(expected_file)

    return FileCheckResult(
        sde_path=sde_path,
        existing_file_count=len(existing_files),
        existing_files=existing_files,
        expected_files=expected_files,
        missing_files=expected_files - existing_files,
        extra_files=existing_files - expected_files,
    )
