"""Domain exception hierarchy.

Nothing in service / controller layers imports HTTPException.
Each class carries both a numeric status_code (HTTP) and a stable string
code (machine-readable) so the frontend can branch on the code, not the text.
"""

from typing import ClassVar


class AppError(Exception):
    status_code: ClassVar[int] = 500
    code: ClassVar[str] = "INTERNAL_ERROR"
    default_message: ClassVar[str] = "An unexpected error occurred."
    headers: ClassVar[dict[str, str] | None] = None

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.default_message
        super().__init__(self.message)


class BadRequestError(AppError):
    status_code = 400
    code = "BAD_REQUEST"
    default_message = "Bad request."


class AuthenticationError(AppError):
    status_code = 401
    code = "UNAUTHENTICATED"
    default_message = "Authentication failed."
    headers = {"WWW-Authenticate": "Bearer"}


class PermissionDeniedError(AppError):
    status_code = 403
    code = "FORBIDDEN"
    default_message = "Permission denied."


class NotFoundError(AppError):
    status_code = 404
    code = "NOT_FOUND"
    default_message = "Resource not found."


class ConflictError(AppError):
    status_code = 409
    code = "CONFLICT"
    default_message = "Resource conflict."


class UnprocessableEntityError(AppError):
    status_code = 422
    code = "UNPROCESSABLE"
    default_message = "Unprocessable entity."