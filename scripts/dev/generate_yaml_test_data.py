# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pyyaml>=6.0.3",
#     "typer>=0.24.1",
# ]
# ///

import json
from pathlib import Path
from time import perf_counter
from typing import Annotated, Any

import typer
from yaml import safe_dump, safe_load

app = typer.Typer(no_args_is_help=True)


@app.command()
def main(
    sde_directory: Annotated[
        Path, typer.Argument(..., help="Path to the SDE directory")
    ],
    output_directory: Annotated[
        Path, typer.Argument(..., help="Path to the output directory")
    ],
) -> None:
    """Generate test data for the database from the SDE YAML files.

    For each YAML file in the input directory, copy the first three records to a new file
    in the output directory with the same name.
    """
    output_directory.mkdir(parents=True, exist_ok=True)
    yaml_directory = output_directory / "yaml"
    yaml_directory.mkdir(parents=True, exist_ok=True)
    json_directory = output_directory / "json"
    json_directory.mkdir(parents=True, exist_ok=True)
    for yaml_input_file in sde_directory.glob("*.yaml"):
        yaml_output_file = yaml_directory / yaml_input_file.name
        json_output_file = json_directory / yaml_input_file.with_suffix(".json").name
        print(f"Processing {yaml_input_file}...")
        start = perf_counter()
        with (
            yaml_input_file.open("r") as infile,
            yaml_output_file.open("w") as yaml_file_handle,
            json_output_file.open("w") as json_file_handle,
        ):
            data: dict[int, Any] = safe_load(infile)
            if not isinstance(data, dict):
                print(
                    f"Skipping {yaml_input_file} because it does not contain a dictionary at the top level."
                )
                continue
            result_dict = {}
            first_three_keys: list[int] = list(data.keys())[:3]
            for record_key in first_three_keys:
                result_dict[record_key] = data[record_key]
            safe_dump(result_dict, yaml_file_handle)
            json_file_handle.write(json.dumps(result_dict, indent=2))
        print(
            f"Finished processing {yaml_input_file} in {perf_counter() - start:.2f} seconds."
        )


if __name__ == "__main__":
    app()
