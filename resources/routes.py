# FastApi
from fastapi import APIRouter

# resources
from resources import auth, loan, user

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(loan.router)
api_router.include_router(user.router)
