"""Jinja-based markdown renderers for performance reports."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from jinja2 import Environment, PackageLoader

from pfmsoft.eve_sd.performance.models import (
    DbSourceReport,
    FileSourceReport,
)


def _decimal_string(value: float | int | str | None) -> str:
    """Render a number in fixed-point decimal form without scientific notation."""
    if value is None:
        return "unknown"
    decimal_value = Decimal(str(value))
    text = format(decimal_value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text else "0"


def _build_environment() -> Environment:
    """Build the Jinja environment for markdown performance templates."""
    environment = Environment(
        loader=PackageLoader("pfmsoft.eve_sd", "templates"),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    environment.filters["decimal"] = _decimal_string
    return environment


def render_files_report_markdown(report: FileSourceReport | dict[str, Any]) -> str:
    """Render a file-backed performance report to markdown using a Jinja template."""
    environment = _build_environment()
    template = environment.get_template("performance/file_report.j2")
    return template.render(report=report)


def render_db_report_markdown(report: DbSourceReport | dict[str, Any]) -> str:
    """Render a DB-backed performance report to markdown using a Jinja template."""
    environment = _build_environment()
    template = environment.get_template("performance/db_report.j2")
    return template.render(report=report)
