from fastapi import APIRouter, status
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


@router.get("/active/{todo_id}")
def get_active_todos(todo_id: int, notify: bool = False):
    for todo in todos:
        if todo.id == todo_id:
            if todo.completed:
                return {"data": todo}
            return {"error": "Todo is not completed"}

    return {"error": "Todo not found"}


# response model
class User(BaseModel):
    name: str
    age: int
    password: str


class UserResponse(BaseModel):
    name: str
    age: int


@router.get("/get-users", response_model=UserResponse)
def get_users():
    return {"name": "talha", "age": 21, "password": "123"}


# status code and response custome response & error handling basic


@router.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User Created"}
