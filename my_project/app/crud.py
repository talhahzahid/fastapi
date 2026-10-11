from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


todos = []


class Todo(BaseModel):
    id: int
    name: str
    completed: bool


@router.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "todo created successfully", "data": todo}


@router.get("/todos")
def get_todos():
    return {"message": "fetch all successfully", "data": todos}


@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}


@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        print(index, "index")
        print(todo, "todo")
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Data Updated", "data": updated_todo}
    return {"error": "Todo not found"}


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Data Deleted"}
    return {"error": "Todo not found"}
