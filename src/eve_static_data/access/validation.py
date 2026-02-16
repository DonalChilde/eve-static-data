"""Code for validating SDE datasets against the TypedDict schema."""

from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

import eve_static_data.models.raw_pydantic as PM
from eve_static_data.access.raw_json_protocol import RawJsonProtocol


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


def agents_in_space(access: RawJsonProtocol) -> DatasetStats:
    """Validate the agentsInSpace dataset."""
    stats = DatasetStats(
        dataset_name="agentsInSpace",
        total_records=0,
        invalid_records=0,
        validation_errors=[],
    )
    for record_number, record in enumerate(access.agents_in_space(), start=1):
        stats.total_records += 1
        try:
            # Validate the record against the pydantic model.
            _ = PM.AgentsInSpace.model_validate(record, extra="forbid")
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


# TODO test this validation code and add validation methods for the other datasets.
# Check if _key vs key is an issue in the pydantic models, and if so,
# add a pre-processing step to rename _key to key before validation. or
# update the pydantic models to accept both _key and key.
