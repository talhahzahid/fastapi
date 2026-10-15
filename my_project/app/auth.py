from fastapi import APIRouter, Depends, HTTPException, status, Header
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

router = APIRouter()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"


# create jwt token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


@router.post("/login")
def login(username: str, password: str):
    if username != "admin" or password != "1234":
        raise HTTPException(status_code=401, detail="Invalid username and password")

    token = create_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}


def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = authorization.split(" ", 1)[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


@router.get("/secure")
def secure_data(user=Depends(verify_token)):
    return {"message": "Secure Data Accessed", "user": user}
