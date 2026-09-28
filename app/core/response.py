"""Standard API response envelope.

Every endpoint returns one of these, success or failure. Errors are produced
by app.core.error_handlers so the wire format is identical everywhere.
"""

from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: list[dict] | None = None


class PaginationMeta(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int


class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: ErrorDetail | None = None
    meta: PaginationMeta | None = None

    @classmethod
    def ok(cls, data: T, meta: PaginationMeta | None = None) -> "ApiResponse[T]":
        return cls(success=True, data=data, error=None, meta=meta)

    @classmethod
    def fail(
        cls,
        code: str,
        message: str,
        details: list[dict] | None = None,
    ) -> "ApiResponse[None]":
        return cls(
            success=False,
            data=None,
            error=ErrorDetail(code=code, message=message, details=details),
        )