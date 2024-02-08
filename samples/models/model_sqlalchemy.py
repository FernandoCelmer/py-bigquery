from py_bigquery._internal import (
    SQLAlchemyColumn as Column,
    SQLAlchemyInteger as Integer,
    SQLAlchemyString as String
)
from py_bigquery._internal import SQLAlchemyDeclarativeBase as declarative_base

Base = declarative_base()


class UserSQLAlchemy(Base):
    __tablename__ = 'user'
    __table_id__ = 'py-bigquery.dataset.user'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=True, comment="Customer Contact")
