"""Lazy loader for localized pydantic models."""

from ..models import localized_pydantic as LP
from .raw_json_td_protocol import RawJsonTDProtocol


class LocalizedLazyLoader:
    def __init__(
        self, access: RawJsonTDProtocol, lang: str = "en", only_published: bool = True
    ) -> None:
        """A Lazy loading container for localized pydantic models of the EVE sde.

        Args:
            access: An access object implementing RawJsonTDProtocol to load raw static data.
            lang: The language code for localization (default is "en").
            only_published: Whether to include only published data (default is True).
        """
        self.access = access
        self.lang = lang
        self.only_published = only_published
        self.sde_info = LP.SdeInfo.from_td(access.sde_info())
        self._blueprints: LP.Blueprints | None = None
        self._categories: LP.Categories | None = None
        self._groups: LP.Groups | None = None
        self._market_groups: LP.MarketGroups | None = None
        self._meta_groups: LP.MetaGroups | None = None
        self._type_materials: LP.TypeMaterials | None = None
        self._eve_types: LP.EveTypes | None = None
        self._regions: LP.Regions | None = None

    @property
    def blueprints(self) -> LP.Blueprints:
        if self._blueprints is None:
            self._blueprints = LP.Blueprints.from_static_data(
                static_data=self.access.blueprints(),
                sde_info=self.sde_info,
                only_published=self.only_published,
            )
        return self._blueprints

    @property
    def categories(self) -> LP.Categories:
        if self._categories is None:
            self._categories = LP.Categories.from_static_data(
                static_data=self.access.categories(),
                sde_info=self.sde_info,
                only_published=self.only_published,
                localized=self.lang,
            )
        return self._categories

    @property
    def groups(self) -> LP.Groups:
        if self._groups is None:
            self._groups = LP.Groups.from_static_data(
                static_data=self.access.groups(),
                sde_info=self.sde_info,
                only_published=self.only_published,
                localized=self.lang,
            )
        return self._groups

    @property
    def market_groups(self) -> LP.MarketGroups:
        if self._market_groups is None:
            self._market_groups = LP.MarketGroups.from_static_data(
                static_data=self.access.market_groups(),
                sde_info=self.sde_info,
                localized=self.lang,
            )
        return self._market_groups

    @property
    def meta_groups(self) -> LP.MetaGroups:
        if self._meta_groups is None:
            self._meta_groups = LP.MetaGroups.from_static_data(
                static_data=self.access.meta_groups(),
                sde_info=self.sde_info,
                localized=self.lang,
            )
        return self._meta_groups

    @property
    def type_materials(self) -> LP.TypeMaterials:
        if self._type_materials is None:
            self._type_materials = LP.TypeMaterials.from_static_data(
                static_data=self.access.type_materials(),
                sde_info=self.sde_info,
            )
        return self._type_materials

    @property
    def eve_types(self) -> LP.EveTypes:
        if self._eve_types is None:
            self._eve_types = LP.EveTypes.from_static_data(
                static_data=self.access.eve_types(),
                sde_info=self.sde_info,
                only_published=self.only_published,
                localized=self.lang,
            )
        return self._eve_types

    @property
    def regions(self) -> LP.Regions:
        if self._regions is None:
            self._regions = LP.Regions.from_static_data(
                static_data=self.access.map_regions(),
                sde_info=self.sde_info,
                localized=self.lang,
            )
        return self._regions
