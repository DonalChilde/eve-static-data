"""Performance report commands for file-based and DB-based SDE access."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Literal

import typer
from pfmsoft.eve_snippets.typer.output import output_to_stdout_or_file
from rich.console import Console

from pfmsoft.eve_sd.performance.generate_reports import (
    generate_db_report,
    generate_files_report,
)
from pfmsoft.eve_sd.performance.models import (
    DbSourceReport,
    FileSourceReport,
)
from pfmsoft.eve_sd.performance.renderers import (
    render_db_report_markdown,
    render_files_report_markdown,
)

app = typer.Typer(no_args_is_help=True, help="Generate and render performance reports.")


def _report_json_filename(
    source_type: str,
    build_number: int,
    report_type: Literal["files", "db"],
) -> str:
    """Return a default filename for a JSON report."""
    return f"performance_report_{source_type}_build_{build_number}_{report_type}.json"


def _report_markdown_filename(
    source_type: str, build_number: int, report_type: Literal["files", "db"]
) -> str:
    """Return a default filename for a markdown report."""
    return f"performance_report_{source_type}_build_{build_number}_{report_type}.md"


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
    ] = 2,
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
            filename = _report_json_filename(report.source_type, build_number, "files")
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
    ] = 2,
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
            filename = _report_json_filename(report.source_type, build_number, "db")
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=report.serialize(indent=indent),
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )


@app.command(name="report-files-markdown")
def report_files_markdown(
    report_json: Annotated[
        Path,
        typer.Option(
            "--from",
            help="Path to a file-backed JSON performance report to render as markdown.",
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
    """Render a file-backed JSON performance report as markdown."""
    if quiet:
        messenger = Console(stderr=True, quiet=True)
    else:
        messenger = Console(stderr=True)
    json_string = report_json.read_text(encoding="utf-8")
    report = FileSourceReport.deserialize(json_string)
    build_number = report.sde_metadata.buildNumber if report.sde_metadata else 0
    markdown_text = render_files_report_markdown(report)
    if output == Path("-"):
        output_path = output
    else:
        if filename is None:
            filename = _report_markdown_filename(
                report.source_type, build_number, "files"
            )
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=markdown_text,
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )


@app.command(name="report-db-markdown")
def report_db_markdown(
    report_json: Annotated[
        Path,
        typer.Option(
            "--from",
            help="Path to a DB-backed JSON performance report to render as markdown.",
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
    """Render a DB-backed JSON performance report as markdown."""
    if quiet:
        messenger = Console(stderr=True, quiet=True)
    else:
        messenger = Console(stderr=True)
    json_string = report_json.read_text(encoding="utf-8")
    report = DbSourceReport.deserialize(json_string)
    build_number = report.sde_metadata.buildNumber if report.sde_metadata else 0
    markdown_text = render_db_report_markdown(report)
    if output == Path("-"):
        output_path = output
    else:
        if filename is None:
            filename = _report_markdown_filename(report.source_type, build_number, "db")
        output_path = output / filename
    output_to_stdout_or_file(
        data_string=markdown_text,
        filepath=output_path,
        overwrite=overwrite,
        messenger=messenger,
    )
