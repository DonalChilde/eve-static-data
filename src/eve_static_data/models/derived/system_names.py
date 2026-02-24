from typing import Self

from eve_static_data.models.datasets import localized_pydantic as LDS
from eve_static_data.models.datasets.sde_dataset_base import LocalizedSdeDataset


class SystemNames(LocalizedSdeDataset):
    data: dict[int, str]

    @classmethod
    def from_datasets(
        cls, map_solar_systems_dataset: LDS.MapSolarSystemsLocalizedDataset
    ) -> Self:
        """Create a SystemNames instance from the MapSolarSystemsLocalizedDataset."""
        return cls(
            localized=map_solar_systems_dataset.localized,
            build_number=map_solar_systems_dataset.build_number,
            release_date=map_solar_systems_dataset.release_date,
            data={
                system.key: system.name
                for system in map_solar_systems_dataset.data.values()
            },
        )
