# Schema Base
from schemas.base import BaseLoan

# Models
from models import State

# Utils
from datetime import datetime


class LoanOut(BaseLoan):
    id: int
    state: State
    created_at: datetime
    last_updated: datetime
