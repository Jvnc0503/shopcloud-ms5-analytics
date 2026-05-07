from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.analytics import router as analytics_router

app = FastAPI(title="MS5 Analytics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "ms5-analytics"
    }

app.include_router(analytics_router)
