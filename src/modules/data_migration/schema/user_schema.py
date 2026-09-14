from datetime import datetime

from beanie import Document
from pydantic import EmailStr


class User(Document):
    name: str
    email: EmailStr
    created_at: datetime = datetime.now()

    class Settings:
        name = "users"