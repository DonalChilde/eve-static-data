"""Module for reading EVE Online Static Data Export (SDE) files."""

import logging
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class SDERecordMetadata:
    dataset: SdeDatasetFiles
    file_path: Path
    record_number: int

    def __str__(self) -> str:
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
        record_count = 0
        for record in read_jsonl_dicts(file_path):
            record_count += 1
            metadata = SDERecordMetadata(
                dataset=dataset, file_path=file_path, record_number=record_count
            )
            yield record, metadata
        logger.info(
            f"Finished reading {dataset.value} {record_count} records from {file_path} in {perf_counter() - start:.4f} seconds."
        )

    def _parse_sde_info(self) -> None:
        """Try to parse the SDE info file to get the build number and release date."""
        sde_info_path = self.sde_path / self.sde_info_name
        if not sde_info_path.is_file():
            raise FileNotFoundError(f"SDE info file not found at {sde_info_path}")
        sde_info = read_jsonl_dicts(sde_info_path)
        if not sde_info:
            raise ValueError(f"SDE info file is empty at {sde_info_path}")
        sde_info_record = next(iter(sde_info))
        self.build_number = sde_info_record.get("buildNumber")
        self.release_date = sde_info_record.get("releaseDate")
