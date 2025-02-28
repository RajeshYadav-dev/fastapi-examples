from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    """
    Endpoint to create a new user.
    POST Request
    http://127.0.0.1:8000/user/
    
    Args:
        user (UserIn): An instance of UserIn containing the user's details.
        
    Returns:
        UserOut: The created user's public information.
    """

    return user