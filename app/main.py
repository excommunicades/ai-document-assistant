from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.api.ai import ai_router
from app.api.server_manage import manage_router
from app.services.startup import process_and_store_documents


@asynccontextmanager
async def lifespan(app: FastAPI):
    process_and_store_documents()
    yield

app = FastAPI(
    title="AI Document Helper",
    debug=settings.app_debug,
    lifespan=lifespan
)


app.include_router(ai_router)
app.include_router(manage_router)
