from fastapi import FastAPI
from routers import assignment
import sys
from os import path

sys.path.append(path.dirname(path.abspath(__file__)))

app = FastAPI()

app.include_router(assignment.router)

@app.get("/")
async def root():
    return {"message": "Hello, this page is e-mart assignment."}
