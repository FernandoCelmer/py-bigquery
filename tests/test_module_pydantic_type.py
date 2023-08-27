import typing

from bigquery_orm.base.bigquery import Type
from bigquery_orm.modules.pydantic.translator import TranslatorPydantic as TR


def test_translator_sqlalchemy_get_type_integer():
    assert TR._type(value=int) == Type.INTEGER
    assert TR._type(value=typing.Optional[int]) == Type.INTEGER


def test_translator_sqlalchemy_get_type_string():
    assert TR._type(value=str) == Type.STRING
    assert TR._type(value=typing.Optional[str]) == Type.STRING
