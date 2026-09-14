from datetime import datetime
from pydantic import BaseModel, Field


class ProductFilterDTO(BaseModel):
    start_date: datetime = Field(
        default="2024-01-01T00:00:00",
        json_schema_extra={"example": "2024-01-01T00:00:00"},
    )
    end_date: datetime = Field(
        default="2024-12-31T23:59:59",
        json_schema_extra={"example": "2024-12-31T23:59:59"},
    )