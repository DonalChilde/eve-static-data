import json
import logging
from dataclasses import dataclass
from typing import Any, TypedDict

from pydantic import ValidationError

from eve_static_data.helpers.pydantic.jsonl_record import (
    BASE_MODELS,
    TransformerProtocol,
)
from eve_static_data.models.type_defs import Lang

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class ModelValidationErrorRecord:
    model: str
    line_number: int
    data: str
    error_messages: list[str]


def is_published_false(text: str) -> bool:
    """Check if the text contains "published": false.

    This is used to identify records that are not published.
    Unpublished records fail validation more often.
    """
    return '"published": false' in text


class ValidModels(TransformerProtocol):
    """A transformer that validates the models and records any validation errors.

    This transformer checks if the record is not published and records that information.
    It also catches any validation errors and records them in a dictionary.
    """

    def __init__(self):
        """Initialize the class."""
        self.validation_errors: dict[int, ModelValidationErrorRecord] = {}
        self.not_published: list[int] = []

    def transform(
        self, value: tuple[int, str], model: type[BASE_MODELS]
    ) -> BASE_MODELS | None:
        """Transform an indexed string into a pydantic BaseModel instance, and record any validation errors."""
        index, text = value
        try:
            text = self._inspect_string(index, text)
            return self._text_to_model(index, text, model)
        except ValidationError as e:
            if index not in self.validation_errors:
                self.validation_errors[index] = ModelValidationErrorRecord(
                    model=model.__name__,
                    line_number=index,
                    data=text,
                    error_messages=[str(e)],
                )
            else:
                self.validation_errors[index].error_messages.append(str(e))
            logger.exception(
                "Validation error parsing line %d: %s in class %s",
                index,
                e,
                model.__name__,
            )
        except Exception as e:
            if index not in self.validation_errors:
                self.validation_errors[index] = ModelValidationErrorRecord(
                    model=model.__name__,
                    line_number=index,
                    data=text,
                    error_messages=[str(e)],
                )
            else:
                self.validation_errors[index].error_messages.append(str(e))
            logger.exception(
                "Unexpected error parsing line %d: %s in class %s",
                index,
                e,
                model.__name__,
            )
            return None

    def _inspect_string(self, index: int, text: str) -> str:
        """Inspect the string before model creation.

        Check if the record is not published and record that information.
        """
        if is_published_false(text):
            self.not_published.append(index)
        return text

    def _text_to_model(
        self, index: int, text: str, model: type[BASE_MODELS]
    ) -> BASE_MODELS:
        """Convert the text to a model instance."""
        return model.model_validate_json(text)


class LocalizedString(TypedDict):
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


def localize_string_dict(string_dict: LocalizedString | None, lang: Lang = "en") -> str:
    """Extract the localized string from a LocalizedString.

    Args:
        string_dict: The LocalizedString to extract from.
        lang: The language code to extract (default is "en" for English).

    Returns:
        The localized string for the specified language, OR:
        - "TRANSLATIONS_NOT_PRESENT" if the input string_dict is None (indicating that the translations are not present in the dataset).
        - "NOT_TRANSLATED" if the specified language is not found in the string_dict (indicating that the translation for that language is not provided).
    """
    if string_dict is None:
        return "TRANSLATIONS_NOT_PRESENT"
    if lang not in string_dict:
        logger.warning(
            f"Localized string for '{lang=}' not found. Available languages: {list(string_dict.keys())}"
        )
        return "NOT_TRANSLATED"
    return string_dict[lang]


class LocalizationTransformer(ValidModels):
    """A transformer that validates the models and records any validation errors, and also checks for missing localizations."""

    def __init__(self, localized_fields: list[str], lang: Lang = "en"):
        """Initialize the class."""
        super().__init__()
        self.localized_fields = localized_fields
        self.lang: Lang = lang

    def _text_to_model(
        self, index: int, text: str, model: type[BASE_MODELS]
    ) -> BASE_MODELS:
        """Convert the text to a model instance, after localizing any specified fields."""
        json_dict = self._transform_dict(index, text)
        return model.model_validate(json_dict)

    def _transform_dict(self, index: int, text: str) -> dict[str, Any]:
        """Convert the text to a dictionary, after localizing any specified fields."""
        json_dict = json.loads(text)
        for field in self.localized_fields:
            if field in json_dict:
                json_dict[field] = localize_string_dict(json_dict[field], self.lang)
        return json_dict
