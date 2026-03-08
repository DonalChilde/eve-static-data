"""Implementation of the ESD protocols."""

import json
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Literal

from multidict import CIMultiDictProxy

from eve_static_data.helpers.aiohttp.download_files import download_bytes_to_file
from eve_static_data.protocols import ESDToolsProtocol


class EsdTools(ESDToolsProtocol):
    """Class for handling ESD tools static data."""

    def __init__(
        self,
        download_url_template: str = "https://developers.eveonline.com/static-data/tranquility/eve-online-static-data-${build_number}-${variant}.zip",
    ):
        """The EsdTools class for handling ESD tools static data."""
        self.download_url_template = download_url_template

    async def download(
        self,
        build_number: int,
        variant: Literal["jsonl", "yaml"],
        output_path: Path,
        overwrite: bool = False,
    ) -> CIMultiDictProxy[str]:
        """Download the ESD tools static data."""
        url = self.download_url_template.format(
            build_number=build_number, variant=variant
        )
        headers = await download_bytes_to_file(
            url=url, file_path=output_path, overwrite=overwrite
        )
        return headers

    def unpack(self, input_path: Path, output_path: Path) -> None:
        """Unpack the EVE static data."""
        with TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(input_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
            sde_info = Path(temp_dir) / "_sde.jsonl"
            if not sde_info.exists():
                raise FileNotFoundError(
                    f"_sde.jsonl file not found in the unzipped SDE data at {temp_dir}. Is this a valid SDE zip file?"
                )
            # There should only be one record in the _sde.jsonl file, but we'll read it as a list just in case
            sde_info_data = json.loads(sde_info.read_text(encoding="utf-8"))
            build_number = sde_info_data.get("build_number")
            if build_number is None:
                raise ValueError(
                    f"Build number not found in _sde.jsonl file at {sde_info}. Is this a valid SDE zip file?"
                )
            output_build_dir = output_path / str(build_number)
            output_build_dir.mkdir(parents=True, exist_ok=True)
            for item in Path(temp_dir).iterdir():
                if item.is_file():
                    item.rename(output_build_dir / item.name)

    def validate(self, input_path: Path, output_path: Path) -> bool:
        """Validate the ESD tools static data."""
        ...

    def derive(self, input_path: Path, output_path: Path) -> None:
        """Derive additional ESD tools static data from the original data."""
        ...

    def esd_import(self, input_path: Path) -> None:
        """Prepare the ESD tools static data for use.

        Args:
            input_path: The path to the static data jsonl zip file.
        """
        ...
