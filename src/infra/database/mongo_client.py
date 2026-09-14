# modules/infra/database/mongo_client.py
import os

from motor.motor_asyncio import AsyncIOMotorClient


def get_mongo_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        host=os.getenv("MONGO_HOST", "localhost"),
        port=int(os.getenv("MONGO_PORT", "27017")),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
    )