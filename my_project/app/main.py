from fastapi import FastAPI
from pydantic import BaseModel
from app.crud import router as crud_router
from app.error_handling import router as error_router
from app.database import router as database_conn
from app.auth import router as auth_c
from app.file_upload import router as filee

app = FastAPI()

app.include_router(crud_router)
app.include_router(error_router)
app.include_router(database_conn)
app.include_router(auth_c)
app.include_router(filee)


@app.get("/")
def home():
    return {"this is home routes"}


# query parameters
# @app.get("/users")
# def get_users(name: str = None):
#     return {"Name": name}


# @app.get("/products")
# def get_products(Limit: int = 10):
#     return {"name"}


# handle multiple query params
# @app.get("/products")
# def get_products(name: str = None, price: int = 0):
#     return {"name": name, "price": price}


# request body
# without validation
# @app.post("/create-user")
# def create_user(user: dict):
#     return {"message": "user created successfully", "data": user}


# # pydantic
# class User(BaseModel):
#     name: str
#     age: int


# @app.post("/register-user")
# def register_user(user: User):
#     return {"message": "user created successfully", "data": user}
