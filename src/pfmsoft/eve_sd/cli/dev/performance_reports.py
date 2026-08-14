"""Performance report commands for file-based and DB-based SDE access."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from pfmsoft.eve_snippets.typer.output import output_to_stdout_or_file
from rich.console import Console

from pfmsoft.eve_sd.performance.generate_reports import (
    generate_db_report,
    generate_files_report,
    render_report_markdown,
)
from pfmsoft.eve_sd.performance.models import SourceReport

app = typer.Typer(no_args_is_help=True, help="Generate and render performance reports.")


def _default_report_filename(
    source_type: str, build_number: int, extension: str
) -> str:
    """Return a default filename that includes the build number and source kind."""
    return f"performance_report_{source_type}_build_{build_number}{extension}"


@app.command(name="report-files")
def report_files(
    source_dir: Annotated[
        Path,
        typer.Option(
            "--from",
            help="Directory containing datasets to benchmark as files.",
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Option(
            "--to",
            help="Directory to save the JSON report to, or '-' for stdout.",
            exists=False,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("-"),
    filename: Annotated[
        str | None,
        typer.Option(
            "--filename",
            help="Optional filename to use when writing a report to a directory.",
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite the output report file if it already exists.",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            help="Suppress messages.",
            show_default=True,
        ),
    ] = False,
    indent: Annotated[
        int | None,
        typer.Option(
            "--indent",
            help="Number of spaces to use for JSON indentation.",
            show_default=True,
        ),
    ] = None,
) -> None:
    """Generate a JSON performance report from filesystem-backed datasets."""
    if quiet:
        messenger = Console(stderr=True, quiet=True)
    else:
        messenger = Console(stderr=True)
    report = generate_files_report(source_dir)
    build_number = report.sde_metadata.buildNumber if report.sde_metadata else 0
    if output == Path("-"):
        output_path = output
    else:
        output = output.expanduser()
        if output.exists() and not output.is_dir():
            raise typer.BadParameter(
                "The --to value must be '-' or a directory path when writing a report."
            )
        output.mkdir(parents=True, exist_ok=True)
        if filename is None:
            filename = _default_report_filename("files", build_number, ".json")
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=report.serialize(indent=indent),
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )


@app.command(name="report-db")
def report_db(
    source_db: Annotated[
        Path,
        typer.Option(
            "--from",
            help="Path to the SQLite database to benchmark.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Option(
            "--to",
            help="Directory to save the JSON report to, or '-' for stdout.",
            exists=False,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("-"),
    filename: Annotated[
        str | None,
        typer.Option(
            "--filename",
            help="Optional filename to use when writing a report to a directory.",
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite the output report file if it already exists.",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            help="Suppress messages.",
            show_default=True,
        ),
    ] = False,
    indent: Annotated[
        int | None,
        typer.Option(
            "--indent",
            help="Number of spaces to use for JSON indentation.",
            show_default=True,
        ),
    ] = None,
) -> None:
    """Generate a JSON performance report from SQLite-backed datasets."""
    if quiet:
        messenger = Console(stderr=True, quiet=True)
    else:
        messenger = Console(stderr=True)
    report = generate_db_report(source_db)
    build_number = report.sde_metadata.buildNumber if report.sde_metadata else 0
    if output == Path("-"):
        output_path = output
    else:
        output = output.expanduser()
        if output.exists() and not output.is_dir():
            raise typer.BadParameter(
                "The --to value must be '-' or a directory path when writing a report."
            )
        output.mkdir(parents=True, exist_ok=True)
        if filename is None:
            filename = _default_report_filename("db", build_number, ".json")
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=report.serialize(indent=indent),
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )


@app.command(name="render-report")
def render_report(
    report_json: Annotated[
        Path,
        typer.Option(
            "--from",
            help="Path to the JSON performance report to render as markdown.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    output: Annotated[
        Path,
        typer.Option(
            "--to",
            help="Directory to save the markdown report to, or '-' for stdout.",
            exists=False,
            file_okay=False,
            dir_okay=True,
        ),
    ] = Path("-"),
    filename: Annotated[
        str | None,
        typer.Option(
            "--filename",
            help="Optional filename to use when writing a markdown report to a directory.",
        ),
    ] = None,
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite the output report file if it already exists.",
        ),
    ] = False,
    quiet: Annotated[
        bool,
        typer.Option(
            "--quiet",
            help="Suppress messages.",
            show_default=True,
        ),
    ] = False,
) -> None:
    """Render a JSON performance report as markdown."""
    if quiet:
        messenger = Console(stderr=True, quiet=True)
    else:
        messenger = Console(stderr=True)
    report = SourceReport.deserialize(report_json.read_text(encoding="utf-8"))
    markdown = render_report_markdown(report)
    build_number = report.sde_metadata.buildNumber if report.sde_metadata else 0
    if output == Path("-"):
        output_path = output
    else:
        output = output.expanduser()
        if output.exists() and not output.is_dir():
            raise typer.BadParameter(
                "The --to value must be '-' or a directory path when writing a report."
            )
        output.mkdir(parents=True, exist_ok=True)
        if filename is None:
            filename = _default_report_filename(report.source_type, build_number, ".md")
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=markdown,
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )
