"""Implementation of the EsdTools."""

from pathlib import Path
from string import Template

from eve_static_data import (
    DATA_CHANGES_URL_TEMPLATE,
    DATA_FILENAME_TEMPLATE,
    LATEST_INFO_URL,
    SCHEMA_CHANGELOG_URL,
    SDE_URL_TEMPLATE,
    USER_AGENT,
)
from eve_static_data.helpers.aiohttp.download_files import (
    download_bytes_to_file,
    download_text,
)
from eve_static_data.helpers.sde_info import SdeInfo
from eve_static_data.helpers.sde_unpack import unpack


class SDETools:
    """Class for handling SDE tools static data."""

    def __init__(
        self,
        latest_info_url: str = LATEST_INFO_URL,
        download_url_template: str = SDE_URL_TEMPLATE,
        data_changes_url_template: str = DATA_CHANGES_URL_TEMPLATE,
        schema_changelog_url: str = SCHEMA_CHANGELOG_URL,
        data_filename_template: str = DATA_FILENAME_TEMPLATE,
        user_agent: str = USER_AGENT,
    ):
        """The SDETools class for handling EVE Static Data."""
        self.latest_info_url = latest_info_url
        self.download_url_template = download_url_template
        self.data_changes_url_template = data_changes_url_template
        self.schema_changelog_url = schema_changelog_url
        self.data_filename_template = data_filename_template
        self.user_agent = user_agent

    async def download(
        self,
        build_number: int,
        output_directory: Path,
        variant: str = "jsonl",
        overwrite: bool = False,
    ) -> Path:
        """Download the SDE tools static data."""
        headers = {"User-Agent": self.user_agent}
        url = Template(self.download_url_template).substitute(
            build_number=build_number, variant=variant
        )
        file_name = Template(self.data_filename_template).substitute(
            build_number=build_number, variant=variant
        )
        output_path = output_directory / file_name
        await download_bytes_to_file(
            url=url, file_path=output_path, headers=headers, overwrite=overwrite
        )
        return output_path

    def unpack(
        self, input_path: Path, output_path: Path, use_build_number: bool = False
    ) -> tuple[Path, SdeInfo]:
        """Unpack the downloaded static data."""
        file_path, info = unpack(
            input_path, output_path, use_build_number=use_build_number
        )
        return file_path, info

    async def validate(self, sde_path: Path, report_directory: Path) -> None:
        """Validate the SDE tools static data."""
        raise NotImplementedError("SDE validation is not yet implemented.")

    async def fetch_data_changes(self, build_number: int) -> str:
        """Download the sde data changes for the given build number.

        The SDE data changes is a JSONL file that contains a list of changes for a build.
        The record with key _meta contains lastBuildNumber, referring to the previous SDE.

        Each line can be parsed with json.loads to convert the JSONL text into a Python dictionary.
        """
        headers = {"User-Agent": self.user_agent}
        url = Template(self.data_changes_url_template).substitute(
            build_number=build_number
        )
        text, _ = await download_text(url=url, headers=headers)
        return text

    async def fetch_schema_changelog(self, build_number: int) -> str:
        """Download the sde schema changelog for the given build number.

        The SDE schema changelog is a YAML file that contains a list of schema changes for a build.
        This function returns the raw YAML text of the changelog. use safe_load from the
        yaml library to parse the YAML text into a Python dictionary.
        """
        headers = {"User-Agent": self.user_agent}
        url = Template(self.schema_changelog_url).substitute(build_number=build_number)
        text, _ = await download_text(url=url, headers=headers)
        return text

    async def fetch_latest_sde_info(self) -> str:
        """Download the latest sde info.

        The latest sde info is a JSONL file that contains information about the latest
        SDE build, including the latest build number and release date.

        Because the latest sde info is a JSONL file with a single record, this function
        returns the raw JSONL text of the latest sde info. use json.loads to parse the
        JSONL text into a Python dictionary.
        """
        headers = {"User-Agent": self.user_agent}
        url = Template(self.latest_info_url).substitute()
        text, _ = await download_text(url=url, headers=headers)
        return text

    # Tools include:
    # - Downloading the SDE tools static data for a given build number.
    # - Unpacking the downloaded static data.
    # - Validating the unpacked static data.
    # - see current cli functionality for more details on the above steps and the expected inputs and outputs of each step.


# import logging
# import shutil
# import zipfile
# from pathlib import Path
# from tempfile import TemporaryDirectory
# from typing import Any, Literal, cast

# from yaml import safe_load

# from eve_static_data import network
# from eve_static_data.derive_datasets import generate_derived_datasets
# from eve_static_data.helpers.sde_info import load_sde_info, load_sde_info_from_zipfile
# from eve_static_data.models.type_defs import Lang
# from eve_static_data.protocols import ESDToolsProtocol
# from eve_static_data.validation import validate_and_save_results

# logger = logging.getLogger(__name__)


