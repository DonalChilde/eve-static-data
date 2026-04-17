"""Code for validating SDE datasets against the TypedDict schema."""

import json
import logging
from pathlib import Path
from time import perf_counter

from pydantic import BaseModel
from rich.console import Console

from eve_static_data.helpers.jsonl_reader import read_jsonl_file
from eve_static_data.helpers.pydantic.save_to_disk import BaseModelToDisk
from eve_static_data.helpers.save_text_file import save_text_file
from eve_static_data.helpers.sde_info import SdeInfo, load_sde_info
from eve_static_data.models.dataset_filenames import SdeDatasetFiles
from eve_static_data.models.pydantic.records import LOOKUP as pydantic_model_lookup
from eve_static_data.sde_tools import SDETools
from eve_static_data.sde_type_sigs import get_sde_type_sigs
from eve_static_data.transformers import ModelLoader, ModelValidationErrorRecord

logger = logging.getLogger(__name__)

# TODO report when input sde build number is greater than app build number and schema changelog afterbuildnumber.


class DatasetStats(BaseModel):
    """Statistics about a dataset."""

    dataset_name: str
    model_name: str
    file_path: Path
    total_records: int
    invalid_records: int
    start: float
    end: float
    error_records: dict[int, ModelValidationErrorRecord]
    published_records_with_errors: list[int] = []
    line_record_not_published: set[int]


class SDEValidationResult(BaseModelToDisk):
    """The result of validating an SDE dataset."""

    build_number: int | None = None
    release_date: str | None = None
    dataset_stats: dict[str, DatasetStats] = {}


def is_published(text: str) -> bool:
    """Check if the text contains "published": false."""
    if '"published": false' in text:
        return False
    return True


# def validate_dataset_records(
#     input_path: Path, dataset: SdeDatasetFiles, console: Console | None = None
# ) -> DatasetStats:
#     """Validate a dataset against its pydantic model."""
#     file_path = input_path / dataset.as_jsonl()
#     model = pydantic_model_lookup.get(dataset, None)
#     stats = DatasetStats(
#         dataset_name=dataset.value,
#         model_name=model.__name__ if model is not None else "None",
#         file_path=file_path,
#         total_records=0,
#         invalid_records=0,
#         error_records={},
#         line_record_not_published=set(),
#         published_records_with_errors=[],
#     )

#     if model is None:
#         msg = (
#             f"No pydantic model found for dataset {dataset.value}, skipping validation."
#         )
#         logger.warning(msg)
#         stats.invalid_records += 1
#         stats.error_records[0] = ModelValidationErrorRecord(
#             model="NONE",
#             line_number=0,
#             data="",
#             error_messages=[msg],
#         )
#         return stats
#     transformer = ModelLoader(
#         model=model, only_published=False, skip_validation_failures=True
#     )
#     for index, record in read_jsonl_file(file_path, transformer=transformer):
#         stats.total_records = index
#         if record is None:
#             stats.invalid_records += 1
#     stats.error_records = transformer.validation_errors
#     stats.line_record_not_published = transformer.line_record_not_published
#     stats.published_records_with_errors = list(
#         set(stats.error_records.keys()) - stats.line_record_not_published
#     )

#     return stats


# def validate_sde_datasets(
#     input_path: Path, console: Console | None = None
# ) -> SDEValidationResult:
#     """Validate all datasets in the SDE against their pydantic models."""
#     logger.info("Starting SDE validation against pydantic models.")
#     sde_info = load_sde_info(input_path)
#     validation_result = SDEValidationResult(
#         build_number=sde_info["buildNumber"],
#         release_date=sde_info["releaseDate"],
#         dataset_stats={},
#     )
#     for dataset in SdeDatasetFiles:
#         validation_result.dataset_stats[dataset.value] = validate_dataset_records(
#             input_path, dataset
#         )
#     return validation_result


class FileCheckResult(BaseModel):
    """The result of checking for dataset files."""

    sde_path: Path
    existing_file_count: int
    existing_files: set[Path]
    expected_files: set[Path]
    missing_files: set[Path]
    extra_files: set[Path]


# def validate_and_save_results(input_path: Path, output_path: Path) -> None:
#     """Validate the SDE datasets and save the results to disk.

