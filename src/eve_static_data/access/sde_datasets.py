"""Helpers for loading typed SDE datasets from an unpacked SDE directory.

Note the dataset from the `types.jsonl` file has been renamed to `EveTypesDataset` to avoid confusion.
"""

from pathlib import Path

from eve_static_data.helpers.sde_info import load_sde_info
from eve_static_data.models.pydantic import datasets as PD
from eve_static_data.models.pydantic import records as PM


class SdeDatasetLoader:
    def __init__(self, sde_path: Path) -> None:
        """Helper class for loading typed SDE datasets from an unpacked SDE directory."""
        self.sde_path = sde_path

    def agent_types(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.AgentTypesDataset:
        """Load the agent types dataset."""
        return agent_types(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def agents_in_space(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.AgentsInSpaceDataset:
        """Load the agents in space dataset."""
        return agents_in_space(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def ancestries(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.AncestriesDataset:
        """Load the ancestries dataset."""
        return ancestries(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def bloodlines(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.BloodlinesDataset:
        """Load the bloodlines dataset."""
        return bloodlines(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def blueprints(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.BlueprintsDataset:
        """Load the blueprints dataset."""
        return blueprints(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def categories(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CategoriesDataset:
        """Load the categories dataset."""
        return categories(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def certificates(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CertificatesDataset:
        """Load the certificates dataset."""
        return certificates(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def character_attributes(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CharacterAttributesDataset:
        """Load the character attributes dataset."""
        return character_attributes(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def clone_grades(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CloneGradesDataset:
        """Load the clone grades dataset."""
        return clone_grades(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def compressible_types(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CompressibleTypesDataset:
        """Load the compressible types dataset."""
        return compressible_types(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def contraband_types(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.ContrabandTypesDataset:
        """Load the contraband types dataset."""
        return contraband_types(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def control_tower_resources(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.ControlTowerResourcesDataset:
        """Load the control tower resources dataset."""
        return control_tower_resources(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def corporation_activities(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.CorporationActivitiesDataset:
        """Load the corporation activities dataset."""
        return corporation_activities(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def debuff_collections(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DebuffCollectionsDataset:
        """Load the debuff collections dataset."""
        return debuff_collections(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def dogma_attribute_categories(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DogmaAttributeCategoriesDataset:
        """Load the dogma attribute categories dataset."""
        return dogma_attribute_categories(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def dogma_attributes(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DogmaAttributesDataset:
        """Load the dogma attributes dataset."""
        return dogma_attributes(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def dogma_effects(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DogmaEffectsDataset:
        """Load the dogma effects dataset."""
        return dogma_effects(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def dogma_units(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DogmaUnitsDataset:
        """Load the dogma units dataset."""
        return dogma_units(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def dynamic_item_attributes(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.DynamicItemAttributesDataset:
        """Load the dynamic item attributes dataset."""
        return dynamic_item_attributes(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def eve_types(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.EveTypesDataset:
        """Load the EVE types dataset."""
        return eve_types(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def factions(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.FactionsDataset:
        """Load the factions dataset."""
        return factions(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def freelance_job_schemas(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.FreelanceJobSchemasDataset:
        """Load the freelance job schemas dataset."""
        return freelance_job_schemas(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def graphics(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.GraphicsDataset:
        """Load the graphics dataset."""
        return graphics(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def groups(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.GroupsDataset:
        """Load the groups dataset."""
        return groups(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def icons(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.IconsDataset:
        """Load the icons dataset."""
        return icons(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def landmarks(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.LandmarksDataset:
        """Load the landmarks dataset."""
        return landmarks(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_asteroid_belts(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapAsteroidBeltsDataset:
        """Load the map asteroid belts dataset."""
        return map_asteroid_belts(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_constellations(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapConstellationsDataset:
        """Load the map constellations dataset."""
        return map_constellations(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_moons(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapMoonsDataset:
        """Load the map moons dataset."""
        return map_moons(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_planets(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapPlanetsDataset:
        """Load the map planets dataset."""
        return map_planets(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_regions(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapRegionsDataset:
        """Load the map regions dataset."""
        return map_regions(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_solar_systems(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapSolarSystemsDataset:
        """Load the map solar systems dataset."""
        return map_solar_systems(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_stargates(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapStargatesDataset:
        """Load the map stargates dataset."""
        return map_stargates(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def map_stars(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MapStarsDataset:
        """Load the map stars dataset."""
        return map_stars(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def market_groups(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MarketGroupsDataset:
        """Load the market groups dataset."""
        return market_groups(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def masteries(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MasteriesDataset:
        """Load the masteries dataset."""
        return masteries(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def mercenary_tactical_operations(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MercenaryTacticalOperationsDataset:
        """Load the mercenary tactical operations dataset."""
        return mercenary_tactical_operations(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def meta_groups(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.MetaGroupsDataset:
        """Load the meta groups dataset."""
        return meta_groups(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def npc_characters(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.NpcCharactersDataset:
        """Load the NPC characters dataset."""
        return npc_characters(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def npc_corporation_divisions(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.NpcCorporationDivisionsDataset:
        """Load the NPC corporation divisions dataset."""
        return npc_corporation_divisions(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def npc_corporations(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.NpcCorporationsDataset:
        """Load the NPC corporations dataset."""
        return npc_corporations(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def npc_stations(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.NpcStationsDataset:
        """Load the NPC stations dataset."""
        return npc_stations(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def planet_resources(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.PlanetResourcesDataset:
        """Load the planet resources dataset."""
        return planet_resources(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def planet_schematics(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.PlanetSchematicsDataset:
        """Load the planet schematics dataset."""
        return planet_schematics(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def races(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.RacesDataset:
        """Load the races dataset."""
        return races(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def sde_info(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.SdeInfoDataset:
        """Load the SDE info dataset."""
        return sde_info(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def skin_licenses(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.SkinLicensesDataset:
        """Load the skin licenses dataset."""
        return skin_licenses(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def skin_materials(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.SkinMaterialsDataset:
        """Load the skin materials dataset."""
        return skin_materials(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def skins(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.SkinsDataset:
        """Load the skins dataset."""
        return skins(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def sovereignty_upgrades(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.SovereigntyUpgradesDataset:
        """Load the sovereignty upgrades dataset."""
        return sovereignty_upgrades(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def station_operations(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.StationOperationsDataset:
        """Load the station operations dataset."""
        return station_operations(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def station_services(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.StationServicesDataset:
        """Load the station services dataset."""
        return station_services(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def translation_languages(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.TranslationLanguagesDataset:
        """Load the translation languages dataset."""
        return translation_languages(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def type_bonus(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.TypeBonusDataset:
        """Load the type bonus dataset."""
        return type_bonus(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def type_dogma(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.TypeDogmaDataset:
        """Load the type dogma dataset."""
        return type_dogma(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )

    def type_materials(
        self, only_published: bool = True, skip_validation_failures: bool = False
    ) -> PD.TypeMaterialsDataset:
        """Load the type materials dataset."""
        return type_materials(
            self.sde_path,
            only_published=only_published,
            skip_validation_failures=skip_validation_failures,
        )


def agent_types(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.AgentTypesDataset:
    """Load the agent types dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.AgentTypes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.AgentTypesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def agents_in_space(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.AgentsInSpaceDataset:
    """Load the agents in space dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.AgentsInSpace,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.AgentsInSpaceDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def ancestries(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.AncestriesDataset:
    """Load the ancestries dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Ancestries,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.AncestriesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def bloodlines(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.BloodlinesDataset:
    """Load the bloodlines dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Bloodlines,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.BloodlinesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def blueprints(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.BlueprintsDataset:
    """Load the blueprints dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Blueprints,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.BlueprintsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def categories(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CategoriesDataset:
    """Load the categories dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Categories,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CategoriesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def certificates(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CertificatesDataset:
    """Load the certificates dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Certificates,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CertificatesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def character_attributes(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CharacterAttributesDataset:
    """Load the character attributes dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.CharacterAttributes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CharacterAttributesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def clone_grades(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CloneGradesDataset:
    """Load the clone grades dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.CloneGrades,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CloneGradesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def compressible_types(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CompressibleTypesDataset:
    """Load the compressible types dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.CompressibleTypes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CompressibleTypesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def contraband_types(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.ContrabandTypesDataset:
    """Load the contraband types dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.ContrabandTypes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.ContrabandTypesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def control_tower_resources(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.ControlTowerResourcesDataset:
    """Load the control tower resources dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.ControlTowerResources,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.ControlTowerResourcesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def corporation_activities(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.CorporationActivitiesDataset:
    """Load the corporation activities dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.CorporationActivities,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.CorporationActivitiesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def debuff_collections(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DebuffCollectionsDataset:
    """Load the debuff collections dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DebuffCollections,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DebuffCollectionsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def dogma_attribute_categories(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DogmaAttributeCategoriesDataset:
    """Load the dogma attribute categories dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DogmaAttributeCategories,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DogmaAttributeCategoriesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def dogma_attributes(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DogmaAttributesDataset:
    """Load the dogma attributes dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DogmaAttributes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DogmaAttributesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def dogma_effects(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DogmaEffectsDataset:
    """Load the dogma effects dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DogmaEffects,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DogmaEffectsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def dogma_units(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DogmaUnitsDataset:
    """Load the dogma units dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DogmaUnits,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DogmaUnitsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def dynamic_item_attributes(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.DynamicItemAttributesDataset:
    """Load the dynamic item attributes dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.DynamicItemAttributes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.DynamicItemAttributesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def eve_types(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.EveTypesDataset:
    """Load the EVE types dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.EveTypes,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.EveTypesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def factions(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.FactionsDataset:
    """Load the factions dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Factions,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.FactionsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def freelance_job_schemas(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.FreelanceJobSchemasDataset:
    """Load the freelance job schemas dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.FreelanceJobSchemas,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    loaded_records = [record for _, record in records if record is not None]
    if len(loaded_records) != 1:
        raise ValueError(
            "Expected exactly one record for the freelance job schemas dataset, "
            f"found {len(loaded_records)}."
        )
    dataset = PD.FreelanceJobSchemasDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        record=loaded_records[0],
    )
    return dataset


def graphics(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.GraphicsDataset:
    """Load the graphics dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Graphics,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.GraphicsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def groups(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.GroupsDataset:
    """Load the groups dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Groups,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.GroupsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def icons(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.IconsDataset:
    """Load the icons dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Icons,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.IconsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def landmarks(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.LandmarksDataset:
    """Load the landmarks dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Landmarks,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.LandmarksDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_asteroid_belts(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapAsteroidBeltsDataset:
    """Load the map asteroid belts dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapAsteroidBelts,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapAsteroidBeltsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_constellations(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapConstellationsDataset:
    """Load the map constellations dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapConstellations,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapConstellationsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_moons(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapMoonsDataset:
    """Load the map moons dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapMoons,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapMoonsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_planets(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapPlanetsDataset:
    """Load the map planets dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapPlanets,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapPlanetsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_regions(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapRegionsDataset:
    """Load the map regions dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapRegions,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapRegionsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_solar_systems(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapSolarSystemsDataset:
    """Load the map solar systems dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapSolarSystems,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapSolarSystemsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_stargates(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapStargatesDataset:
    """Load the map stargates dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapStargates,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapStargatesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def map_stars(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MapStarsDataset:
    """Load the map stars dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MapStars,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MapStarsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def market_groups(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MarketGroupsDataset:
    """Load the market groups dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MarketGroups,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MarketGroupsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def masteries(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MasteriesDataset:
    """Load the masteries dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Masteries,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MasteriesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def mercenary_tactical_operations(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MercenaryTacticalOperationsDataset:
    """Load the mercenary tactical operations dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MercenaryTacticalOperations,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MercenaryTacticalOperationsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def meta_groups(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.MetaGroupsDataset:
    """Load the meta groups dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.MetaGroups,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.MetaGroupsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def npc_characters(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.NpcCharactersDataset:
    """Load the NPC characters dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.NpcCharacters,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.NpcCharactersDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def npc_corporation_divisions(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.NpcCorporationDivisionsDataset:
    """Load the NPC corporation divisions dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.NpcCorporationDivisions,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.NpcCorporationDivisionsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def npc_corporations(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.NpcCorporationsDataset:
    """Load the NPC corporations dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.NpcCorporations,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.NpcCorporationsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def npc_stations(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.NpcStationsDataset:
    """Load the NPC stations dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.NpcStations,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.NpcStationsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def planet_resources(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.PlanetResourcesDataset:
    """Load the planet resources dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.PlanetResources,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.PlanetResourcesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def planet_schematics(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.PlanetSchematicsDataset:
    """Load the planet schematics dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.PlanetSchematics,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.PlanetSchematicsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def races(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.RacesDataset:
    """Load the races dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Races,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.RacesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def sde_info(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.SdeInfoDataset:
    """Load the SDE info dataset."""
    sde_info_dict = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.SdeInfo,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    loaded_records = [record for _, record in records if record is not None]
    if len(loaded_records) != 1:
        raise ValueError(
            f"Expected exactly one record for the SDE info dataset, found {len(loaded_records)}."
        )
    dataset = PD.SdeInfoDataset(
        build_number=sde_info_dict.get("buildNumber"),
        release_date=sde_info_dict.get("releaseDate"),
        record=loaded_records[0],
    )
    return dataset


def skin_licenses(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.SkinLicensesDataset:
    """Load the skin licenses dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.SkinLicenses,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.SkinLicensesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def skin_materials(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.SkinMaterialsDataset:
    """Load the skin materials dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.SkinMaterials,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.SkinMaterialsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def skins(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.SkinsDataset:
    """Load the skins dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.Skins,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.SkinsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def sovereignty_upgrades(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.SovereigntyUpgradesDataset:
    """Load the sovereignty upgrades dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.SovereigntyUpgrades,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.SovereigntyUpgradesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def station_operations(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.StationOperationsDataset:
    """Load the station operations dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.StationOperations,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.StationOperationsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def station_services(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.StationServicesDataset:
    """Load the station services dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.StationServices,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.StationServicesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def translation_languages(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.TranslationLanguagesDataset:
    """Load the translation languages dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.TranslationLanguages,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.TranslationLanguagesDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def type_bonus(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.TypeBonusDataset:
    """Load the type bonus dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.TypeBonus,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.TypeBonusDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def type_dogma(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.TypeDogmaDataset:
    """Load the type dogma dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.TypeDogma,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.TypeDogmaDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset


def type_materials(
    sde_path: Path, only_published: bool = True, skip_validation_failures: bool = False
) -> PD.TypeMaterialsDataset:
    """Load the type materials dataset."""
    sde_info = load_sde_info(sde_path)
    records = PM.read_records(
        sde_path,
        PM.TypeMaterials,
        only_published=only_published,
        skip_validation_failures=skip_validation_failures,
    )
    records_dict = {record.key: record for _, record in records if record is not None}
    dataset = PD.TypeMaterialsDataset(
        build_number=sde_info.get("buildNumber"),
        release_date=sde_info.get("releaseDate"),
        records=records_dict,
    )
    return dataset
