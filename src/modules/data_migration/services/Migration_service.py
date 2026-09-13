# services/Migration_service.py
from src.modules.data_migration.repositories.Migration_repository import (
    migration_repository,
)


class MigrationService:
    def __init__(self):
        self.repository = migration_repository

    async def get_service(self, ticker: str):
        return await self.repository.find_by_ticker(ticker)


migration_service = MigrationService()