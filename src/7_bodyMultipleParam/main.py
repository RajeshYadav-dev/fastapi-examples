from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    """
    Endpoint to update an item with user information.
    http://127.0.0.1:8000/items/123
    Args:
        item_id (int): The ID of the item to update.
        item (Item): An instance of Item containing the item's details.
        user (User): An instance of User containing the user's details.
        
        {
          "item": {
            "name": "Apple",
            "description": "Sweet Apple",
            "price": 203,
            "tax": 12
          },
          "user": {
            "username": "Rajesh",
            "full_name": "Rajesh Yadav"
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
          },
          "user": {
            "username": "Rajesh",
            "full_name": "Rajesh Yadav"
          }
        }
    """

    results = {"item_id": item_id, "item": item, "user": user}
    return results