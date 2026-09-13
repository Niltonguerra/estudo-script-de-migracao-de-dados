from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.modules.app import register_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting app")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Script Provisorio",
    description="script provisório.",
    lifespan=lifespan,
)

register_routers(app)