# class EsdTools(ESDToolsProtocol):
#     """Class for handling ESD tools static data."""

#     def __init__(
#         self,
#         sde_url_template: str = network.SDE_URL_TEMPLATE,
#         data_changes_url_template: str = network.DATA_CHANGES_URL_TEMPLATE,
#         schema_changelog_url: str = network.SCHEMA_CHANGELOG_URL,
#         latest_info_url: str = network.LATEST_INFO_URL,
#     ):
#         """The EsdTools class for handling ESD tools static data."""
#         self.sde_url_template = sde_url_template
#         self.data_changes_url_template = data_changes_url_template
#         self.schema_changelog_url = schema_changelog_url
#         self.latest_info_url = latest_info_url

#     async def download(
#         self,
#         build_number: int,
#         output_path: Path,
#         variant: Literal["jsonl", "yaml"] = "jsonl",
#         overwrite: bool = False,
#     ) -> Path:
#         """Download the ESD tools static data."""
#         response_headers = await network.download_sde_to_file(
#             build_number=build_number,
#             output_path=output_path,
#             url_template_str=self.sde_url_template,
#             variant=variant,
#             overwrite=overwrite,
#         )
#         return response_headers

#     def unpack(self, input_path: Path, output_path: Path) -> tuple[Path, int]:
#         """Unpack the static data.

#         Unzip the input file and save the unpacked data to the output path.

#         Checks for the presence of the _sde.jsonl file in the unpacked files. If the file is not
#         found, raises a FileNotFoundError.

#         Files will be saved to `<output_path>/<build_number>/sde/` directory, where the
#         build number is determined from the `_sde.jsonl` file inside the zip file.

#         Args:
#             input_path: The path to the static data jsonl zip file.
#             output_path: The path to the directory where the unpacked data should be saved.

#         Returns:
#             The path to the directory where the unpacked data is saved.
#         """
#         if not input_path.is_file():
#             raise FileNotFoundError(f"Input path {input_path} is not a file.")
#         if input_path.suffix != ".zip":
#             raise ValueError(f"Input file {input_path} is not a zip file.")
#         if output_path.exists() and not output_path.is_dir():
#             raise FileExistsError(
#                 f"Output path {output_path} already exists and is not a directory."
#             )
#         sde_info = load_sde_info_from_zipfile(input_path)
#         build_number = sde_info.get("buildNumber")
#         if build_number is None:  # type: ignore
#             raise ValueError(
#                 f"Build number not found in _sde.jsonl file in the zip file {input_path}."
#             )
#         with TemporaryDirectory() as temp_dir:
#             with zipfile.ZipFile(input_path, "r") as zip_ref:
#                 zip_ref.extractall(temp_dir)
#             sde_info_file = Path(temp_dir) / "_sde.jsonl"
#             if not sde_info_file.exists():
#                 raise FileNotFoundError(
#                     f"_sde.jsonl file not found in the unzipped SDE data at {temp_dir}. Is this a valid SDE zip file?"
#                 )
#             output_dir = output_path / str(build_number) / "sde"
#             output_dir.mkdir(parents=True, exist_ok=True)
#             for file in Path(temp_dir).iterdir():
#                 if file.is_file():
#                     target_file = output_dir / file.name
#                     if target_file.exists():
#                         raise FileExistsError(
#                             f"Target file {target_file} already exists. Cannot move processed data to {target_file}"
#                         )
#                     shutil.move(file, target_file)
#             return output_dir, build_number

#     async def validate(self, input_path: Path, output_path: Path) -> None:
#         """Validate the ESD tools static data."""
#         sde_info = load_sde_info(input_path)

#         build_number = sde_info.get("buildNumber")
#         output_path.mkdir(parents=True, exist_ok=True)

#         validate_and_save_results(input_path=input_path, output_path=output_path)
#         await self.schema_changelog(build_number=build_number, output_path=output_path)
#         await self.data_changes(build_number=build_number, output_path=output_path)

#     def derive(
#         self,
#         input_path: Path,
#         output_path: Path,
#         lang: Lang = "en",
#     ) -> None:
#         """Derive additional ESD tools static data from the original data."""
#         output_path.mkdir(parents=True, exist_ok=True)
#         generate_derived_datasets(
#             input_path=input_path, output_path=output_path, lang=lang
#         )

#     async def data_changes(
#         self, build_number: int, output_path: Path | None = None
#     ) -> list[str]:
#         """Download the sde data changes for the given build number.

#         Raises a ValueError if the changes are not available for the given build number.

#         Raises a ValueError if a file exists at the output path with the same name as the changelog file.

#         The changes file is named "sde_data_changes-<build_number>.jsonl" and is
#         saved to the <output_path> directory if an output path is provided.

#         Args:
#             build_number: The build number of the static data.
#             output_path: The path to the directory where the changelog should be saved.
#                 If None, the changelog will not be saved to disk.

