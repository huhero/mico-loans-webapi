# Models
from models.enums import RoleType

# Schemas
from schemas.base import UserBase

# Utils
from datetime import datetime


class UserOut(UserBase):
    id: int
    phone: str
    first_name: str
    last_name: str
    role: RoleType
    active: bool
    created_at: datetime
    last_updated: datetime
