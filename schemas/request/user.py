# Pydantic
from pydantic import Field


# Schemas
from schemas.base import UserBase


class UserRegisterIn(UserBase):
    password: str = Field(..., min_length=8)
    phone: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)


class UserLoginIn(UserBase):
    password: str = Field(..., min_length=8)
