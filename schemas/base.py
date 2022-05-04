# Pydantic
from pydantic import BaseModel


class BaseLoan(BaseModel):
    contract_id: str
    amount: float
    term: int
    interest_rate: float


class UserBase(BaseModel):
    email: str
