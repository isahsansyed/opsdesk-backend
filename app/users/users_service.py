from app.core.security import hash_password
from app.users.users_exceptions import UserAlreadyExistsError
from app.users.users_models import User
from app.users.users_repository import UserRepository
from app.users.users_schemas import UserCreate


class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    async def register_user(self, payload: UserCreate) -> User:
        existing = await self.repo.get_by_email(payload.email)
        if existing is not None:
            raise UserAlreadyExistsError()
        return await self.repo.create(
            email=payload.email,
            password_hash=hash_password(payload.password),
            full_name=payload.full_name,
        )