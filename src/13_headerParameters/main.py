from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str | None = Header(default=None)):
    """
    Endpoint to retrieve the User-Agent header from the request.
    http://127.0.0.1:8000/items/
    Args:
        user_agent (str | None): The User-Agent header from the request.
    Returns:
        dict: A dictionary containing the User-Agent header.
        	
      Response body

      {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
      }
    """
    return {"User-Agent": user_agent}