"""CLI commands for SDE development tasks."""

import json
from pathlib import Path
from pprint import pformat
from typing import Annotated, Literal

import typer
from rich.console import Console
from whenever import Instant

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.helpers.datetime_filename import file_safe_iso_datetime_string
from eve_static_data.helpers.dict_diagnostics import (
    collect_dict_keys_and_types_recursive,
)
from eve_static_data.helpers.sde_dict_sigs import sde_dict_sigs_to_file
from eve_static_data.helpers.sde_typed_dicts_to_file import (
    make_typed_dict,
    sde_typed_dicts_to_file,
)
from eve_static_data.models.datasets.sde_dataset_files import SdeDatasetFiles
from eve_static_data.sde_data.validation import (
    SDEValidationResult,
    check_for_dataset_files,
    validate_sde_pydantic,
    validate_sde_typeddict,
)
from eve_static_data.type_explorer.sde_types import sde_type_info

app = typer.Typer(no_args_is_help=True)

# eve-static-data sde dev dict-sig ~/projects/tmp/sde-download-test/sde-3081406-jsonl -f ~/projects/tmp/sde-download-test/sde-3081406-dict-sig.json -b 3081406


@app.command()
def validate_jsonl(
    sde_directory: Annotated[
        Path, typer.Argument(help="The directory containing the SDE data.")
    ],
    reports_path: Annotated[
        Path,
        typer.Argument(
            help="The directory to write validation results to. Will be created if it doesn't exist."
        ),
    ],
    pydantic: Annotated[
        bool,
        typer.Option(
            "-p",
            "--pydantic",
            help="Validate against the Pydantic models.",
        ),
    ] = True,
    typed_dict: Annotated[
        bool,
        typer.Option(
            "-t",
            "--typed-dict",
            help="Validate against the TypedDict models.",
        ),
    ] = False,
):
    """Validate the jsonl files in a directory against the TypedDict models."""
    console = Console()
    console.print(
        f"[bold green]Validating jsonl files in directory: {sde_directory}[/bold green]"
    )
    now = Instant.now()
    access = SdeReader(sde_path=sde_directory)
    files_check(access=access, reports_path=reports_path, now=now)

    if pydantic:
        pydantic_check(access=access, reports_path=reports_path, now=now)
    if typed_dict:
        typed_dict_check(access=access, reports_path=reports_path, now=now)


def pydantic_check(access: SdeReader, reports_path: Path, now: Instant):
    """Validate the jsonl files against the Pydantic models and write results to disk."""
    console = Console()
    console.print(f"[bold green]Validating against Pydantic models...[/bold green]")
    pydantic_results = validate_sde_pydantic(SdeReader(sde_path=access.sde_path))
    pydantic_output_file = (
        reports_path
        / f"{access.build_number}_pydantic_validation_{file_safe_iso_datetime_string(now.format_iso())}.json"
    )
    try:
        pydantic_results.save_to_disk(pydantic_output_file, overwrite=True)
        console.print(
            f"[bold green]Pydantic validation results written to: {pydantic_output_file}[/bold green]"
        )
    except Exception as e:
        console.print(
            f"[bold red]Error writing Pydantic validation results: {e}[/bold red]"
        )
        raise typer.Exit(code=1) from e
    results_summary(pydantic_results, "Pydantic")


def results_summary(
    validation_result: SDEValidationResult, model_type: Literal["Pydantic", "TypedDict"]
) -> None:
    """Print a summary of the validation results."""
    console = Console()
    console.print(
        f"[bold green]{model_type} Validation Summary for build: {validation_result.build_number}[/bold green]"
    )
    for dataset_name, stats in validation_result.dataset_stats.items():
        if stats.invalid_records > 0:
            console.print(
                f"[bold red]Dataset: {dataset_name}, Total Records: {stats.total_records}, Invalid Records: {stats.invalid_records}[/bold red]"
            )
        else:
            console.print(
                f"[bold green]Dataset: {dataset_name}, Total Records: {stats.total_records}, Invalid Records: {stats.invalid_records}[/bold green]"
            )


def typed_dict_check(access: SdeReader, reports_path: Path, now: Instant):
    """Validate the jsonl files against the TypedDict models and write results to disk."""
    console = Console()
    console.print(f"[bold green]Validating against TypedDict models...[/bold green]")
    typed_dict_results = validate_sde_typeddict(SdeReader(sde_path=access.sde_path))
    typed_dict_output_file = (
        reports_path
        / f"{access.build_number}_typed_dict_validation_{file_safe_iso_datetime_string(now.format_iso())}.json"
    )
    try:
        typed_dict_results.save_to_disk(typed_dict_output_file, overwrite=True)
        console.print(
            f"[bold green]TypedDict validation results written to: {typed_dict_output_file}[/bold green]"
        )
    except Exception as e:
        console.print(
            f"[bold red]Error writing TypedDict validation results: {e}[/bold red]"
        )
        raise typer.Exit(code=1) from e
    results_summary(typed_dict_results, "TypedDict")


