"""Common type definitions for the EVE static data models."""

from enum import StrEnum
from typing import Literal

type Lang = Literal["en", "de", "fr", "ja", "ru", "zh", "ko", "es"]
"""A type representing the supported languages for localization."""


class LangEnum(StrEnum):
    EN = "en"
    DE = "de"
    FR = "fr"
    JA = "ja"
    RU = "ru"
    ZH = "zh"
    KO = "ko"
    ES = "es"


"""An enum representing the supported languages for localization."""
