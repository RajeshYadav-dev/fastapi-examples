from fastapi import FastAPI

app = FastAPI()

fake_db = [{"name":"Rajesh", "age":28}, {"name":"Ramesh", "age":30}, {"name":"Suresh", "age":40}, {"name":"Rakesh", "age":20}]

@app.get("/model/items/")
async def read_items(skip:int=0,limit:int=10):
  """
  Endpoint to retrieve a list of items from the database.
  http://127.0.0.1:8000/model/items/?skip=0&limit=2
  Args:
    skip (int): The number of items to skip at the beginning of the list.
    limit (int): The number of items to return.

  Returns:
    list: A list of items, where each item is a dictionary containing the
      item's name and age.
      
    {
    "name": "Suresh",
    "age": 40
    }
  """
  return fake_db[skip+limit]
