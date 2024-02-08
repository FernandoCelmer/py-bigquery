from py_bigquery.base.bigquery import Mode
from py_bigquery.modules.sqlalchemy.translator import TranslatorSQLAlchemy as TR


def test_translator_sqlalchemy_get_mode_required():
    assert TR._mode(value=False) == Mode.REQUIRED


def test_translator_sqlalchemy_get_mode_nullable():
    assert TR._mode(value=True) == Mode.NULLABLE
