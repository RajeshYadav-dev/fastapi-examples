from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Endpoint to update an item with user information.
    http://127.0.0.1:8000/items/123
    Args:
        item_id (int): The ID of the item to update.
        item (Item): An instance of Item containing the item's details.
        {
          "name": "Apple",
          "description": "Hello Apple",
          "price": 1244,
          "tax": 120,
          "tags": ["sweet","sour"],
          "image": {
            "url": "https://fghjklkjhgghjkl;",
            "name": "Apple"
          }
        }
    Returns:
        dict: A dictionary containing the updated item ID, item details, and user details.
        {
          "item_id": 123,
          "item": {
            "name": "Apple",
            "description": "Hello Apple",
            "price": 1244,
            "tax": 120,
            "tags": [
              "sweet",
              "sour"
            ],
            "image": {
              "url": "https://fghjklkjhgghjkl;",
              "name": "Apple"
            }
          }
        }
    """
    
    results = {"item_id": item_id, "item": item}
    return results