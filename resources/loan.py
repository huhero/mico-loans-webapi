# FastApi
from fastapi import APIRouter, Depends, Request


# Managers
from managers.auth import is_admin, oauth2_scheme, is_complainer, is_approver
from managers.loan import LoanManager

# Schemas
from schemas.request.loan import LoanIn
from schemas.response.loan import LoanOut

# Utils
from typing import List, Optional

router = APIRouter(tags=["Loans"])


@router.get(
    "/loans/", dependencies=[Depends(oauth2_scheme)], response_model=List[LoanOut]
)
async def get_loans(request: Request):
    user = request.state.user
    return await LoanManager.get_loans(user)


@router.post(
    "/loans/",
    dependencies=[Depends(oauth2_scheme), Depends(is_complainer)],
    response_model=LoanOut,
)
async def create_loan(request: Request, loan: LoanIn):
    user = request.state.user
    return await LoanManager.create_loan(loan.dict(), user)


@router.delete(
    "/loans/{loan_id}/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=204,
)
async def delete_loan(loan_id: int):
    await LoanManager.delete_loan(loan_id)


@router.put(
    "/loans/{loan_id}/approve",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    responses={204: {"model": None}},
)
async def approve_loan(loan_id: int):
    await LoanManager.approve(loan_id)


@router.put(
    "/loans/{loan_id}/rejected",
    dependencies=[Depends(oauth2_scheme), Depends(is_approver)],
    status_code=204,
)
async def rejected_loan(loan_id: int):
    await LoanManager.rejected(loan_id)
