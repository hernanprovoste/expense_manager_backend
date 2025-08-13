from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import health
from app.db.session import create_db_and_tables

# Lifespan manager manage the starts and ends tasks
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_db_and_tables()
    yield
    print("Shutting down...")


app = FastAPI(title="Expense Manager API", lifespan=lifespan)

app.include_router(health.router)

@app.get("/info", tags=["Info"])
def app_info():
    return {
        "app_name": "Expense Manager API",
        "version": "0.1.0",
    }