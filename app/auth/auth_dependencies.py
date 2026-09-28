from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.auth.auth_controller import AuthController
from app.auth.auth_service import AuthService
from app.users.users_dependencies import get_user_repository, get_user_service
from app.users.users_models import User
from app.users.users_repository import UserRepository
from app.users.users_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(user_repo)


def get_auth_controller(
    auth_service: AuthService = Depends(get_auth_service),
    user_service: UserService = Depends(get_user_service),
) -> AuthController:
    return AuthController(auth_service, user_service)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    service: AuthService = Depends(get_auth_service),
) -> User:
    return await service.resolve_user_from_token(token)