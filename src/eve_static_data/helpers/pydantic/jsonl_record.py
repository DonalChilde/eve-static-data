"""Base class for records that can be read from a JSONL file."""

import json
import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Any, Self, TypeVar

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

BASE_MODELS = TypeVar("BASE_MODELS", bound=BaseModel)


class TransformJsonDict:
    """A class that prvides a method to transform an indexed string into a json dict.

    The tranform method should return a dictionary, or None if the record should be skipped.
    """

    def __init__(self):
        """Initialize the class."""

    def transform(self, value: tuple[int, str]) -> dict[str, Any] | None:
        """Apply the transformation to an indexed string."""
        _, text = value
        return json.loads(text)


class TransformBaseModel:
    """A class that provides a method to transform an indexed string into a pydantic BaseModel instance.

    The tranform method should return an instance of the model, or None if the record should be skipped.
    """

    def __init__(self):
        """Initialize the class."""

    def transform(
        self, value: tuple[int, str], model: type[BASE_MODELS]
    ) -> BASE_MODELS | None:
        """Apply the transformation to an indexed string."""
        _, text = value
        return model.model_validate_json(text)


class JsonlRecord(BaseModel):
    """Base class for records that can be read from a JSONL file."""

    @classmethod
    def lines_as_dict(
        cls,
        file_path: str | Path,
        *,
        transformer: TransformJsonDict | None = None,
        encoding: str = "utf-8",
    ) -> Iterable[tuple[dict[str, Any], int]]:
        """Read a JSONL file and yield records as dictionaries, along with their line number.

        The transformer can be used to apply a transformation to the raw text of each
        line before it is parsed as JSON. If no transformer is provided, the default
        behavior is to parse each line as JSON without any transformation.

        Args:
            file_path: The path to the JSONL file to read.
            encoding: The encoding of the JSONL file (default is "utf-8").
            transformer: An optional transformer to apply before processing each record.

        Yields:
            A tuple containing a dictionary representing a record from the
                JSONL file, and the line number of the record in the file (starting from 1).

        Raises:
            FileNotFoundError: If the file at file_path does not exist.
            JSONDecodeError: If a line in the JSONL file cannot be parsed as JSON.
            Exception: If an unexpected error occurs while reading the file or parsing a line.
        """
        if transformer is None:
            transformer = TransformJsonDict()
        with open(file_path, encoding=encoding) as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    record_dict = transformer.transform((line_number, line))
                    if record_dict is None:
                        continue
                except json.JSONDecodeError as e:
                    logger.exception(
                        "Error parsing line %d: %s as json in class %s For file %s",
                        line_number,
                        e,
                        cls.__name__,
                        file_path,
                    )
                    raise e
                except Exception as e:
                    logger.exception(
                        "Unexpected error parsing line %d: %s as json in class %s For file %s",
                        line_number,
                        e,
                        cls.__name__,
                        file_path,
                    )
                    raise e
                yield record_dict, line_number

    @classmethod
    def lines_as_model(
        cls,
        file_path: str | Path,
        *,
        transformer: TransformBaseModel | None = None,
        encoding: str = "utf-8",
    ) -> Iterable[tuple[Self, int]]:
        """Read a JSONL file and yield records as instances of this class, along with their line number.

        Args:
            file_path: The path to the JSONL file to read.
            encoding: The encoding of the JSONL file (default is "utf-8").
            transformer: An optional transformer to apply before processing each record.

        Yields:
            A tuple containing an instance of this class representing a record from the
                JSONL file, and the line number of the record in the file (starting from 1).

        Raises:
            FileNotFoundError: If the file at file_path does not exist.
            ValidationError: If a line in the JSONL file cannot be parsed into an instance of this class.
            Exception: If an unexpected error occurs while reading the file or parsing a line.



        """
        if transformer is None:
            transformer = TransformBaseModel()
        with open(file_path, encoding=encoding) as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    record = transformer.transform((line_number, line), cls)
                    if record is None:
                        continue
                except ValidationError as e:
                    logger.exception(
                        "Error parsing line %d: %s as %s For file %s",
                        line_number,
                        e,
                        cls.__name__,
                        file_path,
                    )
                    raise e
                except Exception as e:
                    logger.exception(
                        "Unexpected error parsing line %d: %s as %s For file %s",
                        line_number,
                        e,
                        cls.__name__,
                        file_path,
                    )
                    raise e
                yield record, line_number
