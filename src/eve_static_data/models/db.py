"""SQLAlchemy models for the EVE Static Data application.

CamelCase is used for database column names to match the naming convention used in the SDE.
This allows for easier mapping between the SDE data and the database models.

The `_key` field in the SDE jsonl data is renamed to `key` due to issues with pydantic.
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class AppInfo(Base):
    """Information on the creating application and the import date.

    This is set during database creation, with the assumption that the data will be
    imported immediately after.
    """

    __tablename__ = "app_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    version: Mapped[str] = mapped_column()
    import_date: Mapped[str] = mapped_column()


class SdeInfo(Base):
    __tablename__ = "sde_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column()
    buildNumber: Mapped[int] = mapped_column()
    releaseDate: Mapped[str] = mapped_column()
