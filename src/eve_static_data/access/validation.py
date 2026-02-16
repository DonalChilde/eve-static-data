"""Code for validating SDE datasets against the TypedDict schema."""

from typing import Any

from pydantic import BaseModel, ValidationError

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.models.sde_datasets import SdeDatasets
from eve_static_data.models.sde_datasets_models import dataset_pydantic_model_lookup


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

    build_number: int
    release_date: str
    dataset_stats: dict[str, DatasetStats]


class DatasetValidator:
    def __init__(self, build_number: int, release_date: str) -> None:
        """Initialize the validator."""
        self.validation_result: SDEValidationResult = SDEValidationResult(
            build_number=build_number,
            release_date=release_date,
            dataset_stats={},
        )


def validate_dataset(access: SdeReader, dataset: SdeDatasets) -> DatasetStats:
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
