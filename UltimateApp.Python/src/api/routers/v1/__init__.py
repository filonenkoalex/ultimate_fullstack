from fastapi import APIRouter

from shared.utils.module import ModuleUtility

# Initialize the main router
router = APIRouter(prefix="/v1")


# Get all routers and register them
routers: list[APIRouter] = ModuleUtility.get(APIRouter, "api.routers.v1", "router")
for r in routers:
    router.include_router(r)
