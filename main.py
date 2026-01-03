from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q" : q}

# get -> kuch lene ke liye
# post -> kuch dene ke liye
# patch -> jo already pata hai usse badalne ke liye
# delete -> delete karne ke liye
# put -> update karne ke liye

# / signifies the home page ka

# decorators
# error numbers
