"""Temporary markdown renderers for performance reports.

These quick string builders live in the final home for markdown rendering so the
CLI can depend on a stable import path while the implementation later migrates to
Jinja templates.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from pfmsoft.eve_sd.performance.models import (
    DbSourceReport,
    FileSourceReport,
)


def render_files_report_markdown(report: FileSourceReport | dict[str, Any]) -> str:
    """Render a file-backed performance report to markdown text."""
    report_data = report if isinstance(report, dict) else asdict(report)
    lines = [
        "# SDE performance report",
        "",
        f"- source type: {report_data.get('source_type', 'files')}",
        f"- source path: {report_data.get('source_path', 'unknown')}",
        f"- generated at: {report_data.get('generated_at', 'unknown')}",
        f"- total seconds: {report_data.get('total_seconds', 'unknown')}",
        f"- deserialization method: {report_data.get('deserialization_method', 'unknown')}",
        "",
        "## Datasets",
        "",
    ]
    for dataset in report_data.get("datasets", []):
        lines.extend([
            f"### {dataset.get('dataset_name', 'unknown')}",
            "",
            f"- record_count: {dataset.get('record_count', 'unknown')}",
            f"- total_seconds: {dataset.get('total_seconds', 'unknown')}",
            f"- key_type: {dataset.get('key_type', 'unknown')}",
            f"- file_size_bytes: {dataset.get('file_size_bytes', 'unknown')}",
            "",
        ])
    return "\n".join(lines)


def render_db_report_markdown(report: DbSourceReport | dict[str, Any]) -> str:
    """Render a database-backed performance report to markdown text."""
    report_data = report if isinstance(report, dict) else asdict(report)
    lines = [
        "# SDE performance report",
        "",
        f"- source type: {report_data.get('source_type', 'db')}",
        f"- source path: {report_data.get('source_path', 'unknown')}",
        f"- generated at: {report_data.get('generated_at', 'unknown')}",
        f"- total seconds: {report_data.get('total_seconds', 'unknown')}",
        f"- serialization_format: {report_data.get('serialization_format', 'unknown')}",
        "",
        "## Datasets",
        "",
    ]
    for dataset in report_data.get("datasets", []):
        lines.extend([
            f"### {dataset.get('dataset_name', 'unknown')}",
            "",
            f"- record_count: {dataset.get('record_count', 'unknown')}",
            f"- total_seconds: {dataset.get('total_seconds', 'unknown')}",
            f"- dataset_load_seconds: {dataset.get('dataset_load_seconds', 'unknown')}",
            f"- all_dataset_keys_seconds: {dataset.get('all_dataset_keys_seconds', 'unknown')}",
            f"- random_record_access_seconds: {dataset.get('random_record_access_seconds', 'unknown')}",
            f"- random_record_access_sample_size: {dataset.get('random_record_access_sample_size', 'unknown')}",
            f"- key_type: {dataset.get('key_type', 'unknown')}",
            "",
        ])
    return "\n".join(lines)
