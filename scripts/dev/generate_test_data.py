# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "typer>=0.24.1",
# ]
# ///

from pathlib import Path
from typing import Annotated

import typer

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
    """Generate test data for the database from the SDE jsonl files.

    For each jsonl file int he input directory, copy the first three lines to a new file
    in the output directory with the same name.
    """
    output_directory.mkdir(parents=True, exist_ok=True)
    for jsonl_file in sde_directory.glob("*.jsonl"):
        output_file = output_directory / jsonl_file.name
        with jsonl_file.open("r") as infile, output_file.open("w") as outfile:
            for _ in range(3):
                line = infile.readline()
                if not line:
                    break
                outfile.write(line)


if __name__ == "__main__":
    app()
