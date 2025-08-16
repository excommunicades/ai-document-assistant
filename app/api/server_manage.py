from fastapi import APIRouter

from app.config import settings


manage_router = APIRouter(prefix="/manage", tags=["Server"])


@manage_router.get("/health")
def health_check():
    return {
        "status": "ok",
        "env": settings.app_env,
        "debug": settings.app_debug
    }
