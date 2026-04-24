# from eve_static_data.models.common import (
#     TRANSLATION_MISSING,
#     Lang,
#     LocalizableRecord,
#     lang_check,
# )


# def narrow_localizable_record(
#     record: LocalizableRecord, langs: set[Lang]
# ) -> LocalizableRecord:
#     """Narrow a LocalizableRecord to a specific language.

#     Args:
#         record: The LocalizableRecord to narrow.
#         langs: The set of languages to narrow to.

#     Returns:
#         A new LocalizableRecord containing only the translation for the target language.
#     """
#     if not langs:
#         raise ValueError("At least one language must be specified.")
#     localized_fields = set(record.localized_fields(lang=None).keys())
#     for lang in langs:
#         lang_check(lang)
#     for field_name in localized_fields:
#         field = getattr(record, field_name)
#         if field is None:
#             continue
#         new_field = {lang: field.get(lang, TRANSLATION_MISSING) for lang in langs}
#         setattr(record, field_name, new_field)
#     return record
