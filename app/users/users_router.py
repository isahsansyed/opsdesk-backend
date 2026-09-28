# app/users/users_router.py
from fastapi import APIRouter, Depends

from app.auth.auth_dependencies import get_current_user
from app.core.response import ApiResponse
from app.users.users_controller import UserController
from app.users.users_dependencies import get_user_controller
from app.users.users_models import User
from app.users.users_schemas import UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=ApiResponse[UserResponse])
async def read_users_me(
    current_user: User = Depends(get_current_user),
    controller: UserController = Depends(get_user_controller),
) -> ApiResponse[UserResponse]:
    return await controller.profile(current_user)