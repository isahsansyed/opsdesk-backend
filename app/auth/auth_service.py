import uuid

from jose import JWTError, jwt

from app.auth.auth_exceptions import InactiveUserError, InvalidCredentialsError
from app.auth.auth_schemas import Token, UserLogin
from app.core.config import settings
from app.core.constants import JWTClaim, TokenType
from app.core.security import create_access_token, verify_password
from app.users.users_models import User
from app.users.users_repository import UserRepository


class AuthService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def authenticate(self, credentials: UserLogin) -> Token:
        user = await self.user_repo.get_by_email(credentials.email)
        if user is None or not verify_password(credentials.password, user.password_hash):
            raise InvalidCredentialsError()
        if not user.is_active:
            raise InactiveUserError()
        return Token(
            access_token=create_access_token(subject=user.id),
            token_type=TokenType.BEARER.value,
        )

    async def resolve_user_from_token(self, token: str) -> User:
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            subject = payload.get(JWTClaim.SUBJECT.value)
            if subject is None:
                raise InvalidCredentialsError()
            user_id = uuid.UUID(subject)
        except (JWTError, ValueError) as exc:
            raise InvalidCredentialsError() from exc

        user = await self.user_repo.get_by_id(user_id)
        if user is None:
            raise InvalidCredentialsError()
        if not user.is_active:
            raise InactiveUserError()
        return user