#     This will perform the following validations:
#     - Check for the presence of expected dataset files and report any missing or extra files.
#     - Validate the records in each dataset against their corresponding pydantic models
#         and report any validation errors.
#     - Generate type signature information for all the JSONL files in the input_path directory.
#     """
#     sde_info = load_sde_info(input_path)
#     logger.info(
#         f"Validating SDE datasets for build {sde_info['buildNumber']} and saving results to {output_path}"
#     )

#     start = perf_counter()

#     # Generate and save type signature definitions for the SDE datasets.
#     sde_sigs = get_sde_type_sigs(
#         input_path=input_path, build_number=str(sde_info["buildNumber"])
#     )
#     output_file = output_path / f"sde_type_sig-{sde_info['buildNumber']}.json"
#     with output_file.open("w", encoding="utf-8") as f:
#         json.dump(sde_sigs, f, indent=2, sort_keys=True)
#     logger.info(
#         f"SDE type signature definitions saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
#     )

#     # Check for expected dataset files and save results.
#     file_check_result = check_for_dataset_files(input_path)
#     output_file = output_path / f"dataset_file_check_{sde_info['buildNumber']}.json"
#     with output_file.open("w", encoding="utf-8") as f:
#         f.write(file_check_result.model_dump_json(indent=2))
#     logger.info(
#         f"Dataset file check results saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
#     )

#     # Validate datasets against pydantic models and save results.
#     pydantic_validation_result = validate_sde_datasets(input_path)
#     output_file = (
#         output_path
#         / f"pydantic_model_validation_{pydantic_validation_result.build_number}.json"
#     )
#     pydantic_validation_result.save_to_disk(output_file)
#     logger.info(
#         f"SDE pydantic model validation results saved to {output_file} (took {perf_counter() - start:.4f} seconds)"
#     )

#     logger.info(
#         f"Finished validating SDE datasets and saving results to {output_path} in {perf_counter() - start:.4f} seconds."
#     )


async def validation_report(
    sde_path: Path,
    output_path: Path,
    sde_tools: SDETools,
    console: Console | None = None,
    overwrite: bool = False,
) -> None:
    """Run the SDE validation and print a report to the console."""
    messages: list[str] = []
    sde_info = load_sde_info(sde_path)
    msg = (
        f"Running SDE validation report for build {json.dumps(sde_info)} at {sde_path} "
        f"and saving results to {output_path}"
    )
    logger.info(msg)
    optional_printer(msg, console=console)
    messages.append(msg)
    build_number = sde_info["buildNumber"]
    release_date = sde_info["releaseDate"]
    generate_and_save_type_sigs(
        input_path=sde_path,
        output_path=output_path,
        build_number=str(build_number),
        console=console,
    )
    file_check_result, msgs = check_for_dataset_files(sde_path, console=console)
    messages.extend(msgs)
    msgs = report_on_dataset_files(file_check_result, console=console)
    messages.extend(msgs)

    msgs = await fetch_data_changes(
        build_number=build_number,
        output_path=output_path,
        sde_tools=sde_tools,
        overwrite=overwrite,
        console=console,
    )
    messages.extend(msgs)
    msgs = await fetch_schema_changelog(
        build_number=build_number,
        output_path=output_path,
        sde_tools=sde_tools,
        overwrite=overwrite,
        console=console,
    )
    messages.extend(msgs)
    msgs = save_sde_info_to_disk(
        sde_info=sde_info, output_path=output_path, overwrite=overwrite
    )
    messages.extend(msgs)

    dataset_stats, msgs = validate_datasets(sde_path, console=console)
    validation_result = SDEValidationResult(
        build_number=build_number,
        release_date=release_date,
        dataset_stats=dataset_stats,
    )
    messages.extend(msgs)
    save_text_file(
        text=validation_result.model_dump_json(indent=2),
        output_path=output_path,
        file_name=f"sde_validation_result_{build_number}.json",
        overwrite=overwrite,
    )
    msgs = report_on_validated_datasets(validation_result, console=console)
    messages.extend(msgs)

    save_text_file(
        text="\n".join(messages),
        output_path=output_path,
        file_name=f"report_{build_number}.txt",
        overwrite=overwrite,
    )


