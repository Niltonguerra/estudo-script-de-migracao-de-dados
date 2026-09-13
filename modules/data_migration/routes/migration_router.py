# modules/data_migration/routes/migration_router.py
from fastapi import APIRouter

from modules.data_migration.controllers.Migration_controller import Migration_controller

migration_router = APIRouter()


@migration_router.get("/teste/{ticker}")
async def get_quote(ticker: str):
    return await Migration_controller.get_quote(ticker)
