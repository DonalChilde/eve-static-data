"""SQLAlchemy models for the EVE Static Data application.

CamelCase is used for database column names to match the naming convention used in the SDE.
This allows for easier mapping between the SDE data and the database models.

The `_key` field in the SDE jsonl data is renamed to `key` due to issues with pydantic.
"""

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
    iconID: Mapped[int | None] = mapped_column()
    intelligence: Mapped[int] = mapped_column()
    memory: Mapped[int] = mapped_column()
    name: Mapped[Ancestries_Name] = relationship(back_populates="ancestry")
    perception: Mapped[int] = mapped_column()
    shortDescription: Mapped[str | None] = mapped_column()
    willpower: Mapped[int] = mapped_column()


class Bloodlines_Name(Base):
    __tablename__ = "bloodlines_name"

    id: Mapped[int] = mapped_column(primary_key=True)
    bloodline_id: Mapped[int] = mapped_column(ForeignKey("bloodlines.id"))
    bloodline: Mapped["Bloodlines"] = relationship(back_populates="name")
    en: Mapped[str] = mapped_column()
    de: Mapped[str] = mapped_column()
    fr: Mapped[str] = mapped_column()
    ja: Mapped[str] = mapped_column()
    zh: Mapped[str] = mapped_column()
    ru: Mapped[str] = mapped_column()
    ko: Mapped[str] = mapped_column()
    es: Mapped[str] = mapped_column()


class Bloodlines_Description(Base):
    __tablename__ = "bloodlines_description"

    id: Mapped[int] = mapped_column(primary_key=True)
    bloodline_id: Mapped[int] = mapped_column(ForeignKey("bloodlines.id"))
    bloodline: Mapped["Bloodlines"] = relationship(back_populates="description")
    en: Mapped[str] = mapped_column()
    de: Mapped[str] = mapped_column()
    fr: Mapped[str] = mapped_column()
    ja: Mapped[str] = mapped_column()
    zh: Mapped[str] = mapped_column()
    ru: Mapped[str] = mapped_column()
    ko: Mapped[str] = mapped_column()
    es: Mapped[str] = mapped_column()


class Bloodlines(Base):
    __tablename__ = "bloodlines"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[int] = mapped_column()
    charisma: Mapped[int] = mapped_column()
    corporationID: Mapped[int | None] = mapped_column()
    description: Mapped[Bloodlines_Description] = relationship(
        back_populates="bloodline"
    )
    iconID: Mapped[int | None] = mapped_column()
    intelligence: Mapped[int] = mapped_column()
    memory: Mapped[int] = mapped_column()
    name: Mapped[Bloodlines_Name] = relationship(back_populates="bloodline")
    perception: Mapped[int] = mapped_column()
    raceID: Mapped[int] = mapped_column()
    willpower: Mapped[int] = mapped_column()


class Blueprints_Copying_Materials(Base):
    __tablename__ = "blueprints_copying_materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    copying_id: Mapped[int] = mapped_column(ForeignKey("blueprints_copying.id"))
    copying: Mapped["Blueprints_Copying"] = relationship(back_populates="materials")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Copying_Skills(Base):
    __tablename__ = "blueprints_copying_skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    copying_id: Mapped[int] = mapped_column(ForeignKey("blueprints_copying.id"))
    copying: Mapped["Blueprints_Copying"] = relationship(back_populates="skills")
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Copying_Products(Base):
    __tablename__ = "blueprints_copying_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    copying_id: Mapped[int] = mapped_column(ForeignKey("blueprints_copying.id"))
    copying: Mapped["Blueprints_Copying"] = relationship(back_populates="products")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Copying(Base):
    __tablename__ = "blueprints_copying"

    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="copying")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Copying_Materials]] = relationship(
        back_populates="copying"
    )
    skills: Mapped[list[Blueprints_Copying_Skills]] = relationship(
        back_populates="copying"
    )
    products: Mapped[list[Blueprints_Copying_Products]] = relationship(
        back_populates="copying"
    )


