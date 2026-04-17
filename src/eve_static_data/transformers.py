"""Trnasformer classes for use in the data loading process."""

import json
import logging
from dataclasses import dataclass
from typing import Any

from pydantic import ValidationError

from eve_static_data.helpers.jsonl_reader import BASE_MODELS, PydanticTransformer
from eve_static_data.models.type_defs import Lang, LocalizedString

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

    AFAIK, the "published" field is only present in some datasets, at the top level of the record.
    So, this function is a simple string check, rather than parsing the JSON and checking the field.
    """
    return '"published": false' in text


def is_published(text: str) -> bool:
    """Check if the text contains "published": false."""
    if '"published": false' in text:
        return False
    return True


class ModelLoader(PydanticTransformer[BASE_MODELS]):
    def __init__(
        self,
        model: type[BASE_MODELS],
        only_published: bool,
        skip_validation_failures: bool,
    ):
        """A transformer that validates the models and records any validation errors.

        This transformer
        - checks if the record is not published and if not, records the line number.
        - catches any validation errors and records them in a dictionary.
        - optionally skips unpublished records before validation
        - optionally skips validation failures and continues processing the rest of the records.

        Args:
            model: The Pydantic model class to use for validation.
            only_published: Whether to only include published records.
            skip_validation_failures: Whether to skip validation failures.
        """
        super().__init__(model)
        self.validation_errors: dict[int, ModelValidationErrorRecord] = {}
        self.line_record_not_published: set[int] = set()
        self.only_published = only_published
        self.skip_validation_failures = skip_validation_failures

    def __call__(self, value: tuple[int, str]) -> tuple[int, BASE_MODELS | None]:
        """Transform an indexed string into a pydantic BaseModel instance, and record any validation errors."""
        return super().__call__(value)

    def _inspect_string(self, index: int, text: str) -> str:
        """Inspect the string before model creation.

        Check if the record is not published and record that information.
        """
        if is_published_false(text):
            self.line_record_not_published.add(index)
        return text

    def _text_to_model(self, index: int, text: str) -> BASE_MODELS | None:
        """Convert the text to a model instance."""
        if self.only_published and index in self.line_record_not_published:
            return None
        try:
            return self.model.model_validate_json(text)
        except ValidationError as e:
            self.validation_errors[index] = ModelValidationErrorRecord(
                model=self.model.__name__,
                line_number=index,
                data=text,
                error_messages=[err["msg"] for err in e.errors()],
            )
            if self.skip_validation_failures:
                return None
            logger.exception(
                f"Validation error for model {self.model.__name__} at line {index}:{text} {e}"
            )
            raise e


# TODO add model.name and field for error messages.
def localize_string_dict(
    string_dict: LocalizedString | None, model: str, field: str, lang: Lang = "en"
) -> str:
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
        logger.warning(
            f"Localized string dictionary is None for model '{model}' and field '{field}', indicating that translations are not present in the dataset."
        )
        return "TRANSLATIONS_NOT_PRESENT"
    if lang not in string_dict:
        logger.warning(
            f"Localized string for '{lang=}' not found for model '{model}' and field '{field}'. Available languages: {list(string_dict.keys())}"
        )
        return "NOT_TRANSLATED"
    return string_dict[lang]


class LocalizationTransformer(PydanticTransformer[BASE_MODELS]):
    def __init__(
        self,
        model: type[BASE_MODELS],
        localized_fields: list[str],
        only_published: bool,
        skip_validation_failures: bool,
        lang: Lang = "en",
    ):
        """A transformer that localizes and validates the models and records any validation errors.

        This transformer
        - checks if the record is not published and if not, records the line number.
        - json.loads the text and localizes any specified fields in the model.
        - catches any validation errors and records them in a dictionary.
        - optionally skips unpublished records before validation
        - optionally skips validation failures and continues processing the rest of the records.

        Args:
            model: The Pydantic model class to use for validation.
            only_published: Whether to only include published records.
            skip_validation_failures: Whether to skip validation failures.
            localized_fields: A list of field names in the model that should be localized.
            lang: The language code to use for localization (default is "en" for English).
        """
        super().__init__(model)
        self.localized_fields = localized_fields
        self.lang: Lang = lang
        self.only_published = only_published
        self.validation_errors: dict[int, ModelValidationErrorRecord] = {}
        self.line_record_not_published: set[int] = set()
        self.skip_validation_failures = skip_validation_failures

    def _inspect_string(self, index: int, text: str) -> str:
        """Inspect the string before model creation.

        Check if the record is not published and record that information.
        """
        if is_published_false(text):
            self.line_record_not_published.add(index)
        return text

    def _text_to_model(self, index: int, text: str) -> BASE_MODELS | None:
        """Convert the text to a model instance, after localizing any specified fields."""
        if self.only_published and index in self.line_record_not_published:
            return None
        json_dict = self._transform_dict(index, text)
        try:
            return self.model.model_validate(json_dict)
        except ValidationError as e:
            self.validation_errors[index] = ModelValidationErrorRecord(
                model=self.model.__name__,
                line_number=index,
                data=text,
                error_messages=[err["msg"] for err in e.errors()],
            )
            if self.skip_validation_failures:
                return None
            logger.exception(
                f"Validation error for model {self.model.__name__} at line {index}:{text} {e}"
            )
            raise e

    def _transform_dict(self, index: int, text: str) -> dict[str, Any]:
        """Convert the text to a dictionary, after localizing any specified fields."""
        json_dict = json.loads(text)
        for field in self.localized_fields:
            field_dict = json_dict.get(field)
            localized_field = localize_string_dict(
                field_dict, self.model.__name__, field, self.lang
            )
            json_dict[field] = localized_field
        return json_dict
