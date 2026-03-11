# EVE Static Data - A cli and API for downloading and accessing the EVE Online Static Data files.

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Project Description

eve-static-data provides a cli to check the status of the latest release of the EVE Online Static Data dataset. It supports downloading, expanding, and iterating over the various files in the dataset.

### CLI commands for downloading and processing SDE.

### Provides Pydantic models for SDE data.

### Provides localized datasets.

### Validation report, structure information.

### Derived datasets for easy use.

### Easy access functions for programatic usage.

TODO - More complete instructions and examples as the program evolves.

## Quick Start

## Usage

## API Usage

## Installation

This project uses uv for development, and uv is also the easiest way to run the project.

> uv docs:  
> [Astral - uv](https://docs.astral.sh/uv/)  
> [https://docs.astral.sh/uv/concepts/tools/](https://docs.astral.sh/uv/concepts/tools/)  
> [https://docs.astral.sh/uv/reference/cli/#uv-tool](https://docs.astral.sh/uv/reference/cli/#uv-tool)  
> [https://docs.astral.sh/uv/pip/packages/#installing-a-package](https://docs.astral.sh/uv/pip/packages/#installing-a-package)  
> [https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)

To run with uv:

> Note the url format for tool install is the same as that for uv pip install:

```bash
# run eve-static-data without installing
uvx --from git+https://github.com/DonalChilde/eve-static-data@main esd

# OR

# Install to Path
uv tool install --from git+https://github.com/DonalChilde/eve-static-data@main eve-static-data
# and run
esd ARGS
```

## Development

### Download the source code:

```bash
git clone https://github.com/DonalChilde/eve-static-data.git
cd eve-static-data
uv sync
# activate the venv if desired
source ./.venv/bin/activate
```

### Use as a dependency in another project:

```toml
# in your pyproject.toml file, for a uv managed project
dependencies = ["eve-static-data"]
[tool.uv.sources]
eve-static-data = { git = "https://github.com/DonalChilde/eve-static-data", branch = "main" }
```

### ruff settings for formatting and linting

See pyproject.toml file

## Contributing

## License

MIT License - see LICENSE file for details.

## Support

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
