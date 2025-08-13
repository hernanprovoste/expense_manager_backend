from fastapi import FastAPI
from app.api.routes import health

app = FastAPI(title="Expense Manager API")

app.include_router(health.router)

@app.get("/info", tags=["Info"])
def app_info():
    return {
        "app_name": "Expense Manager API",
        "version": "0.1.0",
    }