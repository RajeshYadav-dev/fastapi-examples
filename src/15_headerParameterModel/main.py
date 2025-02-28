from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers: CommonHeaders = Header()):
    """
    Endpoint to retrieve the headers from the request.
    http://127.0.0.1:8000/items/
    Returns:
        dict: A dictionary containing the headers.
    """
    return headers