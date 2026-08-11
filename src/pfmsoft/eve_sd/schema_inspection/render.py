"""Markdown rendering for schema inspection reports."""

from jinja2 import Environment, PackageLoader
from mdformat import text as mdformat_text  # type: ignore

from pfmsoft.eve_sd.schema_inspection.models import SchemaReport


def _build_environment() -> Environment:
    return Environment(
        loader=PackageLoader("pfmsoft.eve_sd", "templates"),
        autoescape=False,
    )


def generate_markdown_report(report: SchemaReport) -> str:
    """Render a human-readable markdown schema report.

    Args:
        report: Schema report from one or more datasets.

    Returns:
        Markdown text with a summary and per-dataset sections.
    """
    environment = _build_environment()
    template = environment.get_template("schema_inspection/markdown_report.j2")
    rendered = template.render(report=report)
    return mdformat_text(rendered, extensions=["tables"])
