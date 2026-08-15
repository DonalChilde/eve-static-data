"""CLI tools for interacting with the EVE Static Data Export (SDE).

When using the eve-sd command line app as part of a third party cli, import
the app object from this module and add it to your own Typer app using the
add_typer() method. For example:

```python
import typer
from pfmsoft.eve_sd.cli import app as eve_sd_app

app = typer.Typer()
app.add_typer(eve_sd_app, name="eve-sd")
```
"""

import typer

from pfmsoft.eve_sd.cli.db import app as sde_import_app
from pfmsoft.eve_sd.cli.dev import app as dev_app
from pfmsoft.eve_sd.cli.docs import app as docs_app
from pfmsoft.eve_sd.cli.export import app as sde_export_app
from pfmsoft.eve_sd.cli.fetch import app as fetch_app
from pfmsoft.eve_sd.cli.schema import app as schema_app
from pfmsoft.eve_sd.cli.unpack_sde import app as unpack_app
from pfmsoft.eve_sd.cli.version import app as version_app
from pfmsoft.eve_sd.cli.view_settings import app as view_settings_app

app = typer.Typer(
    no_args_is_help=True,
    help="Work with EVE Online static data: fetch releases, unpack datasets, build/query "
    "databases, export formats, and inspect schemas.",
)
app.add_typer(fetch_app, name="fetch")
app.add_typer(unpack_app)
app.add_typer(sde_import_app, name="db")
app.add_typer(sde_export_app, name="export")

app.add_typer(schema_app, name="schema")
app.add_typer(dev_app, name="dev")

app.add_typer(version_app)
app.add_typer(view_settings_app)
app.add_typer(docs_app)
