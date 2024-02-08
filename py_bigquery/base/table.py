import logging

from py_bigquery.base.manager import BaseManager
from py_bigquery.exception import ExceptionInvalidModel
from py_bigquery.modules import DataClass, Pydantic, SQLAlchemy


class BaseTable:

    def __new__(cls, model_class: object, client: object = None) -> BaseManager:
        try:
            if hasattr(model_class, "__dataclass_fields__"):
                return DataClass(model_class=model_class, client=client)

            elif model_class.__class__.__name__ == "ModelMetaclass":
                return Pydantic(model_class=model_class, client=client)

            elif model_class.__class__.__name__ == "DeclarativeMeta":
                return SQLAlchemy(model_class=model_class, client=client)

            else:
                raise ExceptionInvalidModel()

        except ExceptionInvalidModel as error:
            logging.error(error)
