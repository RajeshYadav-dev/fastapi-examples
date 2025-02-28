from datetime import datetime, time, timedelta
from uuid import UUID
from pydantic import BaseModel

from fastapi import Body, FastAPI

app = FastAPI()

class UserModel(BaseModel):
  item_id: UUID
  start_datetime: datetime 
  end_datetime: datetime 
  process_after: timedelta
  repeat_at: time | None 


@app.put("/items/{item_id}")
async def read_items(user_data:UserModel):
    """
    Endpoint to retrieve an item by its ID with start_process and duration.
    http://127.0.0.1:8000/items
    Args:
        user_data (UserModel): The user data to be retrieved.
         Request Body:
        {
          "item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "start_datetime": "2025-02-28T07:54:16.130Z",
          "end_datetime": "2025-02-28T07:54:16.130Z",
          "process_after": "P3D",
          "repeat_at": "07:54:16.130Z"
        }
        
        
    Returns:
        dict: A dictionary containing the start_process and duration.
        {
          "item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "start_datetime": "2025-02-28T07:54:16.130000+00:00",
          "end_datetime": "2025-02-28T07:54:16.130000+00:00",
          "process_after": 259200,
          "repeat_at": "07:54:16.130000+00:00",
          "start_process": "2025-03-03T07:54:16.130000+00:00",
          "duration": -259200
        }
    """
    start_process = user_data.start_datetime + user_data.process_after
    duration = user_data.end_datetime - start_process
    
    user_dict = user_data.model_dump()
    user_dict.update({"start_process": start_process,"duration": duration})
    return user_dict
  
'''
Other data types
Here are some of the additional data types you can use:

UUID:
A standard "Universally Unique Identifier", common as an ID in many databases and systems.
In requests and responses will be represented as a str.
datetime.datetime:
A Python datetime.datetime.
In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15T15:53:00+05:00.
datetime.date:
Python datetime.date.
In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15.
datetime.time:
A Python datetime.time.
In requests and responses will be represented as a str in ISO 8601 format, like: 14:23:55.003.
datetime.timedelta:
A Python datetime.timedelta.
In requests and responses will be represented as a float of total seconds.
Pydantic also allows representing it as a "ISO 8601 time diff encoding", see the docs for more info.
frozenset:
In requests and responses, treated the same as a set:
In requests, a list will be read, eliminating duplicates and converting it to a set.
In responses, the set will be converted to a list.
The generated schema will specify that the set values are unique (using JSON Schema's uniqueItems).
bytes:
Standard Python bytes.
In requests and responses will be treated as str.
The generated schema will specify that it's a str with binary "format".
Decimal:
Standard Python Decimal.
In requests and responses, handled the same as a float.
  '''