def generate_and_save_type_sigs(
    input_path: Path,
    output_path: Path,
    build_number: str,
    console: Console | None = None,
) -> tuple[Path, list[str]]:
    """Generate type signature definitions for the SDE datasets and save to a file."""
    messages: list[str] = []
    start = perf_counter()
    msg = f"Generating SDE type signature definitions for SDE at {input_path}..."
    logger.info(msg)
    optional_printer(msg, console=console)
    messages.append(msg)
    sde_sigs = get_sde_type_sigs(input_path=input_path, build_number=build_number)
    output_file = output_path / f"sde_type_sig-{build_number}.json"
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(sde_sigs, f, indent=2, sort_keys=True)
    msg = f"SDE type signature definitions saved to {output_file} (took {perf_counter() - start:.6f} seconds)"
    logger.info(msg)
    optional_printer(msg, console=console)
    messages.append(msg)
    return output_file, messages


def report_on_validated_datasets(
    validation_result: SDEValidationResult, console: Console | None = None
) -> list[str]:
    """Print a report on the validated datasets to the console."""
    messages: list[str] = []
    for dataset_name, stats in validation_result.dataset_stats.items():
        if stats.invalid_records > 0:
            msg = (
                f"Dataset {dataset_name} has {stats.invalid_records} invalid records "
                f"out of {stats.total_records} total records."
            )
            logger.warning(msg)
            messages.append(msg)
    for msg in messages:
        optional_printer(msg, console=console)
    return messages


def validate_datasets(
    input_path: Path, console: Console | None = None
) -> tuple[dict[str, DatasetStats], list[str]]:
    """Validate all datasets in the SDE against their pydantic models and return stats."""
    messages: list[str] = []
    msg = f"Starting SDE dataset validation against pydantic models for SDE at {input_path}..."
    logger.info(msg)
    optional_printer(msg, console=console)
    dataset_stats: dict[str, DatasetStats] = {}

    for dataset in SdeDatasetFiles:
        stats, msgs = validate_records(input_path, dataset, console=console)
        dataset_stats[dataset.value] = stats
        messages.extend(msgs)
    return dataset_stats, messages


def validate_records(
    input_path: Path, dataset: SdeDatasetFiles, console: Console | None = None
) -> tuple[DatasetStats, list[str]]:
    """Validate a dataset against its pydantic model."""
    messages: list[str] = []
    file_path = input_path / dataset.as_jsonl()
    model = pydantic_model_lookup.get(dataset, None)
    stats = DatasetStats(
        dataset_name=dataset.value,
        model_name=model.__name__ if model is not None else "None",
        file_path=file_path,
        total_records=0,
        invalid_records=0,
        start=perf_counter(),
        end=perf_counter(),
        error_records={},
        line_record_not_published=set(),
        published_records_with_errors=[],
    )

    if model is None:
        msg = (
            f"No pydantic model found for dataset {dataset.value}, skipping validation."
        )
        logger.warning(msg)
        messages.append(msg)
        optional_printer(msg, console=console)
        stats.invalid_records += 1
        stats.error_records[0] = ModelValidationErrorRecord(
            model="NONE",
            line_number=0,
            data="",
            error_messages=[msg],
        )
        return stats, messages

    # refactor this to remove unnecessary complication of transformer and read_jsonl_file.
    # needs to:
    # - read the file line by line
    # - for each line, validate against the model and keep track of errors and counts.
    # - determine if the record is published or not, in a way that doesn't require model validate.
    with file_path.open() as f:
        for index, line in enumerate(f, start=1):
            stats.total_records = index
            if not is_published(line):
                stats.line_record_not_published.add(index)
            try:
                model.model_validate_json(line)
            except Exception as e:
                stats.invalid_records += 1
                stats.error_records[index] = ModelValidationErrorRecord(
                    model=model.__name__,
                    line_number=index,
                    data=line,
                    error_messages=[str(e)],
                )
                logger.exception(
                    f"Validation error for model {model.__name__} at line {index}:{line} {e}"
                )
    # transformer = ModelLoader(
    #     model=model, only_published=False, skip_validation_failures=True
    # )
    # for index, record in read_jsonl_file(file_path, transformer=transformer):
    #     stats.total_records = index
    #     if not is_published(record):
    #         stats.line_record_not_published.add(index)
    #     if record is None:
    #         stats.invalid_records += 1
    # stats.error_records = transformer.validation_errors
    # stats.line_record_not_published = transformer.line_record_not_published
    stats.published_records_with_errors = list(
        set(stats.error_records.keys()) - stats.line_record_not_published
    )
    stats.end = perf_counter()
    msg = f"Finished validating dataset {dataset.value}. Total records: {stats.total_records},Published records: {stats.total_records - len(stats.line_record_not_published)}, Invalid records: {stats.invalid_records}, Invalid published records: {len(stats.published_records_with_errors)}, Time taken: {stats.end - stats.start:.6f} seconds."
    messages.append(msg)
    optional_printer(msg, console=console)
    return stats, messages


