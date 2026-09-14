from src.modules.data_migration.adapters.Other_system_Adapter import other_system_adapter
from src.modules.data_migration.services.Migration_service import migration_service
from src.modules.data_migration.DTO.ProductFilterSearchDTO import ProductFilterDTO


class MigrationController:
    def __init__(self):
        self.migration_service = migration_service
        self.other_system_adapter = other_system_adapter

    async def get_controller(self, ticker: str):
        return await self.migration_service.get_service(ticker)

    async def create_product(self, name: str, price: float, description: str):
        return await self.migration_service.create_product(name, price, description)

    async def create_user(self, name: str, email: str):
        return await self.migration_service.create_user(name, email)
    
    async def get_all_products(self, filters: ProductFilterDTO):
        products = await self.migration_service.get_all_products(filters)
        respose = await self.other_system_adapter.send_products(products)
        return respose

    async def get_all_users(self):
        return await self.migration_service.get_all_users()


migration_controller = MigrationController()