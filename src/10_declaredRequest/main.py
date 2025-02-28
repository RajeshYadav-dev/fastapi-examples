from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    Endpoint to update an item with the specified item ID.
    http://127.0.0.1:8000/items/123
    Args:
        item_id (int): The ID of the item to update.
        item (Item): An instance of Item containing the item's details.
        
    Returns:
        dict: A dictionary containing the updated item ID and item details.
        {
          "item_id": 123,
          "item": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2
          }
        }
    """

    results = {"item_id": item_id, "item": item}
    return results