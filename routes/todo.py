from fastapi import APIRouter
# Define router
todoRouter = APIRouter()
todoList = []


@todoRouter.get("/todo")
async def get_todo():
    return todoList

@todoRouter.post("/todo")
async def create_todo(todo: dict) -> dict:
    todoList.append(todo)
    return {"message": "Todo created successfully"}