from src.modules.data_migration.repositories.Migration_repository import migration_repository
from src.modules.data_migration.DTOs.ProductFilterSearchDTO import ProductFilterDTO


class MigrationService:
    def __init__(self):
        self.repository = migration_repository

    async def get_service(self, ticker: str):
        return await self.repository.find_by_name(ticker)

    async def create_product(self, name: str, price: float, description: str):
        return await self.repository.create_product(name, price, description)

    async def create_user(self, name: str, email: str):
        return await self.repository.create_user(name, email)
    
    async def get_all_products(self, filters: ProductFilterDTO):
        return await self.repository.get_all_products(filters)

    async def get_all_users(self):
        return await self.repository.get_all_users()


migration_service = MigrationService()