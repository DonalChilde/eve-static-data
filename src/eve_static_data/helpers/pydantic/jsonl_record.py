"""Base class for records that can be read from a JSONL file."""

import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Protocol, Self, TypeVar

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)

BASE_MODELS = TypeVar("BASE_MODELS", bound=BaseModel)

# TODO abstract this out to a jsonl reader function that takes a transformer and returns
# an iterable of records. Provide a json transformer. Support pydantic transformers.
# Transformer should be able to skip records by returning None.
# transformer sig should be generic callable that takes an indexed string and returns an instance of the model or None.
# in examples show simple function, and callable class for more complex transformations.


class TransformerProtocol(Protocol):
    def transform(
        self, value: tuple[int, str], model: type[BASE_MODELS]
    ) -> BASE_MODELS | None:
        """Apply the transformation to an indexed string and return an instance of the model or None."""
        raise NotImplementedError(
            "TransformerProtocol.transform must be implemented by subclasses."
        )


class TransformBaseModel:
    """A class that provides a method to transform an indexed string into a pydantic BaseModel instance.

    The tranform method should return an instance of the model, or None if the record
    should be skipped.
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
    def transform(
        cls, file_path: str | Path, transformer: TransformerProtocol | None = None
    ) -> Iterable[tuple[int, Self | None]]:
        """Read a JSONL file and yield records as instances of this class.

        Args:
            file_path: The path to the JSONL file to read.
            transformer: An optional transformer to apply before processing each record.

        Yields:
            A tuple containing the line number of the source file, and an instance of
            this class representing a record from the JSONL file or None. If None is
            returned for a record, that signals that the transformer skipped the record.

        Raises:
            FileNotFoundError: If the file at file_path does not exist.
            ValidationError: If a line in the JSONL file cannot be parsed into an instance of this class.
            Exception: If an unexpected error occurs while reading the file or parsing a line.
        """
        if transformer is None:
            transformer = TransformBaseModel()
        with open(file_path, encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    record = transformer.transform((line_number, line), cls)
                    yield line_number, record
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
