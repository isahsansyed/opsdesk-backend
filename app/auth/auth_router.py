from fastapi import APIRouter, Depends, status

from app.auth.auth_controller import AuthController
from app.auth.auth_dependencies import get_auth_controller
from app.auth.auth_schemas import Token, UserLogin
from app.core.response import ApiResponse
from app.users.users_schemas import UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=ApiResponse[UserResponse],
    status_code=status.HTTP_201_CREATED,
)
async def register(
    payload: UserCreate,
    controller: AuthController = Depends(get_auth_controller),
) -> ApiResponse[UserResponse]:
    return await controller.register(payload)


@router.post(
    "/login",
    response_model=ApiResponse[Token],
    status_code=status.HTTP_200_OK,
)
async def login(
    credentials: UserLogin,
    controller: AuthController = Depends(get_auth_controller),
) -> ApiResponse[Token]:
    return await controller.login(credentials)