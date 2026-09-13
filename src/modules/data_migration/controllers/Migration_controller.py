from modules.data_migration.services.Migration_service import migration_service


class Migration_controller:
    def __init__(self):
        self.migration_service = migration_service

    async def teste(self, ticker: str):
        return "teste"

    async def get_controller(self, ticker: str):  # adiciona o parâmetro
        return await self.migration_service.get_service(ticker)


migration_controller = Migration_controller()
