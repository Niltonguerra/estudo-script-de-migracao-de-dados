import os
from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI

from src.modules.app import register_routers
from src.infra.database.database_setup import init_database
from src.infra.exceptions.http_exception_handler import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    print("Starting app")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Script Provisorio",
    description="script provisório.",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

register_routers(app)
register_exception_handlers(app)