def files_check(access: SdeReader, reports_path: Path, now: Instant):
    """Check for missing or extra dataset files and write results to disk."""
    console = Console()
    console.print(
        f"[bold green]Found SDE Build Number: {access.build_number}, release date: {access.release_date}[/bold green]"
    )
    files_report = check_for_dataset_files(access.sde_path)
    files_report_output_file = (
        reports_path
        / f"{access.build_number}_files_report_{file_safe_iso_datetime_string(now.format_iso())}.json"
    )
    files_report.save_to_disk(files_report_output_file, overwrite=True)
    if files_report.missing_files or files_report.extra_files:
        if files_report.missing_files:
            console.print(
                f"[bold red]Missing files: {len(files_report.missing_files)}. See report for details: {files_report_output_file}[/bold red]"
            )
        if files_report.extra_files:
            console.print(
                f"[bold yellow]Extra files: {len(files_report.extra_files)}. See report for details: {files_report_output_file}[/bold yellow]"
            )
    else:
        console.print(
            f"[bold green]All expected files are present and no extra files found. See report for details: {files_report_output_file}[/bold green]"
        )


# TODO Which of these commands is still useful?
# TODO Option to output to a Python file for easy update and comparison of type_def_sig.py
@app.command()
def sde_type_sig(
    sde_directory: Annotated[
        Path, typer.Argument(help="The directory containing the SDE data.")
    ],
    build_number: Annotated[
        str,
        typer.Option("-b", help="The SDE build number of the dataset."),
    ] = "UNDEFINED",
    output_file: Annotated[
        Path | None,
        typer.Option("-f", help="The file to write the generated SDE type sigs to."),
    ] = None,
):
    """Generate SDE type signatures from all the jsonl files in a directory.

    Output defaults to console if no output file is specified.
    """
    pass
    console = Console()
    console.print(
        f"[bold green]Generating SDE type signatures for build: {build_number} at: {sde_directory}[/bold green]"
    )
    sde_sig = sde_type_info(dir_path=sde_directory, build_number=build_number)
    if output_file:
        console.print(f"[bold green]Output file: {output_file}[/bold green]")
        try:
            with output_file.open("w", encoding="utf-8") as f:
                f.write(json.dumps(sde_sig, indent=2, sort_keys=True))
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(code=1) from e
    else:
        console.print(pformat(sde_sig))
        return


@app.command()
def dict_sig(
    sde_directory: Annotated[
        Path, typer.Argument(help="The directory containing the SDE data.")
    ],
    build_number: Annotated[
        str,
        typer.Option("-b", help="The SDE build number of the dataset."),
    ] = "UNDEFINED",
    output_file: Annotated[
        Path | None,
        typer.Option("-f", help="The file to write the generated TypedDicts to."),
    ] = None,
    sde_file: Annotated[
        str,
        typer.Option("-n", help="The SDE file to process."),
    ] = "ALL",
):
    """Generate TypedDict definitions from sample data."""
    pass
    console = Console()
    console.print(
        f"[bold green]Generating TypedDict definitions for file: {sde_file} build: {build_number} at: {sde_directory}[/bold green]"
    )
    files = (
        [SdeDatasetFiles[sde_file.upper()]]
        if sde_file != "ALL"
        else list(SdeDatasetFiles)
    )
    access = SdeReader(sde_path=sde_directory)
    if output_file:
        console.print(f"[bold green]Output file: {output_file}[/bold green]")
        try:
            sde_dict_sigs_to_file(
                sde_directory=sde_directory,
                output_file=output_file,
                build_number=build_number,
            )
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            raise typer.Exit(code=1) from e
        return
    for file_name_enum in files:
        data_iter = access.records(file_name_enum)
        source_info = f"SDE file: {file_name_enum}, build: {build_number}"
        key_info = collect_dict_keys_and_types_recursive(data_iter, source_info)
        console.print(f"[bold blue]Dicionary Sig for {file_name_enum}:[/bold blue]")
        console.print(pformat(key_info))
        console.print("\n")


@app.command()
def generate_typed_dicts(
    sde_directory: Annotated[
        Path, typer.Argument(help="The directory containing the SDE data.")
    ],
    build_number: Annotated[
        str,
        typer.Option("-b", help="The SDE build number of the dataset."),
    ] = "UNDEFINED",
    output_file: Annotated[
        Path | None,
        typer.Option("-f", help="The file to write the generated TypedDicts to."),
    ] = None,
    sde_file: Annotated[
        str,
        typer.Option("-n", help="The SDE file to process."),
    ] = "ALL",
):
    """Generate TypedDict definitions from sample data."""
    pass
    console = Console()
    console.print(
        f"[bold green]Generating TypedDict definitions for file: {sde_file} build: {build_number} at: {sde_directory}[/bold green]"
    )

    if output_file:
        console.print(f"[bold green]Output file: {output_file}[/bold green]")
        try:
            sde_typed_dicts_to_file(
                sde_directory=sde_directory,
                output_file=output_file,
                build_number=build_number,
            )
        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")
            print(e)
            error = typer.Exit(code=1)
            console.print(error)
            raise error from e
        return
    files = (
        [SdeDatasetFiles[sde_file.upper()]]
        if sde_file != "ALL"
        else list(SdeDatasetFiles)
    )
    access = SdeReader(sde_path=sde_directory)
    for file_name_enum in files:
        data_iter = access.records(file_name_enum)
        source_info = f"SDE file: {file_name_enum}, build: {build_number}"
        key_info = collect_dict_keys_and_types_recursive(data_iter, source_info)
        typed_dict = make_typed_dict(
            file_name_enum=file_name_enum, key_info=key_info, source_info=source_info
        )

        console.print(f"[bold blue]TypedDict for {file_name_enum}:[/bold blue]")
        console.print(typed_dict)
        console.print("\n")
