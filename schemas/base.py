# Pydantic
from pydantic import BaseModel, EmailStr, Field


class BaseLoan(BaseModel):
    contract_id: str = Field(...)
    amount: float = Field(..., gt=0)
    term: int = Field(..., gt=0)
    interest_rate: float = Field(..., ge=0.01, le=1.00)


class UserBase(BaseModel):
    email: EmailStr = Field(...)
