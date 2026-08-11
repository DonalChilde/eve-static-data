"""Markdown rendering for schema inspection v2 reports."""

from jinja2 import Environment, PackageLoader
from mdformat import text as mdformat_text  # type: ignore

from pfmsoft.eve_sd.schema_inspection_2.models import (
    SchemaReport2,
    build_sections,
    canonical_type,
    flat_fields,
)


def _build_environment() -> Environment:
    env = Environment(
        loader=PackageLoader("pfmsoft.eve_sd", "templates"),
        autoescape=False,
        trim_blocks=True,  # strip the newline after each block tag
        lstrip_blocks=True,  # strip leading whitespace before block tags
    )
    env.globals["build_sections"] = build_sections
    env.globals["canonical_type"] = canonical_type
    env.globals["flat_fields"] = flat_fields
    return env


def generate_markdown_report(report: SchemaReport2) -> str:
    """Render a human-readable markdown schema report (v2).

    Args:
        report: Schema report from one or more datasets.

    Returns:
        Markdown text with tree-structured field tables per dataset.
    """
    environment = _build_environment()
    template = environment.get_template("schema_inspection_2/markdown_report.j2")
    rendered = template.render(report=report)
    return mdformat_text(rendered, extensions=["tables"])
