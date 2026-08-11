"""Schema-related CLI command groups."""

import typer

from pfmsoft.eve_sd.cli.schema.export import app as export_app
from pfmsoft.eve_sd.cli.schema.report import app as report_app
from pfmsoft.eve_sd.cli.schema.report2 import app as report2_app

app = typer.Typer(
    no_args_is_help=True,
    help="Inspect, report, and export schema information from SDE datasets.",
)

app.add_typer(export_app, name="export", help="Commands for exporting schema data.")
app.add_typer(report_app, name="report", help="Commands for generating schema reports.")
app.add_typer(
    report2_app,
    name="report2",
    help="Generate v2 schema reports with canonical type annotations.",
)
