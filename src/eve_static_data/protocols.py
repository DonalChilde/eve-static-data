"""Protocols for static data classes."""

from pathlib import Path
from typing import Any, Literal, Protocol

from eve_static_data import network
from eve_static_data.models.dataset_filenames import (
    DerivedDatasetFiles,
    SdeDatasetFiles,
)
from eve_static_data.models.type_defs import Lang


class ESDToolsProtocol(Protocol):
    """Tools for working with EVE Online static data."""

    async def download(
        self,
        build_number: int,
        output_path: Path,
        variant: Literal["jsonl", "yaml"] = "jsonl",
        overwrite: bool = False,
    ) -> Path:
        """Download the static data.

        Args:
            build_number: The build number of the SDE to download.
            output_path: The directory to save the downloaded SDE file to.
            variant: The variant of the SDE data to download, either "jsonl" or "yaml". Defaults to "jsonl".
            overwrite: Whether to overwrite the output file if it already exists. Defaults to False.

        Returns:
            The path to the downloaded SDE file.
        """
        ...

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
        ...

    async def validate(
        self, input_path: Path, output_path: Path, build_number: int | None
    ) -> None:
        """Validate the static data.

        Save validation results to the <output_path> directory.
        If a build number is provided, save the validation results to <output_path>/<build_number>/validated/.

        Checks for the presence of the <input_path>/_sde.jsonl file. If the file is not
        found, raises a ValueError.

        If build number is provided, checks that the build number in the <input_path>/_sde.jsonl
        file matches the provided build number. If it does not match, raises a ValueError.

        Results include:
        - validation_report.json: A JSON file containing a summary of the validation results, including the number of records validated, the number of records that passed validation, and the number of records that failed validation.
        - validation_errors.json: A JSON file containing a list of validation errors, including the record that failed validation and the reason for the failure.
        - validation_summary.txt: A human-readable text file summarizing the validation results.
        - sde_data_changelog.jsonl: A JSONL file containing the sde data changelog.
        - sde_schema_changelog.yaml: A YAML file containing the schema changelog.

        """
        ...

    def derive(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int | None,
        lang: Lang = "en",
    ) -> None:
        """Derive localized static data from the original data.

        Save the derived data to the <output_path> directory.
        If a build number is provided, save the derived data to <output_path>/<build_number>/derived/.

        Checks for the presence of the <input_path>/_sde.jsonl file. If the file is not
        found, raises a ValueError.

        If build number is provided, checks that the build number in the <input_path>/_sde.jsonl
        file matches the provided build number. If it does not match, raises a ValueError.

        Args:
            input_path: The path to the unpacked and validated static data.
            output_path: The path to the directory where the derived data should be saved.
            build_number: The build number of the static data.
            lang: The language of the derived data.
        """
        ...

    def export_localized(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int | None,
        lang: Lang = "en",
    ) -> None:
        """Export the static data as localized dataset json files.

        Save the exported data to the <output_path> directory.
        If a build number is provided, save the exported data to <output_path>/<build_number>/exported/.

        Checks for the presence of the <input_path>/_sde.jsonl file. If the file is not
        found, raises a ValueError.

        If build number is provided, checks that the build number in the <input_path>/_sde.jsonl
        file matches the provided build number. If it does not match, raises a ValueError.


        Args:
            input_path: The path to the unpacked, validated, and derived static data.
            output_path: The path to the directory where the exported data should be saved.
            build_number: The build number of the static data.
            lang: The language of the exported data.

        Raises:
            ValueError: If the <input_path>/_sde.jsonl file is not found
            ValueError: If the build number in the <input_path>/_sde.jsonl file does not
                match the provided build number.
        """
        ...

    def export_records(
        self, input_path: Path, output_path: Path, build_number: int | None
    ) -> None:
        """Export the JSONL static data as JSON files containing lists of records.

        Checks for the presence of the <input_path>/_sde.jsonl file. If the file is not
        found, raises a ValueError.

        If build number is provided, checks that the build number in the <input_path>/_sde.jsonl
        file matches the provided build number. If it does not match, raises a ValueError.

        Note that this format removes the advantages of data in jsonl format, such as
        the ability to stream the data and process it in chunks. But it may be useful
        for some use cases.

        Args:
            input_path: The path to the unpacked, validated, and derived static data.
            output_path: The path to the directory where the exported data should be saved.
            build_number: The build number of the static data.
        """
        ...

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
        ...

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
        ...

    async def latest_sde_info(self) -> network.SdeLatestInfo:
        """Download the latest sde info.

        Returns:
            A dictionary containing the latest sde info, including the latest build number and release date.
        """
        ...

    async def process(
        self,
        input_path: Path,
        output_path: Path,
        build_number: int,
        lang: list[Lang] | None = None,
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
            build_number: The build number of the static data.
            lang: A list of languages for which to generate derived dataset files. If None, ["en"] will be used.
        """
        ...


class StaticDataStoreProtocol(Protocol):
    """Protocol for storing and accessing static data builds.

    The static data store can hold multiple builds of static data, each identified by a
    build number. The store provides methods for importing new builds, listing available
    builds, accessing the directory of a specific build, and removing builds from the store.

    Most sde data is kept in the original jsonl format, and users are expected to transform
    the data as needed for their use case. The exception to this is the derived dataset files.
    These are pre-generated since some of them involve combining data from multiple datasets.

    In many cases, the user will only need to access the derived dataset files.



    """

    def import_build(self, input_path: Path, langs: list[Lang] | None = None) -> None:
        """Import a build of static data from the given input path.

        Will not overwrite an existing build with the same build number.

        Args:
            input_path: The path to the sde jsonl variant zip file.
            langs: A list of languages for which to generate derived dataset files.
                If None, ["en"] will be used.

        Raises:
            ValueError: If the build number is already available in the store.

        """
        ...

    def available_builds(self) -> list[tuple[int, str]]:
        """Return a list of available build numbers and release dates in the static data store.

        Returns:
            A list of tuples, where each tuple contains a build number and its corresponding release date.
        """
        ...

    def latest_build(self) -> tuple[int, str] | None:
        """Return the latest build number and release date in the static data store, or None if no builds are available.

        Returns:
            A tuple containing the latest build number and its corresponding release date, or None if no builds are available.
        """
        ...

    def build_directory(self, build_number: int) -> Path | None:
        """Return the directory where the static data for the given build number is stored.

        This would be the directory containing the `sde/`, `derived/`, and `validated/`
        subdirectories for the given build number.

        Args:
            build_number: The build number of the static data.

        Returns:
            The path to the directory where the static data for the given build number is stored, or None if the build is not available.
        """
        ...

    def dataset_file(self, build_number: int, dataset: SdeDatasetFiles) -> Path | None:
        """Return the path to the specified jsonl dataset file for the given build number.

        Args:
            build_number: The build number of the static data.
            dataset: The dataset file to be accessed.

        Returns:
            The path to the specified jsonl dataset file for the given build number, or None
                if the build or dataset file is not available.
        """
        ...

    def derived_dataset_file(
        self, build_number: int, dataset: DerivedDatasetFiles, lang: Lang = "en"
    ) -> Path | None:
        """Return the path to the specified derived dataset file for the given build number.

        Args:
            build_number: The build number of the static data.
            dataset: The dataset file to be accessed.
            lang: The language of the derived dataset file to be accessed.

        Returns:
            The path to the specified derived dataset file for the given build number, or None
                if the build or dataset file is not available.
        """
        ...

    def remove_build(self, build_number: int) -> None:
        """Remove the static data for the given build number from the store.

        Args:
            build_number: The build number of the static data to be removed.

        Raises:
            ValueError: If the build number is not available in the store.
        """
        ...