class Blueprints_Invention_Materials(Base):
    __tablename__ = "blueprints_invention_materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    invention_id: Mapped[int] = mapped_column(ForeignKey("blueprints_invention.id"))
    invention: Mapped["Blueprints_Invention"] = relationship(back_populates="materials")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Invention_Skills(Base):
    __tablename__ = "blueprints_invention_skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    invention_id: Mapped[int] = mapped_column(ForeignKey("blueprints_invention.id"))
    invention: Mapped["Blueprints_Invention"] = relationship(back_populates="skills")
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Invention_Products(Base):
    __tablename__ = "blueprints_invention_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    invention_id: Mapped[int] = mapped_column(ForeignKey("blueprints_invention.id"))
    invention: Mapped["Blueprints_Invention"] = relationship(back_populates="products")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Invention(Base):
    __tablename__ = "blueprints_invention"

    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="invention")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Invention_Materials]] = relationship(
        back_populates="invention"
    )
    skills: Mapped[list[Blueprints_Invention_Skills]] = relationship(
        back_populates="invention"
    )
    products: Mapped[list[Blueprints_Invention_Products]] = relationship(
        back_populates="invention"
    )


class Blueprints_Manufacturing_Materials(Base):
    __tablename__ = "blueprints_manufacturing_materials"
    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturing_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_manufacturing.id")
    )
    manufacturing: Mapped["Blueprints_Manufacturing"] = relationship(
        back_populates="materials"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Manufacturing_Skills(Base):
    __tablename__ = "blueprints_manufacturing_skills"
    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturing_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_manufacturing.id")
    )
    manufacturing: Mapped["Blueprints_Manufacturing"] = relationship(
        back_populates="skills"
    )
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Manufacturing_Products(Base):
    __tablename__ = "blueprints_manufacturing_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    manufacturing_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_manufacturing.id")
    )
    manufacturing: Mapped["Blueprints_Manufacturing"] = relationship(
        back_populates="products"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Manufacturing(Base):
    __tablename__ = "blueprints_manufacturing"
    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="manufacturing")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Manufacturing_Materials]] = relationship(
        back_populates="manufacturing"
    )
    skills: Mapped[list[Blueprints_Manufacturing_Skills]] = relationship(
        back_populates="manufacturing"
    )
    products: Mapped[list[Blueprints_Manufacturing_Products]] = relationship(
        back_populates="manufacturing"
    )


class Blueprints_Reaction_Materials(Base):
    __tablename__ = "blueprints_reaction_materials"
    id: Mapped[int] = mapped_column(primary_key=True)
    reaction_id: Mapped[int] = mapped_column(ForeignKey("blueprints_reaction.id"))
    reaction: Mapped["Blueprints_Reaction"] = relationship(back_populates="materials")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Reaction_Skills(Base):
    __tablename__ = "blueprints_reaction_skills"
    id: Mapped[int] = mapped_column(primary_key=True)
    reaction_id: Mapped[int] = mapped_column(ForeignKey("blueprints_reaction.id"))
    reaction: Mapped["Blueprints_Reaction"] = relationship(back_populates="skills")
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Reaction_Products(Base):
    __tablename__ = "blueprints_reaction_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    reaction_id: Mapped[int] = mapped_column(ForeignKey("blueprints_reaction.id"))
    reaction: Mapped["Blueprints_Reaction"] = relationship(back_populates="products")
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Reaction(Base):
    __tablename__ = "blueprints_reaction"
    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="reaction")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Reaction_Materials]] = relationship(
        back_populates="reaction"
    )
    skills: Mapped[list[Blueprints_Reaction_Skills]] = relationship(
        back_populates="reaction"
    )
    products: Mapped[list[Blueprints_Reaction_Products]] = relationship(
        back_populates="reaction"
    )


