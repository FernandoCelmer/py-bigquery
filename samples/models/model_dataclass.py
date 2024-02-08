from typing import Optional
from dataclasses import dataclass, field


@dataclass
class UserDataClass:
    __tablename__ = 'user'
    __table_id__ = 'py-bigquery.dataset.user'

    id: int
    email: Optional[str] = field(default=None, metadata={"description": "Customer Contact"})
