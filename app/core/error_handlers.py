"""Global exception handlers — the only place AppError meets HTTP."""

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.exceptions import AppError
from app.core.messages import GeneralMessages
from app.core.response import ApiResponse


def _json(body: ApiResponse, status_code: int, headers: dict[str, str] | None = None) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=body.model_dump(mode="json"),
        headers=headers,
    )


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppError)
    async def handle_app_error(_: Request, exc: AppError) -> JSONResponse:
        return _json(
            ApiResponse.fail(code=exc.code, message=exc.message),
            status_code=exc.status_code,
            headers=exc.headers,
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        _: Request, exc: RequestValidationError
    ) -> JSONResponse:
        details = [
            {
                "loc": list(err.get("loc", [])),
                "msg": err.get("msg", ""),
                "type": err.get("type", ""),
            }
            for err in exc.errors()
        ]
        return _json(
            ApiResponse.fail(
                code="VALIDATION_ERROR",
                message="Invalid request payload.",
                details=details,
            ),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_exception(
        _: Request, exc: StarletteHTTPException
    ) -> JSONResponse:
        # Catches FastAPI/Starlette built-ins (404 on unknown route, 405, etc.)
        return _json(
            ApiResponse.fail(code="HTTP_ERROR", message=str(exc.detail)),
            status_code=exc.status_code,
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_error(_: Request, exc: Exception) -> JSONResponse:
        # Last-resort handler. Never leak stack traces to the client.
        return _json(
            ApiResponse.fail(
                code="INTERNAL_ERROR",
                message=GeneralMessages.UNEXPECTED_ERROR,
            ),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )