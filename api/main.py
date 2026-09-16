from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analytics import router as analytics_router
from api.routes.chat import router as chat_router
from api.routes.anomalies import router as anomalies_router


app = FastAPI(
    title="DataPilot AI",
    description="Intelligent Data Engineering & Analytics Platform",
    version="1.0.0",
)


# Allow React frontend to communicate with FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Analytics routes
app.include_router(
    analytics_router,
    prefix="/analytics",
    tags=["Analytics"],
)


# Anomaly detection routes
app.include_router(
    anomalies_router,
    tags=["Anomaly Detection"],
)


# AI chat routes
app.include_router(
    chat_router,
    tags=["AI Chat"],
)


@app.get("/")
def root():
    return {
        "message": "DataPilot AI API is running"
    }