class Blueprints_Research_Material_Materials(Base):
    __tablename__ = "blueprints_research_material_materials"
    id: Mapped[int] = mapped_column(primary_key=True)
    research_material_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_material.id")
    )
    blueprint: Mapped["Blueprints_Research_Material"] = relationship(
        back_populates="materials"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Research_Material_Skills(Base):
    __tablename__ = "blueprints_research_material_skills"
    id: Mapped[int] = mapped_column(primary_key=True)
    research_material_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_material.id")
    )
    blueprint: Mapped["Blueprints_Research_Material"] = relationship(
        back_populates="skills"
    )
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Research_Material_Products(Base):
    __tablename__ = "blueprints_research_material_products"
    id: Mapped[int] = mapped_column(primary_key=True)
    research_material_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_material.id")
    )
    blueprint: Mapped["Blueprints_Research_Material"] = relationship(
        back_populates="products"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Research_Material(Base):
    __tablename__ = "blueprints_research_material"

    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="research_material")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Research_Material_Materials]] = relationship(
        back_populates="blueprint"
    )
    skills: Mapped[list[Blueprints_Research_Material_Skills]] = relationship(
        back_populates="blueprint"
    )
    products: Mapped[list[Blueprints_Research_Material_Products]] = relationship(
        back_populates="blueprint"
    )


class Blueprints_Research_Time_Materials(Base):
    __tablename__ = "blueprints_research_time_materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    research_time_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_time.id")
    )
    blueprint: Mapped["Blueprints_Research_Time"] = relationship(
        back_populates="materials"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()


class Blueprints_Research_Time_Skills(Base):
    __tablename__ = "blueprints_research_time_skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    research_time_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_time.id")
    )
    blueprint: Mapped["Blueprints_Research_Time"] = relationship(
        back_populates="skills"
    )
    typeID: Mapped[int] = mapped_column()
    level: Mapped[int] = mapped_column()


class Blueprints_Research_Time_Products(Base):
    __tablename__ = "blueprints_research_time_products"

    id: Mapped[int] = mapped_column(primary_key=True)
    research_time_id: Mapped[int] = mapped_column(
        ForeignKey("blueprints_research_time.id")
    )
    blueprint: Mapped["Blueprints_Research_Time"] = relationship(
        back_populates="products"
    )
    typeID: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    probability: Mapped[float | None] = mapped_column()


class Blueprints_Research_Time(Base):
    __tablename__ = "blueprints_research_time"

    id: Mapped[int] = mapped_column(primary_key=True)
    blueprint_id: Mapped[int] = mapped_column(ForeignKey("blueprints.id"))
    blueprint: Mapped["Blueprints"] = relationship(back_populates="research_time")
    time: Mapped[int] = mapped_column()
    materials: Mapped[list[Blueprints_Research_Time_Materials]] = relationship(
        back_populates="blueprint"
    )
    skills: Mapped[list[Blueprints_Research_Time_Skills]] = relationship(
        back_populates="blueprint"
    )
    products: Mapped[list[Blueprints_Research_Time_Products]] = relationship(
        back_populates="blueprint"
    )


class Blueprints(Base):
    __tablename__ = "blueprints"

    id: Mapped[int] = mapped_column(primary_key=True)
    key: Mapped[int] = mapped_column()
    maxProductionLimit: Mapped[int | None] = mapped_column()
    blueprintTypeID: Mapped[int] = mapped_column()
    copying: Mapped[Blueprints_Copying | None] = relationship(
        back_populates="blueprint", uselist=False
    )
    invention: Mapped[Blueprints_Invention | None] = relationship(
        back_populates="blueprint", uselist=False
    )
    manufacturing: Mapped[Blueprints_Manufacturing | None] = relationship(
        back_populates="blueprint", uselist=False
    )
    reaction: Mapped[Blueprints_Reaction | None] = relationship(
        back_populates="blueprint", uselist=False
    )
    research_material: Mapped[Blueprints_Research_Material | None] = relationship(
        back_populates="blueprint", uselist=False
    )
    research_time: Mapped[Blueprints_Research_Time | None] = relationship(
        back_populates="blueprint", uselist=False
    )
