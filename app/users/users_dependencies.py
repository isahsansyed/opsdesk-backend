#app/users/users_dependencies.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.users.users_repository import UserRepository
from app.users.users_service import UserService
from app.users.users_controller import UserController


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)


def get_user_controller(
    service: UserService = Depends(get_user_service),
) -> UserController:
    return UserController(service)