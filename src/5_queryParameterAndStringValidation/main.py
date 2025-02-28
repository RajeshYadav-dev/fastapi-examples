from fastapi import FastAPI,Query
from typing import Annotated

app = FastAPI()

# FastApi used to declared additional information and validate your parameter
'''
FastAPI will know that the value of q is not required because of the default value = None.

Having str | None will allow your editor to give you better support and detect errors.
'''

@app.get("/items")
async def get_item(q:str | None=None):
  """
  Endpoint to retrieve a list of items.
   http://127.0.0.1:8000/items
  Args:
    q (str): An optional query parameter to filter the items.
    {"q":"Hello"}
  Returns:
    dict: A dictionary containing the items and the filter query if provided.
    {
    "items": [
    {
      "item_id": 10
    },
    {
      "item_id": 20
    }
           ],
   "q": "Hello"
    }
  """
  
  result = {"items":[{"item_id":10},{"item_id":20}]}
  
  if q:
    result.update({"q":q})
  return result
  

@app.get("/query/")
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
    """
    Endpoint to retrieve a list of items filtered by query string.
    http://127.0.0.1:8000/query/
    Args:
        q (str): An optional query parameter to filter the items.
        {"q":"Hello World"}
    Returns:
        dict: A dictionary containing the items and the filter query if provided.
        {
        "detail": [
         {
          "type": "string_too_short",
          "loc": [
          "query",
          "q"
          ],
          "msg": "String should have at least 3 characters",
        "input": "2",
        "ctx": {
        "min_length": 3
      }
    }
  ]
}
    """

    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results  



