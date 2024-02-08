from py_bigquery.base.bigquery import Mode
from py_bigquery.modules.pydantic.translator import TranslatorPydantic as TR


def test_translator_pydantic_get_mode_required():
    assert TR._mode(value=True) == Mode.REQUIRED


def test_translator_pydantic_get_mode_nullable():
    assert TR._mode(value=False) == Mode.NULLABLE
