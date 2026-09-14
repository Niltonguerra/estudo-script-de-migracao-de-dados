from beanie import Document
from datetime import datetime


class Product(Document):
    name: str
    price: float
    description: str
    created_at: datetime = datetime.now()

    class Settings:
        name = "products"