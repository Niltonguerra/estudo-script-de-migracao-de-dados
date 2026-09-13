# modules/data_migration/migration_router.py
from fastapi import APIRouter

from src.modules.data_migration.routes.migration_router import migration_router

data_migration_router = APIRouter(
  prefix="/data_migration", 
  tags=["Data Migration"]
)

data_migration_router.include_router(migration_router)
