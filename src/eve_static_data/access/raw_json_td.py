"""Raw JSON file access implementation for SDE build 3123381."""
# ruff: noqa: D102

import json
import logging
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

from pydantic import TypeAdapter, ValidationError

from eve_static_data.access.raw_json import RawJsonFileAccess
from eve_static_data.models import raw_td as RTD

from .raw_json_td_protocol import RawJsonTDProtocol
from .sde_file_names import SdeFileNames

logger = logging.getLogger(__name__)


class RawJsonTDFileAccess(RawJsonTDProtocol):
    def __init__(self, sde_dir: Path) -> None:
        self.sde_dir = sde_dir
        self.access = RawJsonFileAccess(sde_dir)

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentsInSpace]:
        for item in self.access.agents_in_space():
            yield cast(RTD.AgentsInSpace, item)

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentTypes]:
        for item in self.access.agent_types():
            yield cast(RTD.AgentTypes, item)

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Ancestries]:
        for item in self.access.ancestries():
            yield cast(RTD.Ancestries, item)

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Bloodlines]:
        for item in self.access.bloodlines():
            yield cast(RTD.Bloodlines, item)

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Blueprints]:
        for item in self.access.blueprints():
            yield cast(RTD.Blueprints, item)

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Categories]:
        for item in self.access.categories():
            yield cast(RTD.Categories, item)

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Certificates]:
        for item in self.access.certificates():
            yield cast(RTD.Certificates, item)

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CharacterAttributes]:
        for item in self.access.character_attributes():
            yield cast(RTD.CharacterAttributes, item)

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CompressibleTypes]:
        for item in self.access.compressible_types():
            yield cast(RTD.CompressibleTypes, item)

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ContrabandTypes]:
        for item in self.access.contraband_types():
            yield cast(RTD.ContrabandTypes, item)

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ControlTowerResources]:
        for item in self.access.control_tower_resources():
            yield cast(RTD.ControlTowerResources, item)

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CorporationActivities]:
        for item in self.access.corporation_activities():
            yield cast(RTD.CorporationActivities, item)

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DebuffCollections]:
        for item in self.access.debuff_collections():
            yield cast(RTD.DebuffCollections, item)

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        for item in self.access.dogma_attribute_categories():
            yield cast(RTD.DogmaAttributeCategories, item)

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributes]:
        for item in self.access.dogma_attributes():
            yield cast(RTD.DogmaAttributes, item)

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaEffects]:
        for item in self.access.dogma_effects():
            yield cast(RTD.DogmaEffects, item)

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaUnits]:
        for item in self.access.dogma_units():
            yield cast(RTD.DogmaUnits, item)

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DynamicItemAttributes]:
        for item in self.access.dynamic_item_attributes():
            yield cast(RTD.DynamicItemAttributes, item)

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Factions]:
        for item in self.access.factions():
            yield cast(RTD.Factions, item)

    def freelance_job_schemas(
        self, **kwargs: dict[str, Any]
    ) -> RTD.FreelanceJobSchemas:
        return self.access.freelance_job_schemas()

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Graphics]:
        for item in self.access.graphics():
            yield cast(RTD.Graphics, item)

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Groups]:
        for item in self.access.groups():
            yield cast(RTD.Groups, item)

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Icons]:
        for item in self.access.icons():
            yield cast(RTD.Icons, item)

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Landmarks]:
        for item in self.access.landmarks():
            yield cast(RTD.Landmarks, item)

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapAsteroidBelts]:
        for item in self.access.map_asteroid_belts():
            yield cast(RTD.MapAsteroidBelts, item)

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapConstellations]:
        for item in self.access.map_constellations():
            yield cast(RTD.MapConstellations, item)

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapMoons]:
        for item in self.access.map_moons():
            yield cast(RTD.MapMoons, item)

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapPlanets]:
        for item in self.access.map_planets():
            yield cast(RTD.MapPlanets, item)

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapRegions]:
        for item in self.access.map_regions():
            yield cast(RTD.MapRegions, item)

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapSolarSystems]:
        for item in self.access.map_solar_systems():
            yield cast(RTD.MapSolarSystems, item)

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStargates]:
        for item in self.access.map_stargates():
            yield cast(RTD.MapStargates, item)

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStars]:
        for item in self.access.map_stars():
            yield cast(RTD.MapStars, item)

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MarketGroups]:
        for item in self.access.market_groups():
            yield cast(RTD.MarketGroups, item)

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Masteries]:
        for item in self.access.masteries():
            yield cast(RTD.Masteries, item)

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MetaGroups]:
        for item in self.access.meta_groups():
            yield cast(RTD.MetaGroups, item)

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcCharacters]:
        for item in self.access.npc_characters():
            yield cast(RTD.NpcCharacters, item)

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        for item in self.access.npc_corporation_divisions():
            yield cast(RTD.NpcCorporationDivisions, item)

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporations]:
        for item in self.access.npc_corporations():
            yield cast(RTD.NpcCorporations, item)

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcStations]:
        for item in self.access.npc_stations():
            yield cast(RTD.NpcStations, item)

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetResources]:
        for item in self.access.planet_resources():
            yield cast(RTD.PlanetResources, item)

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetSchematics]:
        for item in self.access.planet_schematics():
            yield cast(RTD.PlanetSchematics, item)

    def races(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Races]:
        for item in self.access.races():
            yield cast(RTD.Races, item)

    def sde_info(self, **kwargs: dict[str, Any]) -> RTD.SdeInfo:
        return cast(RTD.SdeInfo, self.access.sde_info())

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinLicenses]:
        for item in self.access.skin_licenses():
            yield cast(RTD.SkinLicenses, item)

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinMaterials]:
        for item in self.access.skin_materials():
            yield cast(RTD.SkinMaterials, item)

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Skins]:
        for item in self.access.skins():
            yield cast(RTD.Skins, item)

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        for item in self.access.sovereignty_upgrades():
            yield cast(RTD.SovereigntyUpgrades, item)

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationOperations]:
        for item in self.access.station_operations():
            yield cast(RTD.StationOperations, item)

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationServices]:
        for item in self.access.station_services():
            yield cast(RTD.StationServices, item)

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.TranslationLanguages]:
        for item in self.access.translation_languages():
            yield cast(RTD.TranslationLanguages, item)

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeBonus]:
        for item in self.access.type_bonus():
            yield cast(RTD.TypeBonus, item)

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeDogma]:
        for item in self.access.type_dogma():
            yield cast(RTD.TypeDogma, item)

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeMaterials]:
        for item in self.access.type_materials():
            yield cast(RTD.TypeMaterials, item)

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.EveTypes]:
        for item in self.access.eve_types():
            yield cast(RTD.EveTypes, item)


