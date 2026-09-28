# app/users/users_controller.py
from app.core.response import ApiResponse
from app.users.users_models import User
from app.users.users_schemas import UserCreate, UserResponse
from app.users.users_service import UserService


class UserController:
    def __init__(self, service: UserService) -> None:
        self.service = service

    async def register(self, payload: UserCreate) -> ApiResponse[UserResponse]:
        user = await self.service.register_user(payload)
        return ApiResponse.ok(UserResponse.model_validate(user))

    async def profile(self, user: User) -> ApiResponse[UserResponse]:
        return ApiResponse.ok(UserResponse.model_validate(user))