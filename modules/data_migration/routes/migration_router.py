# modules/data_migration/routes/migration_router.py
from fastapi import APIRouter

from modules.data_migration.controllers.Migration_controller import migration_controller

migration_router = APIRouter()


@migration_router.get("/{ticker}")
async def migrate_data(ticker: str):
    return await migration_controller.migrate_data(ticker)
