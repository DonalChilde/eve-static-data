import logging
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

logger = logging.getLogger(__name__)


class SdeReader:
    def __init__(self, sde_path: Path) -> None:
        self.sde_path = sde_path
        self.sde_info_name = "_sde.jsonl"
        self.build_number: int | None = None
        self.release_date: str | None = None
        try:
            self.parse_sde_info()
        except Exception as e:
            logger.error(f"Error parsing SDE info: {e}")
            pass

    def records(self, dataset: SdeDatasetFiles) -> Iterable[dict[str, Any]]:
        """Yield records from the specified dataset."""
        file_path = self.sde_path / dataset.value
        return read_jsonl_dicts(file_path)

    def parse_sde_info(self) -> None:
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
