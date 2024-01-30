from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None

# Example data
items_db = [
    {"name": "Item 1", "description": "Description 1"},
    {"name": "Item 2", "description": "Description 2"},
]

# Route to list items
@router.get("/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10):
    return items_db[skip : skip + limit]

# Route to retrieve a specific item
@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# Route to create a new item
@router.post("/", response_model=Item)
def create_item(item: Item):
    items_db.append(item.dict())
    return item

# Route to update an existing item
@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    items_db[item_id] = updated_item.dict()
    return updated_item

# Route to delete an item
@router.delete("/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    deleted_item = items_db.pop(item_id)
    return deleted_item
