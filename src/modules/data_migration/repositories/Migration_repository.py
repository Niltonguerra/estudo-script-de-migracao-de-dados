from src.infra.database.mongo_client import db


class MigrationRepository:
    def __init__(self):
        self.collection = db["minha_colecao"]

    async def find_by_ticker(self, ticker: str):
        return self.collection.find_one({"ticker": ticker})


migration_repository = MigrationRepository()