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


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    """
    Very simple and insecure password hasher.

    This function only adds a fixed string to the password, it's not meant to be used in production.
    It's only used here for demonstration purposes.
    """
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    """
    Simulates saving a user to a database with a hashed password.

    Args:
        user_in (UserIn): An instance of UserIn containing the user's details.

    Returns:
        UserInDB: An instance of UserInDB containing the user's details with a hashed password.
    """
#In Pydantic v1 the method was called .dict(), it was deprecated (but still supported) in Pydantic v2, and renamed to .model_dump()
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    """
    Endpoint to create a new user.
    POST Request
    http://127.0.0.1:8000/user/
    Args:
        user_in (UserIn): An instance of UserIn containing the user's details.
        {
          "username": "rajesh@123",
          "password": "rajesh@123",
          "email": "rajesh@example.com",
          "full_name": "Rajesh Yadav"
        }
    Returns:
        UserOut: The created user's public information.
        
        	
        Response body
        {
          "username": "rajesh@123",
          "email": "rajesh@example.com",
          "full_name": "Rajesh Yadav"
        }
    """
    user_saved = fake_save_user(user_in)
    return user_saved
  