@dataclass
class ValidationResult:
    source: str
    data: Any
    error: Exception

    def __str__(self) -> str:
        return f"Validation error for {self.source} item:\n{json.dumps(self.data, indent=2)}\nError details: {self.error}"


class RawJsonFileAccessValidator(RawJsonTDProtocol):
    def __init__(self, dir_path: Path) -> None:
        """This class can be used to validate the raw json file data against the TypedDict models.

        It will log any validation errors, and store them in the `validation_errors` attribute for later inspection.

        If validation fails, values will still be returned. This allows for the entire dataset to be validated without
        stopping at the first error. Because of this behavior, this class should not be used for production use,
        but rather as a development tool to identify and fix issues with the raw data.
        """
        self.dir_path = dir_path
        self.access = RawJsonTDFileAccess(dir_path)
        self.validation_errors: list[ValidationResult] = []

    def agents_in_space(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentsInSpace]:
        adapter = TypeAdapter(RTD.AgentsInSpace)
        for item in self.access.agents_in_space():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="agents_in_space", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def agent_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.AgentTypes]:
        adapter = TypeAdapter(RTD.AgentTypes)
        for item in self.access.agent_types():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="agent_types", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def ancestries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Ancestries]:

        adapter = TypeAdapter(RTD.Ancestries)
        for item in self.access.ancestries():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="ancestries", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def bloodlines(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Bloodlines]:
        adapter = TypeAdapter(RTD.Bloodlines)
        for item in self.access.bloodlines():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="bloodlines", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def blueprints(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Blueprints]:

        adapter = TypeAdapter(RTD.Blueprints)
        for item in self.access.blueprints():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="blueprints", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def categories(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Categories]:
        adapter = TypeAdapter(RTD.Categories)
        for item in self.access.categories():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="categories", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def certificates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Certificates]:
        adapter = TypeAdapter(RTD.Certificates)
        for item in self.access.certificates():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="certificates", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def character_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CharacterAttributes]:
        adapter = TypeAdapter(RTD.CharacterAttributes)
        for item in self.access.character_attributes():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="character_attributes", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def compressible_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CompressibleTypes]:
        adapter = TypeAdapter(RTD.CompressibleTypes)
        for item in self.access.compressible_types():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="compressible_types", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def contraband_types(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ContrabandTypes]:
        adapter = TypeAdapter(RTD.ContrabandTypes)
        for item in self.access.contraband_types():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="contraband_types", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def control_tower_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.ControlTowerResources]:
        adapter = TypeAdapter(RTD.ControlTowerResources)
        for item in self.access.control_tower_resources():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="control_tower_resources", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def corporation_activities(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.CorporationActivities]:
        adapter = TypeAdapter(RTD.CorporationActivities)
        for item in self.access.corporation_activities():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="corporation_activities", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def debuff_collections(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DebuffCollections]:
        adapter = TypeAdapter(RTD.DebuffCollections)
        for item in self.access.debuff_collections():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="debuff_collections", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def dogma_attribute_categories(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributeCategories]:
        adapter = TypeAdapter(RTD.DogmaAttributeCategories)
        for item in self.access.dogma_attribute_categories():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="dogma_attribute_categories", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def dogma_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DogmaAttributes]:
        adapter = TypeAdapter(RTD.DogmaAttributes)
        for item in self.access.dogma_attributes():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="dogma_attributes", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def dogma_effects(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaEffects]:
        adapter = TypeAdapter(RTD.DogmaEffects)
        for item in self.access.dogma_effects():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="dogma_effects", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def dogma_units(self, **kwargs: dict[str, Any]) -> Iterable[RTD.DogmaUnits]:
        adapter = TypeAdapter(RTD.DogmaUnits)
        for item in self.access.dogma_units():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="dogma_units", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def dynamic_item_attributes(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.DynamicItemAttributes]:
        adapter = TypeAdapter(RTD.DynamicItemAttributes)
        for item in self.access.dynamic_item_attributes():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="dynamic_item_attributes", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def factions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Factions]:
        adapter = TypeAdapter(RTD.Factions)
        for item in self.access.factions():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="factions", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def freelance_job_schemas(
        self, **kwargs: dict[str, Any]
    ) -> RTD.FreelanceJobSchemas:
        item = self.access.freelance_job_schemas()
        logger.error(
            "Free lance job schemas validation is not implemented yet. Returning raw data without validation."
        )
        raise NotImplementedError(
            "Freelance job schemas validation is not implemented yet."
        )
        return item

    def graphics(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Graphics]:
        adapter = TypeAdapter(RTD.Graphics)
        for item in self.access.graphics():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="graphics", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Groups]:
        adapter = TypeAdapter(RTD.Groups)
        for item in self.access.groups():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="groups", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def icons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Icons]:
        adapter = TypeAdapter(RTD.Icons)
        for item in self.access.icons():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="icons", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def landmarks(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Landmarks]:
        adapter = TypeAdapter(RTD.Landmarks)
        for item in self.access.landmarks():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="landmarks", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_asteroid_belts(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapAsteroidBelts]:
        adapter = TypeAdapter(RTD.MapAsteroidBelts)
        for item in self.access.map_asteroid_belts():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="map_asteroid_belts", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_constellations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapConstellations]:
        adapter = TypeAdapter(RTD.MapConstellations)
        for item in self.access.map_constellations():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="map_constellations", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_moons(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapMoons]:
        adapter = TypeAdapter(RTD.MapMoons)
        for item in self.access.map_moons():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="map_moons", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_planets(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapPlanets]:
        adapter = TypeAdapter(RTD.MapPlanets)
        for item in self.access.map_planets():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="map_planets", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_regions(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapRegions]:
        adapter = TypeAdapter(RTD.MapRegions)
        for item in self.access.map_regions():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="map_regions", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_solar_systems(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.MapSolarSystems]:
        adapter = TypeAdapter(RTD.MapSolarSystems)
        for item in self.access.map_solar_systems():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="map_solar_systems", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_stargates(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStargates]:
        adapter = TypeAdapter(RTD.MapStargates)
        for item in self.access.map_stargates():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="map_stargates", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def map_stars(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MapStars]:
        adapter = TypeAdapter(RTD.MapStars)
        for item in self.access.map_stars():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="map_stars", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def market_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MarketGroups]:
        adapter = TypeAdapter(RTD.MarketGroups)
        for item in self.access.market_groups():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="market_groups", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def masteries(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Masteries]:
        adapter = TypeAdapter(RTD.Masteries)
        for item in self.access.masteries():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="masteries", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def meta_groups(self, **kwargs: dict[str, Any]) -> Iterable[RTD.MetaGroups]:
        adapter = TypeAdapter(RTD.MetaGroups)
        for item in self.access.meta_groups():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="meta_groups", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def npc_characters(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcCharacters]:

        adapter = TypeAdapter(RTD.NpcCharacters)
        for item in self.access.npc_characters():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="npc_characters", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def npc_corporation_divisions(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporationDivisions]:
        adapter = TypeAdapter(RTD.NpcCorporationDivisions)
        for item in self.access.npc_corporation_divisions():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="npc_corporation_divisions", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def npc_corporations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.NpcCorporations]:
        adapter = TypeAdapter(RTD.NpcCorporations)
        for item in self.access.npc_corporations():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="npc_corporations", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def npc_stations(self, **kwargs: dict[str, Any]) -> Iterable[RTD.NpcStations]:
        adapter = TypeAdapter(RTD.NpcStations)
        for item in self.access.npc_stations():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="npc_stations", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def planet_resources(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetResources]:
        adapter = TypeAdapter(RTD.PlanetResources)
        for item in self.access.planet_resources():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="planet_resources", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def planet_schematics(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.PlanetSchematics]:
        adapter = TypeAdapter(RTD.PlanetSchematics)
        for item in self.access.planet_schematics():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="planet_schematics", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def races(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Races]:
        adapter = TypeAdapter(RTD.Races)
        for item in self.access.races():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="races", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def sde_info(self, **kwargs: dict[str, Any]) -> RTD.SdeInfo:
        sde_info = self.access.sde_info()
        adapter = TypeAdapter(RTD.SdeInfo)
        try:
            sde_info = adapter.validate_python(sde_info, extra="forbid")
        except ValidationError as e:
            result = ValidationResult(source="sde_info", data=sde_info, error=e)
            logger.error(str(result))
            self.validation_errors.append(result)
        return sde_info

    def skin_licenses(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinLicenses]:
        adapter = TypeAdapter(RTD.SkinLicenses)
        for item in self.access.skin_licenses():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="skin_licenses", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def skin_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.SkinMaterials]:
        adapter = TypeAdapter(RTD.SkinMaterials)
        for item in self.access.skin_materials():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="skin_materials", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item

    def skins(self, **kwargs: dict[str, Any]) -> Iterable[RTD.Skins]:
        adapter = TypeAdapter(RTD.Skins)
        for item in self.access.skins():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="skins", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def sovereignty_upgrades(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.SovereigntyUpgrades]:
        adapter = TypeAdapter(RTD.SovereigntyUpgrades)
        for item in self.access.sovereignty_upgrades():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="sovereignty_upgrades", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def station_operations(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationOperations]:
        adapter = TypeAdapter(RTD.StationOperations)
        for item in self.access.station_operations():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="station_operations", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def station_services(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.StationServices]:
        adapter = TypeAdapter(RTD.StationServices)
        for item in self.access.station_services():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="station_services", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def translation_languages(
        self, **kwargs: dict[str, Any]
    ) -> Iterable[RTD.TranslationLanguages]:
        adapter = TypeAdapter(RTD.TranslationLanguages)
        for item in self.access.translation_languages():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(
                    source="translation_languages", data=item, error=e
                )
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def type_bonus(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeBonus]:
        adapter = TypeAdapter(RTD.TypeBonus)
        for item in self.access.type_bonus():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="type_bonus", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def type_dogma(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeDogma]:
        adapter = TypeAdapter(RTD.TypeDogma)
        for item in self.access.type_dogma():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="type_dogma", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def type_materials(self, **kwargs: dict[str, Any]) -> Iterable[RTD.TypeMaterials]:
        adapter = TypeAdapter(RTD.TypeMaterials)
        for item in self.access.type_materials():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="type_materials", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def eve_types(self, **kwargs: dict[str, Any]) -> Iterable[RTD.EveTypes]:
        adapter = TypeAdapter(RTD.EveTypes)
        for item in self.access.eve_types():
            try:
                validated_item = adapter.validate_python(item, extra="forbid")
            except ValidationError as e:
                result = ValidationResult(source="eve_types", data=item, error=e)
                logger.error(str(result))
                self.validation_errors.append(result)
                continue
            yield validated_item
        return

    def validate(self, file_name: SdeFileNames) -> None:
        """Validate a specific SDE file."""
        match file_name:
            case SdeFileNames.AGENTS_IN_SPACE:
                _ = list(self.agents_in_space())
            case SdeFileNames.AGENT_TYPES:
                _ = list(self.agent_types())
            case SdeFileNames.ANCESTRIES:
                _ = list(self.ancestries())
            case SdeFileNames.BLOODLINES:
                _ = list(self.bloodlines())
            case SdeFileNames.BLUEPRINTS:
                _ = list(self.blueprints())
            case SdeFileNames.CATEGORIES:
                _ = list(self.categories())
            case SdeFileNames.CERTIFICATES:
                _ = list(self.certificates())
            case SdeFileNames.CHARACTER_ATTRIBUTES:
                _ = list(self.character_attributes())
            case SdeFileNames.COMPRESSIBLE_TYPES:
                _ = list(self.compressible_types())
            case SdeFileNames.CONTRABAND_TYPES:
                _ = list(self.contraband_types())
            case SdeFileNames.CONTROL_TOWER_RESOURCES:
                _ = list(self.control_tower_resources())
            case SdeFileNames.CORPORATION_ACTIVITIES:
                _ = list(self.corporation_activities())
            case SdeFileNames.DEBUFF_COLLECTIONS:
                _ = list(self.debuff_collections())
            case SdeFileNames.DOGMA_ATTRIBUTE_CATEGORIES:
                _ = list(self.dogma_attribute_categories())
            case SdeFileNames.DOGMA_ATTRIBUTES:
                _ = list(self.dogma_attributes())
            case SdeFileNames.DOGMA_EFFECTS:
                _ = list(self.dogma_effects())
            case SdeFileNames.DOGMA_UNITS:
                _ = list(self.dogma_units())
            case SdeFileNames.DYNAMIC_ITEM_ATTRIBUTES:
                _ = list(self.dynamic_item_attributes())
            case SdeFileNames.FACTIONS:
                _ = list(self.factions())
            case SdeFileNames.FREELANCE_JOB_SCHEMAS:
                pass  # Not implemented yet, so we skip validation for this file.
            case SdeFileNames.GRAPHICS:
                _ = list(self.graphics())
            case SdeFileNames.GROUPS:
                _ = list(self.groups())
            case SdeFileNames.ICONS:
                _ = list(self.icons())
            case SdeFileNames.LANDMARKS:
                _ = list(self.landmarks())
            case SdeFileNames.MAP_ASTEROID_BELTS:
                _ = list(self.map_asteroid_belts())
            case SdeFileNames.MAP_CONSTELLATIONS:
                _ = list(self.map_constellations())
            case SdeFileNames.MAP_MOONS:
                _ = list(self.map_moons())
            case SdeFileNames.MAP_PLANETS:
                _ = list(self.map_planets())
            case SdeFileNames.MAP_REGIONS:
                _ = list(self.map_regions())
            case SdeFileNames.MAP_SOLAR_SYSTEMS:
                _ = list(self.map_solar_systems())
            case SdeFileNames.MAP_STARGATES:
                _ = list(self.map_stargates())
            case SdeFileNames.MAP_STARS:
                _ = list(self.map_stars())
            case SdeFileNames.MARKET_GROUPS:
                _ = list(self.market_groups())
            case SdeFileNames.MASTERIES:
                _ = list(self.masteries())
            case SdeFileNames.META_GROUPS:
                _ = list(self.meta_groups())
            case SdeFileNames.NPC_CHARACTERS:
                _ = list(self.npc_characters())
            case SdeFileNames.NPC_CORPORATION_DIVISIONS:
                _ = list(self.npc_corporation_divisions())
            case SdeFileNames.NPC_CORPORATIONS:
                _ = list(self.npc_corporations())
            case SdeFileNames.NPC_STATIONS:
                _ = list(self.npc_stations())
            case SdeFileNames.PLANET_RESOURCES:
                _ = list(self.planet_resources())
            case SdeFileNames.PLANET_SCHEMATICS:
                _ = list(self.planet_schematics())
            case SdeFileNames.RACES:
                _ = list(self.races())
            case SdeFileNames.SDE_INFO:
                _ = self.sde_info()
            case SdeFileNames.SKIN_LICENSES:
                _ = list(self.skin_licenses())
            case SdeFileNames.SKIN_MATERIALS:
                _ = list(self.skin_materials())
            case SdeFileNames.SKINS:
                _ = list(self.skins())
            case SdeFileNames.SOVEREIGNTY_UPGRADES:
                _ = list(self.sovereignty_upgrades())
            case SdeFileNames.STATION_OPERATIONS:
                _ = list(self.station_operations())
            case SdeFileNames.STATION_SERVICES:
                _ = list(self.station_services())
            case SdeFileNames.TRANSLATION_LANGUAGES:
                _ = list(self.translation_languages())
            case SdeFileNames.TYPE_BONUS:
                _ = list(self.type_bonus())
            case SdeFileNames.TYPE_DOGMA:
                _ = list(self.type_dogma())
            case SdeFileNames.TYPE_MATERIALS:
                _ = list(self.type_materials())
            case SdeFileNames.TYPES:
                _ = list(self.eve_types())
            case _:
                raise ValueError(f"Unknown SDE file name: {file_name}")

    def validate_all(self) -> None:
        """Validate all SDE files."""
        for file_name in SdeFileNames:
            self.validate(file_name)
