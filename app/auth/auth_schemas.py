import uuid

from pydantic import BaseModel, EmailStr

from app.core.constants import TokenType


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = TokenType.BEARER.value


class TokenData(BaseModel):
    user_id: uuid.UUID | None = None