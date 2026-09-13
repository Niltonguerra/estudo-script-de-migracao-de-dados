from fastapi import FastAPI

from modules.data_migration.migration_router import data_migration_router
from modules.health.health_router import health_router


def register_routers(app: FastAPI) -> None:
    app.include_router(health_router)
    app.include_router(data_migration_router)
