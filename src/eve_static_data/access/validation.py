"""Code for validating SDE datasets against the TypedDict schema."""

from pathlib import Path
from typing import Any

from pydantic import BaseModel, TypeAdapter, ValidationError

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models.sde_datasets import SdeDatasets
from eve_static_data.models.sde_datasets_models import (
    dataset_pydantic_model_lookup,
    dataset_td_model_lookup,
)


class DatasetValidationRecord(BaseModel):
    """A record of a validation error for a dataset."""

    record_number: int
    data: dict[str, Any]
    error_message: str


class DatasetStats(BaseModel):
    """Statistics about a dataset."""

    dataset_name: str
    total_records: int
    invalid_records: int
    validation_errors: list[DatasetValidationRecord]


class SDEValidationResult(BaseModel):
    """The result of validating an SDE dataset."""

    build_number: int | None = None
    release_date: str | None = None
    dataset_stats: dict[str, DatasetStats]


# class DatasetValidator:
#     def __init__(self, build_number: int | None, release_date: str | None) -> None:
#         """Initialize the validator."""
#         self.validation_result: SDEValidationResult = SDEValidationResult(
#             build_number=build_number,
#             release_date=release_date,
#             dataset_stats={},
#         )


def validate_dataset_pydantic(access: SdeReader, dataset: SdeDatasets) -> DatasetStats:
    """Validate a dataset against its pydantic model."""
    stats = DatasetStats(
        dataset_name=dataset.value,
        total_records=0,
        invalid_records=0,
        validation_errors=[],
    )
    model = dataset_pydantic_model_lookup(dataset)
    for record_number, record in enumerate(access.records(dataset), start=1):
        stats.total_records += 1
        try:
            # Validate the record against the pydantic model.
            _ = model.model_validate(record, extra="forbid")
        except ValidationError as e:
            stats.invalid_records += 1
            stats.validation_errors.append(
                DatasetValidationRecord(
                    record_number=record_number,
                    data=record,
                    error_message=str(e),
                )
            )
    return stats


def validate_dataset_typeddict(access: SdeReader, dataset: SdeDatasets) -> DatasetStats:
    """Validate a dataset against its TypedDict model."""
    stats = DatasetStats(
        dataset_name=dataset.value,
        total_records=0,
        invalid_records=0,
        validation_errors=[],
    )
    model = TypeAdapter(dataset_td_model_lookup(dataset))
    for record_number, record in enumerate(access.records(dataset), start=1):
        stats.total_records += 1
        try:
            # Validate the record against the TypedDict model.
            _ = model.validate_python(record, extra="forbid")
        except ValidationError as e:
            stats.invalid_records += 1
            stats.validation_errors.append(
                DatasetValidationRecord(
                    record_number=record_number,
                    data=record,
                    error_message=str(e),
                )
            )
    return stats


def validate_sde_pydantic(access: SdeReader) -> SDEValidationResult:
    """Validate all datasets in the SDE against their pydantic models."""
    validation_result = SDEValidationResult(
        build_number=access.build_number,
        release_date=access.release_date,
        dataset_stats={},
    )
    for dataset in SdeDatasets:
        validation_result.dataset_stats[dataset.value] = validate_dataset_pydantic(
            access, dataset
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


def check_for_dataset_files(sde_path: Path) -> FileCheckResult:
    """Check if the expected dataset files are present in the SDE path."""
    # missing_files: set[Path] = set()
    # extra_files: set[Path] = set()
    existing_files = set(p for p in sde_path.iterdir() if p.is_file())
    expected_files = set(sde_path / dataset.value for dataset in SdeDatasets)
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
