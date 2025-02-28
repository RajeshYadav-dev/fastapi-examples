from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """
    Endpoint to update an item with user information.
    http://127.0.0.1:8000/items/123
    Args:
        item_id (int): The ID of the item to update.
        item (Item): An instance of Item containing the item's details.
          {
            "item": {
              "name": "Apple",
              "description": "Sweet Apple",
              "price": 123,
              "tax": 10
            }
          }
        

    Returns:
        dict: A dictionary containing the updated item ID, item details, and user details.
        {
          "item_id": 123,
          "item": {
            "name": "Apple",
            "description": "Sweet Apple",
            "price": 203,
            "tax": 12
          }
        }
    """
    results = {"item_id": item_id, "item": item}
    return results