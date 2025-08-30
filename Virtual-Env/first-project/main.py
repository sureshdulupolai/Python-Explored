# uv run uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello To My First project"}
