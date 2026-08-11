"""Schema report v2 command group."""

import typer

from pfmsoft.eve_sd.cli.schema.report2.files import app as report2_files_app

app = typer.Typer(
    no_args_is_help=True,
    help="Generate v2 schema reports (tree-structured, with canonical type annotations).",
)

app.add_typer(
    report2_files_app,
    help="Generate v2 schema reports by reading local dataset files.",
)
