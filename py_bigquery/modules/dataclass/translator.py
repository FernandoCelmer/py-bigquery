import typing

from typing import Any

from dataclasses import _MISSING_TYPE
from py_bigquery.base.bigquery import Mode, Type


class TranslatorDataClass:

    @staticmethod
    def _type(value: Any):
        objects = {
            int: Type.INTEGER,
            str: Type.STRING,
            typing.Optional[int]: Type.INTEGER,
            typing.Optional[str]: Type.STRING,
        }
        return objects.get(value)

    @staticmethod
    def _mode(value: Any):
        objects = {
            _MISSING_TYPE: Mode.REQUIRED
        }
        return objects.get(value, Mode.NULLABLE)
