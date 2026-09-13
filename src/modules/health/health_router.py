from fastapi import APIRouter

health_router: APIRouter = APIRouter(tags=["Health"])


@health_router.get("/health")
async def health():
    return {"status": "ok", "service": "script-provisorio"}