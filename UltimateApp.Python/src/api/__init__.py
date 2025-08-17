from fastapi import FastAPI

from api.routers import router as aggregated_router

app = FastAPI()
app.include_router(aggregated_router)
