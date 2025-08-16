from fastapi import FastAPI

from api.routers.v1 import router as main_router

app = FastAPI()
app.include_router(main_router)