# Schema Base
from schemas.base import BaseLoan

# Models
from models import State

# Utils
from datetime import datetime
from typing import Optional


class LoanOut(BaseLoan):
    id: int
    contract_document_url: Optional[str]
    state: State
    created_at: datetime
    last_updated: datetime
