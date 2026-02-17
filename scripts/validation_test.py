from pathlib import Path
from typing import Annotated, Any

import typer

from eve_static_data.access.sde_reader import SdeReader
from eve_static_data.access.validation import (
    SDEValidationResult,
    check_for_dataset_files,
    validate_dataset_pydantic,
    validate_dataset_typeddict,
)
from eve_static_data.models.sde_dataset_files import SdeDatasetFiles

app = typer.Typer()


# typer /home/chad/projects/eve-static-data/scripts/validation_test.py run ~/tmp/static-data-3201939-jsonl/
@app.command()
def validate(
    path_in: Annotated[Path, typer.Argument(..., help="Path to the input file")],
):
    """Validate the SDE dataset."""
    typer.echo("\n\nChecking for expected dataset files...\n\n")
    file_check_result = check_for_dataset_files(path_in)
    print(file_check_result.model_dump_json(indent=2))

    access = SdeReader(path_in)
    sde_info: dict[str, Any] = next(
        iter(access.records(SdeDatasetFiles.SDE_INFO))
    )  # Get the first (and only) record from _sde.jsonl
    validator_pydantic = SDEValidationResult(
        build_number=sde_info["buildNumber"],
        release_date=sde_info["releaseDate"],
        dataset_stats={},
    )
    typer.echo("\n\nValidating with pydantic models...\n\n")
    dataset = SdeDatasetFiles.AGENTS_IN_SPACE
    validator_pydantic.dataset_stats[dataset.value] = validate_dataset_pydantic(
        access, dataset
    )
    print(validator_pydantic.model_dump_json(indent=2))

    typer.echo("\n\nNow validating with TypedDict models...\n\n")
    validator_typeddict = SDEValidationResult(
        build_number=sde_info["buildNumber"],
        release_date=sde_info["releaseDate"],
        dataset_stats={},
    )
    dataset = SdeDatasetFiles.AGENTS_IN_SPACE
    validator_typeddict.dataset_stats[dataset.value] = validate_dataset_typeddict(
        access, dataset
    )
    print(validator_typeddict.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
