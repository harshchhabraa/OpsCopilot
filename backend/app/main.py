from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.core.config import get_settings
from app.db.session import check_database_connection


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="AI-powered IT operations and incident management platform.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to OpsCopilot",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "opscopilot-api",
    }


@app.get("/health/db")
def database_health():
    try:
        check_database_connection()

        return {
            "status": "healthy",
            "database": "connected",
        }

    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        ) from exc
