"""Password hashing + JWT token creation."""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.core.constants import JWTClaim, PasswordHashScheme

_pwd_context = CryptContext(
    schemes=[PasswordHashScheme.BCRYPT.value],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    return _pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return _pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: Any, expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    payload = {
        JWTClaim.SUBJECT.value: str(subject),
        JWTClaim.EXPIRES_AT.value: expire,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)