"""Functions for working with the database."""

from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import Session
from whenever import Instant

import eve_static_data.models.db as DBM
from eve_static_data import __app_name__, __version__


def engine_factory(db_path: str, echo: bool = True) -> Engine:
    """Create a SQLAlchemy engine for the given database path.

    Args:
        db_path (str): The file path to the SQLite database. Use `:memory:` for an in-memory database.
        echo (bool): If True, the engine will log all statements. Defaults to True.

    Returns:
        Engine: A SQLAlchemy engine instance.
    """
    print(f"Creating engine for database at: {db_path}")
    return create_engine(f"sqlite+pysqlite:///{db_path}", echo=echo)


def create_db(engine: Engine):
    """Create the database tables.

    Args:
        engine (Engine): The SQLAlchemy engine to use for creating the database.
    """
    # TODO: Add error handling for database creation
    # TODO: Error if the database already exists and is not empty
    # This will create the tables defined in the Base metadata. If the tables already exist, it will not overwrite them.
    DBM.Base.metadata.create_all(engine)
    with Session(engine) as session:
        app_info = DBM.AppInfo(
            name=__app_name__,
            version=__version__,
            import_date=Instant.now().format_rfc2822(),
        )
        session.add(app_info)
        session.commit()


def db_exists(engine: Engine) -> bool:
    """Check if the database exists and has the necessary tables.

    Args:
        engine (Engine): The SQLAlchemy engine to use for checking the database.

    Returns:
        bool: True if the database exists and has the necessary tables, False otherwise.
    """
    try:
        with Session(engine) as session:
            app_info = session.execute(select(DBM.AppInfo)).scalar_one_or_none()
            return app_info is not None
    except Exception:
        return False
