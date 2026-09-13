# modules/infra/database/mongo_client.py
import os

from pymongo import MongoClient
from pymongo.database import Database


def get_database() -> Database:
    client = MongoClient(
        host=os.getenv("MONGO_HOST", "localhost"),
        port=int(os.getenv("MONGO_PORT", "27017")),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
    )
    return client[os.getenv("MONGO_DB", "admin")]


db = get_database()