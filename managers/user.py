# PassLib
from passlib.context import CryptContext

# Fastapi
from fastapi import HTTPException, status

# Manager
from managers.auth import AuthManager

# DB
from db import database

# Models
from models import user
from models.enums import RoleType

# Utils
from asyncpg import UniqueViolationError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])
        user_data["active"] = True
        try:
            id_ = await database.execute(user.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email exists.",
            )

        user_do = await database.fetch_one(user.select().where(user.c.id == id_))
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def login(user_data):

        user_do = await database.fetch_one(
            user.select().where(user.c.email == user_data["email"])
        )

        if user_do and user_do["active"] == False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Your account is deactivated, contact the administrator. ",
            )
        if not user_do:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Wrong email or password",
            )
        elif not pwd_context.verify(user_data["password"], user_do["password"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Wrong email or password",
            )

        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_all_users():
        try:
            result = await database.fetch_all(
                user.select().where(user.c.active == True)
            )
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="without results. ",
                )
            return result
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Please contact the administrator.",
            )

    @staticmethod
    async def get_user_by_email(email):
        try:
            result = await database.fetch_all(
                user.select().where(user.c.email == email, user.c.active == True)
            )

            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="without results. ",
                )
            return result
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Please contact the administrator.",
            )

    @staticmethod
    async def change_role_user(role: RoleType, user_id):
        try:
            await database.execute(
                user.update()
                .where(user.c.id == user_id, user.c.active == True)
                .values(role=role)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Please contact the administrator.",
            )