#         Returns:
#             A list of strings representing the sde data changes.
#         """
#         if output_path is not None and output_path.is_file():
#             raise FileExistsError(
#                 f"Output path {output_path} is a file. Please provide a directory path or set output_path to None."
#             )

#         text = await network.get_sde_data_changes(
#             build_number=build_number, url_template=self.data_changes_url_template
#         )
#         changes = text.splitlines()
#         if output_path:
#             output_file = output_path / f"changes-{build_number}.jsonl"
#             if output_file.exists():
#                 raise FileExistsError(
#                     f"Data changes file {output_file} already exists. Please remove the existing file or choose a different output path."
#                 )
#             output_file.parent.mkdir(parents=True, exist_ok=True)
#             output_file.write_text(text)
#         return changes

#     async def schema_changelog(
#         self, build_number: int, output_path: Path | None = None
#     ) -> dict[str, Any]:
#         """Download the sde schema changelog for the given build number.

#         Raises a ValueError if the changelog is not available for the given build number.

#         Raises a ValueError if a file exists at the output path with the same name as the changelog file.

#         The changelog file is named "sde_schema_changelog-<build_number>.yaml" and is
#         saved to the <output_path> directory if an output path is provided.

#         Args:
#             build_number: The build number of the static data.
#             output_path: The path to the directory where the changelog should be saved.
#                 If None, the changelog will not be saved to disk.

#         Returns:
#             A dictionary containing the sde schema changelog.
#         """
#         if output_path is not None and output_path.is_file():
#             raise FileExistsError(
#                 f"Output path {output_path} is a file. Please provide a directory path "
#                 "or set output_path to None."
#             )

#         text = await network.get_sde_schema_changelog(url=self.schema_changelog_url)
#         if output_path:
#             output_file = output_path / f"schema_changelog-{build_number}.yaml"
#             if output_file.exists():
#                 raise FileExistsError(
#                     f"Schema changelog file {output_file} already exists. Please remove the existing file or choose a different output path."
#                 )
#             output_file.parent.mkdir(parents=True, exist_ok=True)
#             if output_file.exists():
#                 raise FileExistsError(
#                     f"Schema changelog file {output_file} already exists. Please remove the existing file or choose a different output path."
#                 )
#             output_file.write_text(text)
#         result = safe_load(text)
#         return cast(dict[str, Any], result)

#     async def latest_sde_info(self) -> network.SdeLatestInfo:
#         """Download the latest sde info.

#         Returns:
#             A dictionary containing the latest sde info, including the latest build number and release date.
#         """
#         info = await network.current_sde_info(url=self.latest_info_url)
#         return info

#     def export_localized(
#         self,
#         input_path: Path,
#         output_path: Path,
#         build_number: int | None,
#         lang: Lang = "en",
#     ) -> None:
#         pass
#         raise NotImplementedError(
#             "Exporting localized datasets is not yet implemented."
#         )

#     def export_records(
#         self, input_path: Path, output_path: Path, build_number: int | None
#     ) -> None:
#         pass
#         raise NotImplementedError("Exporting records is not yet implemented.")

#     async def process(
#         self,
#         input_path: Path,
#         output_path: Path,
#         lang: list[Literal["en", "de", "fr", "ja", "ru", "zh", "ko", "es"]]
#         | None = None,
#     ) -> None:
#         """Prepare the static data for use.

#         Runs the full pipeline of unpacking, validating, and deriving the data.

#         Build number is determined from the _sde.jsonl file in the input path unpacked files.
#         If the file is not found, or if the build number is not found in the file, raises a ValueError.

#         Raises a ValueError if the build number is already available in the output path.

#         Raises a ValueError if one of the languages in the lang list is not supported.

#         Saves the processed data to the <output_path>/<build_number>/ directory, with the
#         following structure:
#         - `<output_path>/<build_number>/sde/`: The unpacked original data.
#         - `<output_path>/<build_number>/derived/`: The derived localized data.
#         - `<output_path>/<build_number>/validation/`: The sde validation results.


#         Args:
#             input_path: The path to the static data jsonl zip file.
#             output_path: The path to the directory where the processed data should be saved.
#             lang: A list of languages for which to generate derived dataset files. If None, ["en"] will be used.
#         """
#         if lang is None:
#             lang = ["en"]
#         if output_path.is_file():
#             raise ValueError(
#                 f"Output path {output_path} is a file, expected a directory."
#             )

#         sde_dir, build_number = self.unpack(
#             input_path=input_path, output_path=output_path
#         )

#         # Validate unpacked data and save results to disk
#         validated_dir = self.validation_directory(
#             base_path=output_path, build_number=build_number
#         )
#         await self.validate(input_path=sde_dir, output_path=validated_dir)
#         # Derive additional datasets and save to disk
#         derived_dir = self.derived_directory(
#             base_path=output_path, build_number=build_number
#         )
#         for language in lang:
#             self.derive(
#                 input_path=sde_dir,
#                 output_path=derived_dir,
#                 lang=language,
#             )
