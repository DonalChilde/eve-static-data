"""Code for validating SDE datasets against the TypedDict schema."""

from typing import Any

from pydantic import BaseModel, ValidationError


class DatasetValidationRecord(BaseModel):
    """A record of a validation error for a dataset."""

    dataset_name: str
    data: dict[str, Any]
    error_message: str


class DatasetStats(BaseModel):
    """Statistics about a dataset."""

    dataset_name: str
    build_number: int
    release_date: str
    total_records: int
    invalid_records: int
    validation_errors: list[DatasetValidationRecord]


class SDEValidationResult(BaseModel):
    """The result of validating an SDE dataset."""

    build_number: int
    release_date: str
    dataset_stats: dict[str, DatasetStats]
