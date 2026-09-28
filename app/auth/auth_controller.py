from app.auth.auth_schemas import Token, UserLogin
from app.auth.auth_service import AuthService
from app.core.response import ApiResponse
from app.users.users_schemas import UserCreate, UserResponse
from app.users.users_service import UserService


class AuthController:
    def __init__(self, auth_service: AuthService, user_service: UserService) -> None:
        self.auth_service = auth_service
        self.user_service = user_service

    async def register(self, payload: UserCreate) -> ApiResponse[UserResponse]:
        user = await self.user_service.register_user(payload)
        return ApiResponse.ok(UserResponse.model_validate(user))

    async def login(self, credentials: UserLogin) -> ApiResponse[Token]:
        token = await self.auth_service.authenticate(credentials)
        return ApiResponse.ok(token)