"""
OpsDesk API - Main Application Entrypoint
"""

from fastapi import Depends, FastAPI, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

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
    database: str

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

async def health_check(db: AsyncSession = Depends(get_db)) -> HealthResponse:
    """
    Checks API liveness and PostgreSQL database connectivity.
    """
    try:
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return HealthResponse(status="ok", database=db_status)