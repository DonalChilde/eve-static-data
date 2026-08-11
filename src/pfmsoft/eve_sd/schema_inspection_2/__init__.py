"""Schema inspection v2 — tree-structured output with canonical type derivation."""

from .inspect import DatasetInput, build_schema_report, inspect_dataset_data
from .models import (
    DatasetSchema,
    FieldSchema,
    FieldSection,
    SchemaReport2,
    build_sections,
    canonical_type,
    flat_fields,
)
from .render import generate_markdown_report
from .report_from_files import (
    get_json_schema_report,
    get_jsonl_schema_report,
    get_yaml_schema_report,
)

__all__ = [
    "DatasetInput",
    "DatasetSchema",
    "FieldSchema",
    "FieldSection",
    "SchemaReport2",
    "build_schema_report",
    "build_sections",
    "canonical_type",
    "flat_fields",
    "generate_markdown_report",
    "get_json_schema_report",
    "get_jsonl_schema_report",
    "get_yaml_schema_report",
    "inspect_dataset_data",
]
