"""
OpsDesk API - Main Application Entrypoint
"""

from starlette.types import Message
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
    title="OpsDesk API",
    description="Production-Grade Real-Time Support & Incident Management Backend",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class RootResponse(BaseModel):
    message: str

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/",
response_model=RootResponse,
status_code=status.HTTP_200_OK,
tags=["Root"],
summary="API Root Status",
)
async def read_root() -> RootResponse:
    """
    Root endpoint verifying server availability.
    """
    return RootResponse(message="OpsDesk API is running!")

@app.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    summary="Application Healthcheck",
    )

async def health_check() -> HealthResponse:
    """
    Liveness check used by container orchestrators and monitoring tools.
    """
    return HealthResponse(status="ok", version="0.1.0")