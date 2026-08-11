"""Generate schema v2 reports by inspecting local SDE dataset files."""

import dataclasses
import json
from pathlib import Path
from typing import Annotated

import typer
from pfmsoft.eve_snippets import save_text_file
from rich.console import Console

from pfmsoft.eve_sd.cli.helpers import ReportChoice
from pfmsoft.eve_sd.helpers.sde_metadata import SourceMedia, load_sde_metadata
from pfmsoft.eve_sd.schema_inspection_2 import (
    generate_markdown_report,
    get_json_schema_report,
    get_jsonl_schema_report,
    get_yaml_schema_report,
)

app = typer.Typer(no_args_is_help=True)


@app.command(name="files")
def report2_files(
    from_directory: Annotated[
        Path,
        typer.Option(
            "--from",
            help="The path to the directory containing the SDE dataset files.",
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
    to_directory: Annotated[
        Path | None,
        typer.Option(
            "--to",
            help="The directory to save the schema report to.",
            file_okay=False,
            dir_okay=True,
        ),
    ] = None,
    stdout_format: Annotated[
        ReportChoice,
        typer.Option(
            "--stdout-format",
            help="The format of the schema report to print to stdout.",
            case_sensitive=False,
            show_default=True,
        ),
    ] = ReportChoice.MARKDOWN,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite existing report files when writing output.",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            help="Suppress output messages.",
        ),
    ] = False,
) -> None:
    """Generate a v2 schema report from local datasets in one directory."""
    messenger = Console(stderr=True, quiet=quiet)
    stdout = Console()
    try:
        sde_metadata = load_sde_metadata(from_directory)
    except (FileNotFoundError, ValueError) as exc:
        raise typer.BadParameter(str(exc)) from exc

    messenger.print(
        f"[bold green]Generating schema report (v2) for {from_directory}[/bold green]"
    )

    match sde_metadata.source_media:
        case SourceMedia.YAML:
            schema_report = get_yaml_schema_report(from_directory)
        case SourceMedia.JSONL:
            schema_report = get_jsonl_schema_report(from_directory)
        case SourceMedia.JSON:
            schema_report = get_json_schema_report(from_directory)
        case _:
            raise typer.BadParameter(
                f"Unsupported source media {sde_metadata.source_media!r}."
            )

    markdown_report = generate_markdown_report(schema_report)
    match stdout_format:
        case ReportChoice.JSON:
            stdout.print(
                json.dumps(dataclasses.asdict(schema_report), indent=2, default=str)
            )
        case ReportChoice.MARKDOWN:
            stdout.print(markdown_report)
        case ReportChoice.NONE:
            pass

    if to_directory is None:
        return

    build_number = sde_metadata.buildNumber
    format_name = sde_metadata.variant.value
    json_file_name = f"schema_report2_{format_name}_{build_number}.json"
    markdown_file_name = f"schema_report2_{format_name}_{build_number}.md"
    save_text_file(
        text=json.dumps(dataclasses.asdict(schema_report), indent=2, default=str),
        directory=to_directory,
        filename=json_file_name,
        overwrite=overwrite,
    )
    save_text_file(
        text=markdown_report,
        directory=to_directory,
        filename=markdown_file_name,
        overwrite=overwrite,
    )
    messenger.print(
        f"[bold green]Report saved to {to_directory} as {json_file_name} and {markdown_file_name}[/bold green]"
    )
