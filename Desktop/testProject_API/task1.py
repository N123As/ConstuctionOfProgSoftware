from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    items_db = []

#get
@app.get("/items", response_model=List[Item])
def get_items():
    return items_db

#getid
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item wasnt found")

#post
@app.post("/items", response_model=Item)
def create_item(item: Item):
    if any(existing_item.id == item.id for existing_item in items_db):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    
    item.id = max([i.id for i in items_db], default=0) + 1  # Генеруємо ID
    items_db.append(item)
    return item

#patch
@app.patch("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: Item):
    for item in items_db:
        if item.id == item_id:
            if item_data.name is not None:
                item.name = item_data.name
            if item_data.description is not None:
                item.description = item_data.description
            return item
    raise HTTPException(status_code=404, detail="Item wasnt found")

#delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items_db
    if not any(item.id == item_id for item in items_db):
        raise HTTPException(status_code=404, detail="Item wasnt found")

    items_db = [item for item in items_db if item.id != item_id]
    return {"message": "Item deleted"}

