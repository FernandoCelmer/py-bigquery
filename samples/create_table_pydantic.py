from google.cloud.bigquery import Client

from py_bigquery import Table
from samples import UserPydantic


def create_table_pydantic(client: Client) -> None:
    table = Table(model_class=UserPydantic, client=client)
    table.create()
