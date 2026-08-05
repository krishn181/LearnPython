from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    age: int

items = {}

@app.post("/item")
def create_data(item: Item ):
    item_id = len(items) + 1
    items[item_id] = item.model_dump()

    return {
        "id": item_id,  
        "item": items[item_id]
    }

@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id in items:
        return items
    return {"message": "Item not found"}

@app.put("/update/{item_id}")
def put_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item.model_dump()
        return {"message": "Item updated successfully"}

    return {"message": "Item not found"}

@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        items.pop(item_id)
        return {"message": "Item deleted successfully"}

    return {"message": "Item not found"}