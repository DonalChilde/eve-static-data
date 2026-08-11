"""Schema inspection utilities and report models."""

from .models import (
    DatasetInspection,
    PathInspection,
    SchemaReport,
)
from .render import generate_markdown_report
from .report import DatasetInput, build_schema_report, inspect_dataset_data
from .report_from_db import get_schema_report_from_db
from .report_from_files import (
    get_json_schema_report,
    get_jsonl_schema_report,
    get_yaml_schema_report,
)

__all__ = [
    "DatasetInput",
    "DatasetInspection",
    "PathInspection",
    "SchemaReport",
    "build_schema_report",
    "generate_markdown_report",
    "get_json_schema_report",
    "get_jsonl_schema_report",
    "get_schema_report_from_db",
    "get_yaml_schema_report",
    "inspect_dataset_data",
]
