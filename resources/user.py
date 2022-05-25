# FastApi
from fastapi import APIRouter, Depends, status

# Managers
from managers.auth import oauth2_scheme, is_admin
from managers.user import UserManager
from models.enums import RoleType

# Schemas
from schemas.response.user import UserOut

# Utils
from typing import List, Optional


router = APIRouter(tags=["Users"])


@router.get(
    path="/users/",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    response_model=List[UserOut],
    status_code=status.HTTP_200_OK,
)
async def get_users(email: Optional[str] = None):
    """
    Get all Users

    This path operation retrive all users or a user especific by email in the app.

    Returns a list json with the basic information.
    * id: int.
    * phone: str.
    * first_name: str.
    * last_name: str.
    * role: RoleType.
    * active: bool.
    * created_at: datetime.
    * last_updated: datetime.
    """
    if email:
        return await UserManager.get_user_by_email(email)

    return await UserManager.get_all_users()


@router.put(
    path="/users/{user_id}/make_admin",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=status.HTTP_204_NO_CONTENT,
    responses={204: {"model": None}},
)
async def make_admin(user_id: int):
    """
    Make user admin

    This path operation make user admin.
    """
    await UserManager.change_role_user(RoleType.admin, user_id)


@router.put(
    path="/users/{user_id}/make_approver",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=status.HTTP_204_NO_CONTENT,
    responses={204: {"model": None}},
)
async def make_approver(user_id: int):
    """
    Make user approver

    This path operation make user admin.
    """
    await UserManager.change_role_user(RoleType.approver, user_id)


@router.put(
    path="/users/{user_id}/make_complainer",
    dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
    status_code=status.HTTP_204_NO_CONTENT,
    responses={204: {"model": None}},
)
async def make_complainer(user_id: int):
    """
    Make user complainer

    This path operation make user admin.
    """
    await UserManager.change_role_user(RoleType.complainer, user_id)
