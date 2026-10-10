from fastapi import FastAPI

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
@app.get("/products")
def get_products(name: str = None, price: int = 0):
    return {"name": name, "price": price}
