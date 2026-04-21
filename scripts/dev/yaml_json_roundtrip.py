# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pydantic>=2.12.5",
#     "pyyaml>=6.0.3",
#     "typer>=0.24.1",
# ]
# ///
import json
from pathlib import Path
from time import perf_counter
from typing import Annotated, Any

import typer
from pydantic import RootModel
from yaml import safe_load

import eve_static_data.models.pydantic.yaml_datasets
from eve_static_data.models.pydantic import yaml_records

app = typer.Typer()

YAML_DATASET_CASES: list[tuple[str, type[RootModel[Any]]]] = [
    (
        "agentsInSpace.yaml",
        eve_static_data.models.pydantic.yaml_datasets.AgentsInSpaceRoot,
    ),
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


@app.command()
def main(
    sde_path: Annotated[Path, typer.Argument(..., help="Path to the SDE directory")],
    output_path: Annotated[
        Path, typer.Argument(..., help="Path to output the JSON files to")
    ],
) -> None:
    """Script to test YAML fixture round-tripping through JSON."""
    for file_name, root_model in YAML_DATASET_CASES:
        yaml_file_path = sde_path / file_name
        print(f"Processing {yaml_file_path}...")
        with yaml_file_path.open(encoding="utf-8") as file_handle:
            start = perf_counter()
            loaded: Any = safe_load(file_handle)
            print(
                f"\tLoaded {file_name} with pyyaml in {perf_counter() - start:.2f} seconds, now validating against {root_model.__name__}..."
            )

        assert isinstance(loaded, dict)
        start = perf_counter()
        model_instance = root_model.model_validate(loaded)
        print(
            f"\tValidated {file_name} against {root_model.__name__} in {perf_counter() - start:.2f} seconds, now dumping to JSON..."
        )
        json_output = model_instance.model_dump_json(indent=2)

        output_file_path = output_path / file_name.replace(".yaml", ".json")
        output_file_path.parent.mkdir(parents=True, exist_ok=True)
        start = perf_counter()
        output_file_path.write_text(json_output, encoding="utf-8")
        print(
            f"\tDumped {file_name} to JSON via pydantic in {perf_counter() - start:.2f} seconds at {output_file_path}."
        )
        start = perf_counter()
        with open(output_file_path, encoding="utf-8") as file_handle:
            reloaded = root_model.model_validate_json(file_handle.read())
        print(
            f"\tReloaded {file_name} from JSON via pydantic in {perf_counter() - start:.2f} seconds."
        )
        start = perf_counter()
        with open(output_file_path, encoding="utf-8") as file_handle:
            reloaded_json = json.load(file_handle)
        print(
            f"\tReloaded {file_name} from JSON using standard json.load in {perf_counter() - start:.2f} seconds, final validation successful."
        )


if __name__ == "__main__":
    app()
