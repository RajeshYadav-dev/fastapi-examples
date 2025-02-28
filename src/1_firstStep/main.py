from fastapi import FastAPI


app  = FastAPI()

@app.get("/")
async def root():
  """
  Simple root endpoint that returns a message of 'Hello World'.

  Returns:
    dict: A dictionary containing a message.
  """
  return {"message": "Hello World"}
