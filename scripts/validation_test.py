from pathlib import Path
from typing import Annotated, Any

import typer

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.access.validation import SDEValidationResult, validate_dataset
from eve_static_data.models.sde_datasets import SdeDatasets

app = typer.Typer()


# typer /home/chad/projects/eve-static-data/scripts/validation_test.py run ~/tmp/static-data-3201939-jsonl/
@app.command()
def validate(
    path_in: Annotated[Path, typer.Argument(..., help="Path to the input file")],
):
    """Validate the SDE dataset."""
    access = SdeReader(path_in)
    sde_info: dict[str, Any] = next(
        iter(access.records(SdeDatasets.SDE_INFO))
    )  # Get the first (and only) record from _sde.jsonl
    validator = SDEValidationResult(
        build_number=sde_info["buildNumber"],
        release_date=sde_info["releaseDate"],
        dataset_stats={},
    )
    dataset = SdeDatasets.AGENTS_IN_SPACE
    validator.dataset_stats[dataset.value] = validate_dataset(access, dataset)

    print(validator.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
