from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()

'''
Declare Cookie parameters¶
Then declare the cookie parameters using the same structure as with Path and Query.

You can define the default value as well as all the extra validation or annotation parameters:
'''

@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    """
    Endpoint to retrieve the advertisement ID from cookies.
    http://127.0.0.1:8000/items/
    
    Args:
        ads_id (str | None): An optional cookie parameter for the advertisement ID. 
        Defaults to None if not set in the cookies.
        
    Returns:
        dict: A dictionary containing the advertisement ID from the cookies.
        {
            "ads_id": "some_id_value"
        }
    """

    return {"ads_id": ads_id}