"""CLI commands for SDE development tasks."""

import json
from pathlib import Path
from pprint import pformat
from typing import Annotated

import typer
from rich.console import Console

from eve_static_data.access.sde_reader import SdeReader

# from eve_static_data.access.raw_json_td import RawJsonFileAccessValidator
from eve_static_data.helpers.dict_diagnostics import (
    collect_dict_keys_and_types_recursive,
)
from eve_static_data.helpers.sde_dict_sigs import sde_dict_sigs_to_file
from eve_static_data.helpers.sde_typed_dicts_to_file import (
    make_typed_dict,
    sde_typed_dicts_to_file,
)
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles
from eve_static_data.type_explorer.sde_types import sde_type_info

app = typer.Typer(no_args_is_help=True)

# eve-static-data sde dev dict-sig ~/projects/tmp/sde-download-test/sde-3081406-jsonl -f ~/projects/tmp/sde-download-test/sde-3081406-dict-sig.json -b 3081406


# @app.command()
# def validate_jsonl(
#     sde_directory: Annotated[
#         Path, typer.Argument(help="The directory containing the SDE data.")
#     ],
# ):
#     """Validate the jsonl files in a directory against the TypedDict models."""
#     console = Console()
#     console.print(
#         f"[bold green]Validating jsonl files in directory: {sde_directory}[/bold green]"
#     )
#     validator = RawJsonFileAccessValidator(dir_path=sde_directory)
#     validator.validate_all()
#     if validator.validation_errors:
#         console.print(
#             f"[bold red]Validation completed with {len(validator.validation_errors)} errors:[/bold red]"
#         )
#         console.print(f"[bold red]See logs for more details.[/bold red]")
#         for error in validator.validation_errors:
#             console.print(f"[bold red]{error.source} {error.error}[/bold red]")


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
