from collections.abc import Iterable
from pathlib import Path
from typing import Any

from eve_static_data.helpers.jsonl_reader import read_jsonl_dicts
from eve_static_data.models.sde_datasets import SdeDatasets


class SdeReader:
    def __init__(self, sde_path: Path) -> None:
        self.sde_path = sde_path

    def records(self, dataset: SdeDatasets) -> Iterable[dict[str, Any]]:
        file_path = self.sde_path / dataset.value
        return read_jsonl_dicts(file_path)
