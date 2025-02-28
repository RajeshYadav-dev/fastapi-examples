from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def root(item_id:int):
  """
  Endpoint to retrieve an item by its ID.

  Args:
    item_id (int): The ID of the item to retrieve.
    http://127.0.0.1:8000/items/123

  Returns:
    dict: A dictionary containing the item ID.
    {
      "item_id:": 123
    }
  """

  return {"item_id:":item_id}


@app.get("/user/me")
async def user_me():
  """
  Endpoint to return a simple message saying "Hello This is Me".
  http://127.0.0.1:8000/user/me
  Returns:
    dict: A dictionary containing the message.
    {
      "message:":"Hello This is Me."
    }
  """
  
  return {"message:":"Hello This is Me."}

# Here this endpoint not going to call because first endpoint will call always
@app.get("/user/{user_id}")
async def user_me(user_id:str):
  """
  Endpoint to retrieve a user by its ID.

  Args:
    user_id (str): The ID of the user to retrieve.
    http://127.0.0.1:8000/user/me

  Returns:
    dict: A dictionary containing the user ID.
    {
      "user_id:": me
    }
  """
  return {"user_id:":user_id}



@app.get("/hello")
async def helloJava():
  """
  Endpoint to return a greeting message.
  http://127.0.0.1:8000/hello
  Returns:
    dict: A dictionary containing the greeting message.
    {
      "Hello:": "Java"
    }
  """

  return {"Hello:":"Java"}



# Here this enpoint will call always first endpoint will be called
@app.get("/hello")
async def helloJava():
  """
  Endpoint to return a greeting message.
  http://127.0.0.1:8000/hello
  Returns:
    dict: A dictionary containing the greeting message.
    {
      "Hello:": "Java"
    }
  """
  return {"Hello:":"Java"}

@app.get("/item/{item_id}/name/{item_name}")
async def root(item_id:int, item_name:str):
  """
  Endpoint to retrieve an item by its ID and name.

  Args:
    item_id (int): The ID of the item to retrieve.
    item_name (str): The name of the item to retrieve.
    http://127.0.0.1:8000/item/123/name/mango
  Returns:
    dict: A dictionary containing the item ID and name.
    {
     "item_id": 123,
     "item_name": "mango"
    }
  """
  return {"item_id":item_id, "item_name":item_name}


from enum import Enum
class ModelName(str, Enum):
  name = "name"
  id = "id"
  city = "city"
  
@app.get("/model/{model_name}")  
async def get_model(model_name:ModelName):
  """
  Endpoint to retrieve a model based on its name.
  http://127.0.0.1:8000/model/name
  Args:
    model_name (str): The name of the model to retrieve.

  Returns:
    dict: A dictionary containing the model name.
    {
      "model_name": "name"
    }
  """
  if model_name == ModelName.name:
    return {"model_name":model_name}
  if model_name == ModelName.id:
    return {"model_name":model_name}
  return {"model_name":model_name}


