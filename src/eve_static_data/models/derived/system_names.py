"""System names derived from the MapSolarSystemsLocalizedDataset."""

from typing import Self

from eve_static_data.models.pydantic import localized_datasets as LDS


class SystemNames(LDS.SdeDatasetLocalized):
    records: dict[int, str]

    @classmethod
    def from_datasets(
        cls, map_solar_systems_dataset: LDS.MapSolarSystemsLocalizedDataset
    ) -> Self:
        """Create a SystemNames instance from the MapSolarSystemsLocalizedDataset."""
        return cls(
            lang=map_solar_systems_dataset.lang,
            build_number=map_solar_systems_dataset.build_number,
            release_date=map_solar_systems_dataset.release_date,
            records={
                system.key: system.name
                for system in map_solar_systems_dataset.records.values()
            },
        )
