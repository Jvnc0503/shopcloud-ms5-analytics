from fastapi import FastAPI
from app.routes.analytics import router as analytics_router

app = FastAPI(title="MS5 Analytics")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "ms5-analytics"
    }

app.include_router(analytics_router)
