# FastApi
from fastapi import UploadFile

# Schema Base
from schemas.base import BaseLoan

# utils
from typing import Optional


class LoanIn(BaseLoan):
    # encoded_document: str
    # extension: str
    pass
