# import shutil
# from pathlib import Path

# from eve_static_data.helpers.sde_info import load_sde_info
# from eve_static_data.models.dataset_filenames import (
#     DerivedDatasetFiles,
#     SdeDatasetFiles,
# )
# from eve_static_data.models.type_defs import Lang
# from eve_static_data.protocols import StaticDataStoreProtocol


# class EsdStore(StaticDataStoreProtocol):
#     """A store for EVE Static Data Export (ESD) data.

#     This class implements the StaticDataStoreProtocol and provides access to the ESD datasets.

#     The ESD datasets are expected to be organized in a directory structure as follows:
#     ```
#     data_dir/
#         build_number_1/
#             sde/
#                 <sde dataset files>
#             derived/
#                 <derived dataset files>
#             validated/
#                 <validated dataset files>
#         build_number_2/
#             sde/
#                 <sde dataset files>
#             derived/
#                 <derived dataset files>
#             validated/
#                 <validated dataset files>
#         ...
#     ```
#     """

#     def __init__(self, data_dir: Path):
#         """Initialize the EsdStore with the directory containing the ESD datasets.

#         Args:
#             data_dir: The directory where the ESD datasets are located.
#         """
#         self.data_dir = data_dir

#     def import_build(
#         self, input_path: Path, build_number: int, langs: list[Lang] | None = None
#     ) -> None:
#         """Import a build of static data from the given input path.

#         Will not overwrite an existing build with the same build number.
#         The build number provided is used to check for existing builds. The build number
#         used to determine the actual build being imported will be determined from the
#         metadata in the input file.

#         Args:
#             input_path: The path to the sde jsonl variant zip file.
#             build_number: The build number of the static data.
#             langs: A list of languages for which to generate derived dataset files.
#                 If None, ["en"] will be used.

#         Raises:
#             ValueError: If the build number is already available in the store.

#         """
#         if self.build_directory(build_number) is not None:
#             raise ValueError(
#                 f"Build number {build_number} is already available in the store."
#             )

#     def available_builds(self) -> list[tuple[int, str]]:
#         """Return a list of available build numbers and release dates in the static data store.

#         Returns:
#             A list of tuples, where each tuple contains a build number and its corresponding release date.
#         """
#         builds: list[tuple[int, str]] = []
#         for build_dir in self.data_dir.iterdir():
#             if build_dir.is_dir():
#                 try:
#                     sde_dir = build_dir / "sde"
#                     sde_info = load_sde_info(sde_dir)
#                     builds.append((sde_info["buildNumber"], sde_info["releaseDate"]))
#                 except Exception:
#                     continue  # Skip directories that do not contain the _sde.jsonl file.
#         return builds

#     def latest_build(self) -> tuple[int, str] | None:
#         """Return the latest build number and release date in the static data store, or None if no builds are available.

#         Returns:
#             A tuple containing the latest build number and its corresponding release date, or None if no builds are available.
#         """
#         builds = self.available_builds()
#         if not builds:
#             return None
#         return max(builds, key=lambda x: x[0])

#     def build_directory(self, build_number: int) -> Path | None:
#         """Return the directory where the static data for the given build number is stored.

#         This would be the directory containing the `sde/`, `derived/`, and `validated/`
#         subdirectories for the given build number.

#         Args:
#             build_number: The build number of the static data.

#         Returns:
#             The path to the directory where the static data for the given build number is stored, or None if the build is not available.
#         """
#         build_dir = self.data_dir / str(build_number)
#         if build_dir.is_dir():
#             return build_dir
#         return None

#     def dataset_file(self, build_number: int, dataset: SdeDatasetFiles) -> Path | None:
#         """Return the path to the specified jsonl dataset file for the given build number.

#         Args:
#             build_number: The build number of the static data.
#             dataset: The dataset file to be accessed.

#         Returns:
#             The path to the specified jsonl dataset file for the given build number, or None
#                 if the build or dataset file is not available.
#         """
#         build_dir = self.build_directory(build_number)
#         if build_dir is None:
#             return None
#         dataset_path = build_dir / "sde" / dataset.as_jsonl()
#         if dataset_path.is_file():
#             return dataset_path
#         return None

#     def derived_dataset_file(
#         self, build_number: int, dataset: DerivedDatasetFiles, lang: Lang = "en"
#     ) -> Path | None:
#         """Return the path to the specified derived dataset file for the given build number.

#         Args:
#             build_number: The build number of the static data.
#             dataset: The dataset file to be accessed.
#             lang: The language of the derived dataset file to be accessed.

#         Returns:
#             The path to the specified derived dataset file for the given build number, or None
#                 if the build or dataset file is not available.
#         """
#         build_dir = self.build_directory(build_number)
#         if build_dir is None:
#             return None
#         dataset_path = build_dir / "derived" / dataset.localized(lang)
#         if dataset_path.is_file():
#             return dataset_path
#         return None

#     def remove_build(self, build_number: int) -> None:
#         """Remove the static data for the given build number from the store.

#         Args:
#             build_number: The build number of the static data to be removed.

#         Raises:
#             ValueError: If the build number is not available in the store.
#         """
#         build_dir = self.build_directory(build_number)
#         if build_dir is None:
#             raise ValueError(
#                 f"Build number {build_number} is not available in the store."
#             )
#         shutil.rmtree(build_dir)
