"""Common type definitions for the EVE static data models."""

from enum import StrEnum
from typing import Literal, TypedDict

TRANSLATION_MISSING = "NOT_AVAILABLE"

type Lang = Literal["en", "de", "fr", "ja", "ru", "zh", "ko", "es"]
"""A type representing the supported languages for localization."""

PossibleTranslationLanguages = {"en", "de", "fr", "ja", "ru", "zh", "ko", "es"}


class LangEnum(StrEnum):
    """An enum representing the supported languages for localization."""

    EN = "en"
    DE = "de"
    FR = "fr"
    JA = "ja"
    RU = "ru"
    ZH = "zh"
    KO = "ko"
    ES = "es"


def lang_check(lang: Lang) -> None:
    """Helper function to check if a language is valid."""
    if lang not in PossibleTranslationLanguages:
        raise ValueError(
            f"Invalid language: {lang}. Must be one of {PossibleTranslationLanguages}."
        )


class LocalizedString(TypedDict, total=False):
    """The shape of a localized string.

    The languages are defined in the SDE file: translationLanguages.jsonl
    """

    en: str
    de: str
    fr: str
    ja: str
    zh: str
    ru: str
    ko: str
    es: str


class LocalizableRecord:
    def localized_fields(self, lang: Lang) -> dict[str, str]:
        """Returns a dict of the localized fields in the model."""
        raise NotImplementedError("This method should be implemented by subclasses.")
