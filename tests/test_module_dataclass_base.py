from tests.conftest import (
    mock_base_table_keys as keys,
    mock_base_table_mapping as mapping
)

from samples import UserDataClass
from py_bigquery.modules.dataclass.base import DataClass


def test_base_sqlalchemy_instance_keys(keys):
    table = DataClass(model_class=UserDataClass)

    assert table.keys == keys


def test_base_sqlalchemy_instance_map(mapping):
    table = DataClass(model_class=UserDataClass)

    assert table.map == mapping
