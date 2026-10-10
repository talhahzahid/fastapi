from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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
