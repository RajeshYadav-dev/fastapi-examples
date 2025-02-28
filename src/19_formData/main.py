from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str


@app.post("/login/")
async def login(data: FormData = Form()):
    """
    Endpoint to login using form data.

    Args:
        data (FormData): The form data to be passed containing the username and password.

    Returns:
        FormData: The form data that was passed in.
    """
    return data