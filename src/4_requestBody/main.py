from fastapi import FastAPI
from pydantic import BaseModel

# To send data we must use commonly POST or (PUT,DELETE,PAPTH)
# Don't use GET While sending data to server
class Item(BaseModel):
  name :str
  decription : str | None = None
  price : float
  tax : float | None = None


app = FastAPI()

@app.post("/items")
async def create_item(item_data:Item):
  """
  Endpoint to create a new item.
  POST Request
  http://127.0.0.1:8000/items
  Args:
    item_data (Item): The item to be created.
    Request Body:
    {
    "name": "Apple",
    "decription": "Apple Apple very very sweet apple",
    "price": 150.50,
    "tax": 10.23
    }

  Returns:
    Item: The created item.
    Response Body:
    {
    "name": "Apple",
    "decription": "Apple Apple very very sweet apple",
    "price": 150.50,
    "tax": 10.23
    }
  """
  
  return item_data


@app.post("/items-tax")
async def get_items(items_data:Item):
  """
  Endpoint to return an item with the price and the tax.
  POST Request
  http://127.0.0.1:8000/items-tax
  Args:
    items_data (Item): The item to be returned.
    Request Body:
    {
    "name": "Apple",
    "decription": "Apple Apple very very sweet apple",
    "price": 150.50,
    "tax": 10.23
    }

  Returns:
    dict: The item with the price and the tax.
    Response Body:
    {
    "name": "Apple",
    "decription": "Apple Apple very very sweet apple",
    "price": 150.50,
    "tax": 10.23,
    "price_with_tax": 160.73
    }
  """
  dict_item = items_data.model_dump()
  
  if items_data.tax is not None:
    price_with_tax = items_data.price + items_data.tax
    dict_item.update({"price_with_tax":price_with_tax})
  return dict_item