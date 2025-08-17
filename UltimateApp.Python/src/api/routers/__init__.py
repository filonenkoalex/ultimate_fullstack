from fastapi import APIRouter

from shared.utils.module import ModuleUtility

router = APIRouter()

# Get all routers and register them using the new generic utility
routers: list[APIRouter] = ModuleUtility.get(APIRouter, "api.routers", "router")
for r in routers:
    router.include_router(r)
