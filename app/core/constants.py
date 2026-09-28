# app/core/constants.py

"""Structured constants — no magic strings elsewhere in the codebase."""

from enum import StrEnum


class TokenType(StrEnum):
    BEARER = "bearer"


class JWTClaim(StrEnum):
    SUBJECT = "sub"
    EXPIRES_AT = "exp"


class PasswordHashScheme(StrEnum):
    BCRYPT = "bcrypt"


class AuthScheme(StrEnum):
    BEARER = "Bearer"


class HeaderName(StrEnum):
    WWW_AUTHENTICATE = "WWW-Authenticate"


class UserRole(StrEnum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    AGENT = "AGENT"
    CUSTOMER = "CUSTOMER"