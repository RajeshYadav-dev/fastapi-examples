from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    """
    Endpoint for user login using form data.

    Args:
        username (str): The username submitted via form data.
        password (str): The password submitted via form data.

    Returns:
        dict: A dictionary containing the submitted username.
    """

    return {"username": username,"password":password}