# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
import logging
from pathlib import Path
from typing import Annotated

from typer import Typer

from eve_static_data import ESDLoader
from eve_static_data.logging_config import setup_logging

logger = logging.getLogger(__name__)
log_dir = Path("~/tmp/logs/esd-export-script").expanduser()
setup_logging(log_dir=log_dir)
app = Typer(no_args_is_help=True)


@app.command()
def export(sde_path: Annotated[Path, "Path to the SDE directory"]):
    """Export the SDE data to JSON format."""
    loader = ESDLoader(
        sde_path=sde_path, derived_datasets_path=sde_path / "derived_datasets"
    )
    # eve_types_localized = loader.localized_datasets.eve_types()
    # print(f"Exported {len(eve_types_localized.records)} EVE types.")

    market_paths = loader.derived_datasets.market_paths()
    print(f"Exported {len(market_paths.records)} market paths.")
    eve_types = loader.derived_datasets.normalized_eve_types()
    print(f"Exported {len(eve_types.records)} normalized EVE types.")
    region_names = loader.derived_datasets.region_names()
    print(f"Exported {len(region_names.records)} region names.")
    system_names = loader.derived_datasets.system_names()
    print(f"Exported {len(system_names.records)} system names.")


if __name__ == "__main__":
    app()
    # typer ./scripts/exports.py run ~/tmp/esd/3279491 export