def report_on_dataset_files(
    file_check_result: FileCheckResult, console: Console | None = None
) -> list[str]:
    """Print a report on the dataset files to the console."""
    messages: list[str] = []
    messages.append(f"Dataset file check for SDE path {file_check_result.sde_path}:")
    messages.append(f"  Expected files: {len(file_check_result.expected_files)}")
    messages.append(f"  Existing files: {file_check_result.existing_file_count}")
    if file_check_result.missing_files:
        messages.append(f"  Missing files ({len(file_check_result.missing_files)}):")
        for missing_file in file_check_result.missing_files:
            messages.append(f"    - {missing_file.name}")
    if file_check_result.extra_files:
        messages.append(f"  Extra files ({len(file_check_result.extra_files)}):")
        for extra_file in file_check_result.extra_files:
            messages.append(f"    - {extra_file.name}")
    for msg in messages:
        optional_printer(msg, console=console)
    return messages


def check_for_dataset_files(
    input_path: Path, console: Console | None = None
) -> tuple[FileCheckResult, list[str]]:
    """Check if the expected dataset files are present in the SDE path."""
    messages: list[str] = []
    msg = f"Checking for expected dataset files in {input_path}..."
    optional_printer(msg, console=console)
    messages.append(msg)
    existing_files = set(p for p in input_path.iterdir() if p.is_file())
    expected_files = set(input_path / dataset.as_jsonl() for dataset in SdeDatasetFiles)
    result = FileCheckResult(
        sde_path=input_path,
        existing_file_count=len(existing_files),
        existing_files=existing_files,
        expected_files=expected_files,
        missing_files=expected_files - existing_files,
        extra_files=existing_files - expected_files,
    )
    return result, messages


def save_sde_info_to_disk(
    sde_info: SdeInfo, output_path: Path, overwrite: bool = False
) -> list[str]:
    """Save the SDE info to disk and return messages about the save operation."""
    messages: list[str] = []
    file_name = f"sde_info_{sde_info['buildNumber']}.json"
    output_file = save_text_file(
        text=json.dumps(sde_info, indent=2),
        output_path=output_path,
        file_name=file_name,
        overwrite=overwrite,
    )
    msg = f"SDE info saved to {output_file}"
    logger.info(msg)
    messages.append(msg)
    return messages


async def fetch_schema_changelog(
    output_path: Path,
    build_number: int,
    sde_tools: SDETools,
    overwrite: bool = False,
    console: Console | None = None,
) -> list[str]:
    """Fetch the schema changelog and save to a file."""
    messages: list[str] = []
    msg = f"Fetching schema changelog for build {build_number}..."
    optional_printer(msg, console=console)
    messages.append(msg)
    changelog = await sde_tools.fetch_schema_changelog(build_number=build_number)
    save_text_file(
        text=changelog,
        output_path=output_path,
        file_name="schema_changelog.yaml",
        overwrite=overwrite,
    )
    msg = f"Schema changelog saved to {output_path}"
    optional_printer(msg, console=console)
    messages.append(msg)
    return messages


async def fetch_data_changes(
    build_number: int,
    output_path: Path,
    sde_tools: SDETools,
    overwrite: bool = False,
    console: Console | None = None,
) -> list[str]:
    """Fetch the data changes for a given build number and save to a file."""
    messages: list[str] = []
    msg = f"Fetching data changes for build {build_number}..."
    optional_printer(msg, console=console)
    messages.append(msg)
    changes = await sde_tools.fetch_data_changes(build_number=build_number)
    save_text_file(
        text=changes,
        output_path=output_path,
        file_name=f"sde_data_changes_{build_number}.jsonl",
        overwrite=overwrite,
    )
    msg = f"Data changes for build {build_number} saved to {output_path}"
    optional_printer(msg, console=console)
    messages.append(msg)
    return messages


def optional_printer(message: str, console: Console | None = None) -> None:
    """Print a message to the console if a console is provided, otherwise do nothing."""
    if console is not None:
        console.print(message)
