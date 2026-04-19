"""Tests for YAML fixture validation against yaml_records root models."""

import importlib.resources
from importlib.resources.abc import Traversable
from typing import Any

import pytest
import yaml
from pydantic import RootModel

from eve_static_data.models.pydantic import yaml_records


def _yaml_fixture_path(file_name: str) -> Traversable:
    """Get a Traversable to a YAML SDE fixture file.

    Args:
        file_name: Name of the fixture file under tests/resources/sde_data/yaml.

    Returns:
        Traversable to the fixture file.
    """
    return importlib.resources.files("tests.resources.sde_data.yaml") / file_name


def _load_yaml_mapping(file_name: str) -> dict[Any, Any]:
    """Load a YAML fixture expected to have a dictionary root.

    Args:
        file_name: Name of the fixture file under tests/resources/sde_data/yaml.

    Returns:
        Parsed YAML mapping.
    """
    fixture_path = _yaml_fixture_path(file_name)
    with fixture_path.open(encoding="utf-8") as file_handle:
        loaded: Any = yaml.safe_load(file_handle)

    assert isinstance(loaded, dict)
    return loaded  # type: ignore


# Add new dataset/model pairs here as yaml_records.py grows.
YAML_DATASET_CASES: list[tuple[str, type[RootModel[Any]]]] = [
    ("agentsInSpace.yaml", yaml_records.AgentsInSpaceRoot),
    ("agentTypes.yaml", yaml_records.AgentTypesRoot),
    ("ancestries.yaml", yaml_records.AncestriesRoot),
    ("bloodlines.yaml", yaml_records.BloodlinesRoot),
    ("blueprints.yaml", yaml_records.BlueprintsRoot),
    ("categories.yaml", yaml_records.CategoriesRoot),
    ("certificates.yaml", yaml_records.CertificatesRoot),
    ("characterAttributes.yaml", yaml_records.CharacterAttributesRoot),
    ("cloneGrades.yaml", yaml_records.CloneGradesRoot),
    ("compressibleTypes.yaml", yaml_records.CompressibleTypesRoot),
    ("contrabandTypes.yaml", yaml_records.ContrabandTypesRoot),
    ("controlTowerResources.yaml", yaml_records.ControlTowerResourcesRoot),
    ("corporationActivities.yaml", yaml_records.CorporationActivitiesRoot),
    ("dbuffCollections.yaml", yaml_records.DebuffCollectionsRoot),
    ("dogmaAttributeCategories.yaml", yaml_records.DogmaAttributeCategoriesRoot),
    ("dogmaAttributes.yaml", yaml_records.DogmaAttributesRoot),
    ("dogmaEffects.yaml", yaml_records.DogmaEffectsRoot),
    ("dogmaUnits.yaml", yaml_records.DogmaUnitsRoot),
    ("dynamicItemAttributes.yaml", yaml_records.DynamicItemAttributesRoot),
    ("factions.yaml", yaml_records.FactionsRoot),
    ("freelanceJobSchemas.yaml", yaml_records.FreelanceJobSchemasRoot),
    ("graphics.yaml", yaml_records.GraphicsRoot),
    ("groups.yaml", yaml_records.GroupsRoot),
    ("icons.yaml", yaml_records.IconsRoot),
    ("landmarks.yaml", yaml_records.LandmarksRoot),
    ("mapAsteroidBelts.yaml", yaml_records.MapAsteroidBeltsRoot),
    ("mapConstellations.yaml", yaml_records.MapConstellationsRoot),
    ("mapMoons.yaml", yaml_records.MapMoonsRoot),
    ("mapPlanets.yaml", yaml_records.MapPlanetsRoot),
    ("mapRegions.yaml", yaml_records.MapRegionsRoot),
    ("mapSecondarySuns.yaml", yaml_records.MapSecondarySunsRoot),
    ("mapSolarSystems.yaml", yaml_records.MapSolarSystemsRoot),
    ("mapStargates.yaml", yaml_records.MapStargatesRoot),
    ("mapStars.yaml", yaml_records.MapStarsRoot),
    ("marketGroups.yaml", yaml_records.MarketGroupsRoot),
    ("masteries.yaml", yaml_records.MasteriesRoot),
    ("metaGroups.yaml", yaml_records.MetaGroupsRoot),
    ("mercenaryTacticalOperations.yaml", yaml_records.MercenaryTacticalOperationsRoot),
    ("npcCharacters.yaml", yaml_records.NpcCharactersRoot),
    ("npcCorporationDivisions.yaml", yaml_records.NpcCorporationDivisionsRoot),
    ("npcCorporations.yaml", yaml_records.NpcCorporationsRoot),
    ("npcStations.yaml", yaml_records.NpcStationsRoot),
    ("planetResources.yaml", yaml_records.PlanetResourcesRoot),
    ("planetSchematics.yaml", yaml_records.PlanetSchematicsRoot),
    ("races.yaml", yaml_records.RacesRoot),
    ("skinLicenses.yaml", yaml_records.SkinLicensesRoot),
    ("skinMaterials.yaml", yaml_records.SkinMaterialsRoot),
    ("skins.yaml", yaml_records.SkinsRoot),
    ("_sde.yaml", yaml_records.SdeInfoRoot),
    ("sovereigntyUpgrades.yaml", yaml_records.SovereigntyUpgradesRoot),
    ("stationOperations.yaml", yaml_records.StationOperationsRoot),
    ("stationServices.yaml", yaml_records.StationServicesRoot),
    ("translationLanguages.yaml", yaml_records.TranslationLanguagesRoot),
    ("typeBonus.yaml", yaml_records.TypeBonusRoot),
    ("typeDogma.yaml", yaml_records.TypeDogmaRoot),
    ("typeMaterials.yaml", yaml_records.TypeMaterialsRoot),
    ("types.yaml", yaml_records.EveTypesRoot),
]


@pytest.mark.parametrize(
    ("fixture_file_name", "root_model"),
    YAML_DATASET_CASES,
)
def test_yaml_fixtures_validate_against_root_models(
    fixture_file_name: str,
    root_model: type[RootModel[Any]],
) -> None:
    """YAML fixture mappings should validate against their root models."""
    payload = _load_yaml_mapping(fixture_file_name)

    validated = root_model.model_validate(payload)

    assert isinstance(validated, root_model)
    assert validated.model_dump(mode="python")
