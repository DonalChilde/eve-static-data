"""Base class for records that can be read from a JSONL file."""

import json
import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Any, Self

from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)


class JsonlRecord(BaseModel):
    """Base class for records that can be read from a JSONL file."""

    @classmethod
    def dicts_from_jsonl_file(
        cls, file_path: str | Path, encoding: str = "utf-8"
    ) -> Iterable[tuple[dict[str, Any], int]]:
        """Read a JSONL file and yield records as dictionaries, along with their line number.

        Args:
            file_path: The path to the JSONL file to read.
            encoding: The encoding of the JSONL file (default is "utf-8").

        Yields:
            A tuple containing a dictionary representing a record from the
                JSONL file, and the line number of the record in the file (starting from 1).

        Raises:
            FileNotFoundError: If the file at file_path does not exist.
            JSONDecodeError: If a line in the JSONL file cannot be parsed as JSON.
            Exception: If an unexpected error occurs while reading the file or parsing a line.
        """
        with open(file_path, encoding=encoding) as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    record_dict = json.loads(line)
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
    def from_jsonl_file(
        cls, file_path: str | Path, encoding: str = "utf-8"
    ) -> Iterable[tuple[Self, int]]:
        """Read a JSONL file and yield records as instances of this class, along with their line number.

        Args:
            file_path: The path to the JSONL file to read.
            encoding: The encoding of the JSONL file (default is "utf-8").

        Yields:
            A tuple containing an instance of this class representing a record from the
                JSONL file, and the line number of the record in the file (starting from 1).

        Raises:
            FileNotFoundError: If the file at file_path does not exist.
            ValidationError: If a line in the JSONL file cannot be parsed into an instance of this class.
            Exception: If an unexpected error occurs while reading the file or parsing a line.



        """
        with open(file_path, encoding=encoding) as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    record = cls.model_validate_json(line)
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
