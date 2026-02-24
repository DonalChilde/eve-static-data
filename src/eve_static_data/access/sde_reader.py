"""Module for reading EVE Online Static Data Export (SDE) files."""

import logging
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts
from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles

logger = logging.getLogger(__name__)

# FIXME: Error handling when data is missing or malformed.


@dataclass(slots=True)
class SDERecordMetadata:
    dataset: SdeDatasetFiles
    file_path: Path
    record_number: int

    def __str__(self) -> str:
        """Return a string representation of the SDE record metadata."""
        return f"{self.dataset.value} record {self.record_number} in {self.file_path}"


class SdeReader:
    def __init__(self, sde_path: Path, sde_info_name: str = "_sde.jsonl") -> None:
        """Initialize the SDE reader with the path to the SDE data and optionally the name of the SDE info file.

        Args:
            sde_path (Path): The path to the directory containing the SDE JSONL files.
            sde_info_name (str): The name of the SDE info file (default is "_sde.jsonl").
        """
        self.sde_path = sde_path
        self.sde_info_name = sde_info_name
        self.build_number: int | None = None
        self.release_date: str | None = None
        try:
            self._parse_sde_info()
        except Exception as e:
            logger.error(f"Error parsing SDE info: {e}")
            pass

    def records(
        self, dataset: SdeDatasetFiles, file_name: str | None = None
    ) -> Iterable[tuple[dict[str, Any], SDERecordMetadata]]:
        """Yield records from the specified dataset."""
        if file_name:
            file_path = self.sde_path / file_name
        else:
            file_path = self.sde_path / dataset.value
        start = perf_counter()
        index = 0
        for record, index in read_jsonl_dicts(file_path):
            metadata = SDERecordMetadata(
                dataset=dataset, file_path=file_path, record_number=index
            )
            yield record, metadata
        logger.info(
            f"Finished reading {dataset.value} {index} records from {file_path} in {perf_counter() - start:.4f} seconds."
        )

    def record_at(
        self, dataset: SdeDatasetFiles, index: int, file_name: str | None = None
    ) -> tuple[dict[str, Any], SDERecordMetadata]:
        """Return the record at the specified index from the specified dataset.

        Indexes are line numbers in the JSONL file, starting at 1. If the index is out of range, an IndexError is raised.
        """
        if file_name:
            file_path = self.sde_path / file_name
        else:
            file_path = self.sde_path / dataset.value
        start = perf_counter()
        line_number = 0
        for record, line_number in read_jsonl_dicts(file_path):
            if line_number == index:
                metadata = SDERecordMetadata(
                    dataset=dataset, file_path=file_path, record_number=line_number
                )
                logger.info(
                    f"Finished reading {dataset.value} record {index} of {line_number} from {file_path} in {perf_counter() - start:.4f} seconds."
                )
                return record, metadata
        raise IndexError(
            f"Index {index} of {line_number} out of range for dataset {dataset.value} in file {file_path}"
        )

    def _parse_sde_info(self) -> None:
        """Try to parse the SDE info file to get the build number and release date."""
        sde_info_path = self.sde_path / self.sde_info_name
        if not sde_info_path.is_file():
            raise FileNotFoundError(f"SDE info file not found at {sde_info_path}")
        data, metadata = self.record_at(
            dataset=SdeDatasetFiles.SDE_INFO, index=1, file_name=self.sde_info_name
        )
        _ = metadata
        self.build_number = data.get("buildNumber")  # type: ignore
        self.release_date = data.get("releaseDate")  # type: ignore
