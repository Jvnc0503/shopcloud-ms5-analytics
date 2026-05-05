from fastapi import FastAPI
from app.routes.analytics import router as analytics_router

app = FastAPI(title="MS5 Analytics")

app.include_router(analytics_router, prefix="/analytics")
