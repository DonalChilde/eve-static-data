"""Implementation of the ESDTools protocol."""

import logging
import shutil
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any, Literal, cast

from yaml import safe_load

from eve_static_data import network
from eve_static_data.derive_datasets import generate_derived_datasets
from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.type_defs import Lang
from eve_static_data.protocols import ESDToolsProtocol
from eve_static_data.validation import validate_and_save_results

logger = logging.getLogger(__name__)


class EsdTools(ESDToolsProtocol):
    """Class for handling ESD tools static data."""

    def __init__(
        self,
        sde_url_template: str = network.SDE_URL_TEMPLATE,
        data_changes_url_template: str = network.DATA_CHANGES_URL_TEMPLATE,
        schema_changelog_url: str = network.SCHEMA_CHANGELOG_URL,
        latest_info_url: str = network.LATEST_INFO_URL,
    ):
        """The EsdTools class for handling ESD tools static data."""
        self.sde_url_template = sde_url_template
        self.data_changes_url_template = data_changes_url_template
        self.schema_changelog_url = schema_changelog_url
        self.latest_info_url = latest_info_url

    async def download(
        self,
        build_number: int,
        output_path: Path,
        variant: Literal["jsonl", "yaml"] = "jsonl",
        overwrite: bool = False,
    ) -> Path:
        """Download the ESD tools static data."""
        response_headers = await network.download_sde_to_file(
            build_number=build_number,
            output_path=output_path,
            url_template_str=self.sde_url_template,
            variant=variant,
            overwrite=overwrite,
        )
        return response_headers

    def unpack(
        self, input_path: Path, output_path: Path, build_number: int | None
    ) -> Path:
        """Unpack the static data.

        Unzip the input file and save the unpacked data to the output path.
        If a build number is provided, save the unpacked data to <output_path>/<build_number>/sde/.

        Checks for the presence of the _sde.jsonl file in the unpacked files. If the file is not
        found, raises a FileNotFoundError.

        If build number is provided, checks that the build number in the _sde.jsonl
        file matches the provided build number. If it does not match, raises a ValueError.

        Args:
            input_path: The path to the static data jsonl zip file.
            output_path: The path to the directory where the unpacked data should be saved.
            build_number: The build number of the static data.

        """
        if not input_path.is_file():
            raise FileNotFoundError(f"Input path {input_path} is not a file.")
        if input_path.suffix != ".zip":
            raise ValueError(f"Input file {input_path} is not a zip file.")
        with TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(input_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
            sde_info_file = Path(temp_dir) / "_sde.jsonl"
            if not sde_info_file.exists():
                raise FileNotFoundError(
                    f"_sde.jsonl file not found in the unzipped SDE data at {temp_dir}. Is this a valid SDE zip file?"
                )
            # There should only be one record in the _sde.jsonl file, but we'll read it as a list just in case
            sde_info_data = load_sde_info(Path(temp_dir))
            if (
                build_number is not None
                and sde_info_data.get("buildNumber") != build_number
            ):
                raise ValueError(
                    f"Build number in _sde.jsonl file ({sde_info_data.get('buildNumber')}) does not match the expected build number ({build_number}). Is this a valid SDE zip file?"
                )
            if build_number is None:
                output_dir = output_path
            else:
                output_dir = output_path / str(build_number) / "sde"
            output_dir.mkdir(parents=True, exist_ok=True)
            for file in Path(temp_dir).iterdir():
                if file.is_file():
                    target_file = output_dir / file.name
                    if target_file.exists():
                        raise FileExistsError(
                            f"Target file {target_file} already exists. Cannot move processed data to {target_file}"
                        )
                    shutil.move(file, target_file)
            return output_dir

    async def validate(
        self, input_path: Path, output_path: Path, build_number: int | None = None
    ) -> None:
        """Validate the ESD tools static data."""
        sde_info = load_sde_info(input_path)
        if build_number is not None and sde_info.get("buildNumber") != build_number:
            raise ValueError(
                f"Build number in _sde.jsonl file ({sde_info.get('buildNumber')}) does "
                f"not match the expected build number ({build_number}). Is this a valid SDE zip file?"
            )
        if build_number is not None:
            output_dir = output_path / str(build_number) / "validation"
        else:
            output_dir = output_path
            build_number = sde_info.get("buildNumber")
        output_dir.mkdir(parents=True, exist_ok=True)

        validate_and_save_results(input_path=input_path, output_path=output_dir)
        await self.schema_changelog(build_number=build_number, output_path=output_dir)
        await self.data_changes(build_number=build_number, output_path=output_dir)

    def derive(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int | None = None,
        lang: Lang = "en",
    ) -> None:
        """Derive additional ESD tools static data from the original data."""
        sde_info = load_sde_info(input_path)
        if build_number is not None and sde_info.get("buildNumber") != build_number:
            raise ValueError(
                f"Build number in _sde.jsonl file ({sde_info.get('buildNumber')}) does "
                f"not match the expected build number ({build_number}). Is this a valid SDE zip file?"
            )
        if build_number is not None:
            output_dir = output_path / str(build_number) / "derived"
        else:
            output_dir = output_path
        output_dir.mkdir(parents=True, exist_ok=True)
        generate_derived_datasets(
            input_path=input_path, output_path=output_dir, lang=lang
        )

    async def data_changes(
        self, build_number: int, output_path: Path | None = None
    ) -> list[str]:
        """Download the sde data changes for the given build number.

        Raises a ValueError if the changes are not available for the given build number.

        Raises a ValueError if a file exists at the output path with the same name as the changelog file.

        The changes file is named "sde_data_changes-<build_number>.jsonl" and is
        saved to the <output_path> directory if an output path is provided.

        Args:
            build_number: The build number of the static data.
            output_path: The path to the directory where the changelog should be saved.
                If None, the changelog will not be saved to disk.

        Returns:
            A list of strings representing the sde data changes.
        """
        if output_path is not None and output_path.is_file():
            raise FileExistsError(
                f"Output path {output_path} is a file. Please provide a directory path or set output_path to None."
            )

        text = await network.get_sde_data_changes(
            build_number=build_number, url_template=self.data_changes_url_template
        )
        changes = text.splitlines()
        if output_path:
            output_file = output_path / f"changes-{build_number}.jsonl"
            if output_file.exists():
                raise FileExistsError(
                    f"Data changes file {output_file} already exists. Please remove the existing file or choose a different output path."
                )
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(text)
        return changes

    async def schema_changelog(
        self, build_number: int, output_path: Path | None = None
    ) -> dict[str, Any]:
        """Download the sde schema changelog for the given build number.

        Raises a ValueError if the changelog is not available for the given build number.

        Raises a ValueError if a file exists at the output path with the same name as the changelog file.

        The changelog file is named "sde_schema_changelog-<build_number>.yaml" and is
        saved to the <output_path> directory if an output path is provided.

        Args:
            build_number: The build number of the static data.
            output_path: The path to the directory where the changelog should be saved.
                If None, the changelog will not be saved to disk.

        Returns:
            A dictionary containing the sde schema changelog.
        """
        if output_path is not None and output_path.is_file():
            raise FileExistsError(
                f"Output path {output_path} is a file. Please provide a directory path "
                "or set output_path to None."
            )

        text = await network.get_sde_schema_changelog(url=self.schema_changelog_url)
        if output_path:
            output_file = output_path / f"schema_changelog-{build_number}.yaml"
            if output_file.exists():
                raise FileExistsError(
                    f"Schema changelog file {output_file} already exists. Please remove the existing file or choose a different output path."
                )
            output_file.parent.mkdir(parents=True, exist_ok=True)
            if output_file.exists():
                raise FileExistsError(
                    f"Schema changelog file {output_file} already exists. Please remove the existing file or choose a different output path."
                )
            output_file.write_text(text)
        result = safe_load(text)
        return cast(dict[str, Any], result)

    async def latest_sde_info(self) -> network.SdeLatestInfo:
        """Download the latest sde info.

        Returns:
            A dictionary containing the latest sde info, including the latest build number and release date.
        """
        info = await network.current_sde_info(url=self.latest_info_url)
        return info

    def export_localized(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int | None,
        lang: Lang = "en",
    ) -> None:
        pass
        raise NotImplementedError(
            "Exporting localized datasets is not yet implemented."
        )

    def export_records(
        self, input_path: Path, output_path: Path, build_number: int | None
    ) -> None:
        pass
        raise NotImplementedError("Exporting records is not yet implemented.")

    async def process(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int,
        lang: list[Literal["en", "de", "fr", "ja", "ru", "zh", "ko", "es"]]
        | None = None,
    ) -> None:
        """Prepare the static data for use.

        Runs the full pipeline of unpacking, validating, and deriving the data.

        Build number is determined from the _sde.jsonl file in the input path unpacked files.
        If the file is not found, or if the build number is not found in the file, raises a ValueError.

        Raises a ValueError if the build number is already available in the output path.

        Raises a ValueError if one of the languages in the lang list is not supported.

        Saves the processed data to the <output_path>/<build_number>/ directory, with the
        following structure:
        - `<output_path>/<build_number>/sde/`: The unpacked original data.
        - `<output_path>/<build_number>/derived/`: The derived localized data.
        - `<output_path>/<build_number>/validation/`: The sde validation results.


        Args:
            input_path: The path to the static data jsonl zip file.
            output_path: The path to the directory where the processed data should be saved.
            lang: A list of languages for which to generate derived dataset files. If None, ["en"] will be used.
        """
        if lang is None:
            lang = ["en"]
        if output_path.is_file():
            raise ValueError(
                f"Output path {output_path} is a file, expected a directory."
            )

        sde_dir = self.unpack(
            input_path=input_path, output_path=output_path, build_number=build_number
        )

        # Validate unpacked data and save results to disk
        await self.validate(
            input_path=sde_dir,
            output_path=output_path,
            build_number=build_number,
        )
        # Derive additional datasets and save to disk
        for language in lang:
            self.derive(
                input_path=sde_dir,
                output_path=output_path,
                build_number=build_number,
                lang=language,
            )
