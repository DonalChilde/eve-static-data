"""Generate schema v2 reports from an SDE SQLite database."""

import sqlite3
from collections.abc import Iterable

from pfmsoft.eve_sd.db.query import DatasetDbQuery
from pfmsoft.eve_sd.schema_inspection.inspect import DatasetInput, build_schema_report
from pfmsoft.eve_sd.schema_inspection.models import SchemaReport


def get_schema_report_from_db(connection: sqlite3.Connection) -> SchemaReport:
    """Generate a v2 schema report from all datasets in a sqlite database."""
    db_query = DatasetDbQuery(connection)
    sde_metadata = db_query.sde_metadata

    def dataset_input_generator() -> Iterable[DatasetInput]:
        for dataset_name, key_type in db_query.dataset_key_types.items():
            if key_type == "int":
                data = db_query.get_int_records(dataset_name)
            elif key_type == "str":
                data = db_query.get_str_records(dataset_name)
            else:
                raise ValueError(
                    f"Unexpected key type '{key_type}' for dataset '{dataset_name}'."
                )
            yield DatasetInput(
                dataset_name=dataset_name,
                dataset_data={k: v for k, v in data},
                sde_metadata=sde_metadata,
            )

    return build_schema_report(
        datasets=dataset_input_generator(),
        sde_metadata=sde_metadata,
        dataset_source=str(connection),
    )
