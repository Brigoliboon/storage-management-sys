from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from user import user_info
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

items= {1:Item(name='okay', price=2, is_offer=True)}
@app.post("/")
def read_root():
    return {"Hello": "World"}
@app.get("/{auth_key}/items/{item_id}")
def read_item(item_id: int, auth_key: str) -> Item:
    if auth_key not in user_info:
        raise HTTPException(status_code=401, detail='Invalid API key.', headers=None)
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found', headers=None)
    return items[item_id]
@app.put("/update/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
