from typing import Annotated, Literal

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    """
    Endpoint to retrieve a list of items filtered by query string.
    http://127.0.0.1:8000/items/
    Args:
        filter_query (FilterParams): An object containing the filter parameters.
        {
        "limit": 100,
        "offset": 0,
        "order_by": "created_at",
        "tags": []
        }
    Returns:
        dict: A dictionary containing the filter query.
        {
        "limit": 100,
        "offset": 0,
        "order_by": "created_at",
        "tags": []
        }
    """
    return filter_query