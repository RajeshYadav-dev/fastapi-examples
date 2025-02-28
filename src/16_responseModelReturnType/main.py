from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    """
    Endpoint to create a new item.
    POST Request
    http://127.0.0.1:8000/items/
    
    Args:
        item (Item): An instance of Item containing the item's details.
        
    Returns:
        Item: The created item.
        
        	
        Response body
        [
          {
            "name": "Portal Gun",
            "description": null,
            "price": 42,
            "tax": null,
            "tags": []
          },
          {
            "name": "Plumbus",
            "description": null,
            "price": 32,
            "tax": null,
            "tags": []
          }
        ]
    """

    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    """
    Endpoint to retrieve a list of items.
    GET Request
    http://127.0.0.1:8000/items/
    
    {
      "name": "Apple",
      "description": "Sweet apple",
      "price": 1223,
      "tax": 12,
      "tags": ["apple","banana"]
    }

    Returns:
        list[Item]: A list of Item containing the item's details.
        Response body
        {
          "name": "Apple",
          "description": "Sweet apple",
          "price": 1223,
          "tax": 12,
          "tags": [
            "apple",
            "banana"
          ]
        }
    """
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]
    
    