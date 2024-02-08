from py_bigquery.base.bigquery import Type
from py_bigquery._internal import SQLAlchemyInteger, SQLAlchemyString
from py_bigquery.modules.sqlalchemy.translator import TranslatorSQLAlchemy as TR


def test_translator_sqlalchemy_get_type_integer():
    assert TR._type(value=SQLAlchemyInteger) == Type.INTEGER


def test_translator_sqlalchemy_get_type_string():
    assert TR._type(value=SQLAlchemyString) == Type.STRING
