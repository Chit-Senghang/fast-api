# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.app import router

app = FastAPI()

# Include the items router under the "/items" path
app.include_router(router, prefix="/items", tags=["items"])

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the main page!"}
