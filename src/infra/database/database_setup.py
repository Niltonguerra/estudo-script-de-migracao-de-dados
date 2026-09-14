# modules/infra/database/database_setup.py
import os

from beanie import init_beanie

from src.infra.database.mongo_client import get_mongo_client
from src.modules.data_migration.schema.product_schema import Product
from src.modules.data_migration.schema.user_schema import User


async def init_database():
    client = get_mongo_client()
    await init_beanie(
        database=client[os.getenv("MONGO_DB", "admin")],
        document_models=[
            Product,
            User
        ],
    )