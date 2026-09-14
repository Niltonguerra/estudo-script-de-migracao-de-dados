from fastapi import APIRouter

from src.modules.data_migration.controllers.Migration_controller import migration_controller
from src.modules.data_migration.DTOs.ProductFilterSearchDTO import ProductFilterDTO
from datetime import datetime
migration_router = APIRouter()


@migration_router.get("/teste/{ticker}")
async def migrate_data(ticker: str):
    return await migration_controller.get_controller(ticker)


@migration_router.post("/product")
async def create_product(name: str, price: float, description: str):
    return await migration_controller.create_product(name, price, description)


@migration_router.post("/user")
async def create_user(name: str, email: str):
    return await migration_controller.create_user(name, email)


@migration_router.get("/products")
async def get_all_products(start_date: datetime, end_date: datetime):
    filters = ProductFilterDTO(start_date=start_date, end_date=end_date)
    return await migration_controller.get_all_products(filters)


@migration_router.get("/users")
async def get_all_users():
    return await migration_controller.get_all_users()