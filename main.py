from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Root endpoint that returns a greeting
@app.get("/")
def read_root():
    return {"Hello": "World"}

#GET endpoint that returns item_id and optional query param
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# PUT endpoint that updates an item with JSON data
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item.id, "name": item.name}