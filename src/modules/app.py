from fastapi import FastAPI

from src.modules.data_migration.migration_setup import data_migration_router
from src.modules.health.health_router import health_router


def register_routers(app: FastAPI) -> None:
    app.include_router(health_router)
    app.include_router(data_migration_router)
