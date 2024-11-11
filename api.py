from fastapi import FastAPI
from routes.todo import todoRouter
import sys

app = FastAPI()
print(sys.version)
# Routes
app.include_router(todoRouter)

@app.get("/")
async def home() -> dict:
    return {"message": "Hello World"}