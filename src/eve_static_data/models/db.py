"""SQLAlchemy models for the EVE Static Data application.

CamelCase is used for database column names to match the naming convention used in the SDE.
This allows for easier mapping between the SDE data and the database models.

The `_key` field in the SDE jsonl data is renamed to `key` due to issues with pydantic.
"""

from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# -------------------------------------------------------------------------------
# Common models
# -------------------------------------------------------------------------------


# class LocalizedString(Base):
#     """A localized string with translations for different languages.

#     This is used for fields that have translations in the SDE, such as item names and descriptions.
#     """

#     __tablename__ = "localized_strings"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     en: Mapped[str] = mapped_column()
#     de: Mapped[str] = mapped_column()
#     fr: Mapped[str] = mapped_column()
#     ja: Mapped[str] = mapped_column()
#     zh: Mapped[str] = mapped_column()
#     ru: Mapped[str] = mapped_column()
#     ko: Mapped[str] = mapped_column()
#     es: Mapped[str] = mapped_column()


# class Materials(Base):
#     """A quantity of materials."""

#     __tablename__ = "materials"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     typeID: Mapped[int] = mapped_column()
#     quantity: Mapped[int] = mapped_column()


# class SkillRequirement(Base):
#     """A skill requirement for a blueprint or item."""

#     __tablename__ = "skill_requirement"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     typeID: Mapped[int] = mapped_column()
#     level: Mapped[int] = mapped_column()


# class Color(Base):
#     """A color with RGB values."""

#     __tablename__ = "color"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     r: Mapped[int] = mapped_column()
#     g: Mapped[int] = mapped_column()
#     b: Mapped[int] = mapped_column()


# class Position(Base):
#     """A position in 3D space."""

#     __tablename__ = "position"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     x: Mapped[float] = mapped_column()
#     y: Mapped[float] = mapped_column()
#     z: Mapped[float] = mapped_column()


# -------------------------------------------------------------------------------
# SDE-specific models
# -------------------------------------------------------------------------------


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
    key: Mapped[int] = mapped_column()
    buildNumber: Mapped[int] = mapped_column()
    releaseDate: Mapped[str] = mapped_column()


class AgentsInSpace(Base):
    __tablename__ = "agents_in_space"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[int] = mapped_column()
    dungeonID: Mapped[int] = mapped_column()
    solarSystemID: Mapped[int] = mapped_column()
    spawnPointID: Mapped[int] = mapped_column()
    typeID: Mapped[int] = mapped_column()


class AgentTypes(Base):
    __tablename__ = "agent_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column()


class Ancestries_Description(Base):
    __tablename__ = "ancestries_description"

    id: Mapped[int] = mapped_column(primary_key=True)
    ancestry_id: Mapped[int] = mapped_column(ForeignKey("ancestries.id"))
    ancestry: Mapped["Ancestries"] = relationship(back_populates="description")
    en: Mapped[str] = mapped_column()
    de: Mapped[str] = mapped_column()
    fr: Mapped[str] = mapped_column()
    ja: Mapped[str] = mapped_column()
    zh: Mapped[str] = mapped_column()
    ru: Mapped[str] = mapped_column()
    ko: Mapped[str] = mapped_column()
    es: Mapped[str] = mapped_column()


class Ancestries_Name(Base):
    __tablename__ = "ancestries_name"

    id: Mapped[int] = mapped_column(primary_key=True)
    ancestry_id: Mapped[int] = mapped_column(ForeignKey("ancestries.id"))
    ancestry: Mapped["Ancestries"] = relationship(back_populates="name")
    en: Mapped[str] = mapped_column()
    de: Mapped[str] = mapped_column()
    fr: Mapped[str] = mapped_column()
    ja: Mapped[str] = mapped_column()
    zh: Mapped[str] = mapped_column()
    ru: Mapped[str] = mapped_column()
    ko: Mapped[str] = mapped_column()
    es: Mapped[str] = mapped_column()


class Ancestries(Base):
    __tablename__ = "ancestries"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[int] = mapped_column()
    bloodlineID: Mapped[int] = mapped_column()
    charisma: Mapped[int] = mapped_column()
    description: Mapped[Ancestries_Description] = relationship(
        back_populates="ancestry"
    )
    iconID: Mapped[Optional[int]] = mapped_column()
    intelligence: Mapped[int] = mapped_column()
    memory: Mapped[int] = mapped_column()
    name: Mapped[Ancestries_Name] = relationship(back_populates="ancestry")
    perception: Mapped[int] = mapped_column()
    shortDescription: Mapped[str | None] = mapped_column()
    willpower: Mapped[int] = mapped_column()
