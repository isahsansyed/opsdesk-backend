from fastapi import Depends, FastAPI, status
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.auth_router import router as auth_router
from app.core.error_handlers import register_exception_handlers
from app.db.session import get_db
from app.users.users_router import router as users_router

app = FastAPI(
    title="OpsDesk API",
    description="Production-Grade Real-Time Support & Incident Management Backend",
    version="0.1.0",
)

register_exception_handlers(app)
app.include_router(auth_router)
app.include_router(users_router)


class HealthResponse(BaseModel):
    status: str
    database: str


@app.get("/", tags=["meta"])
async def root():
    return {"message": "OpsDesk API is running"}


@app.get("/health", response_model=HealthResponse, status_code=status.HTTP_200_OK)
async def health_check(db: AsyncSession = Depends(get_db)) -> HealthResponse:
    try:
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {e}"
    return HealthResponse(status="ok", database=db_status)