from enum import Enum

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: int


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI"}


@app.post("/items/{item_id}")
async def get_item(
    *,
    item_id: int = Path(title="The ID of item to get", ge=0, le=10000),
    q: str | None = Query(default=None, max_length=50),
    item: Item | None = None,
    importance: int = Body()
):
    return {
        "item_id": item_id,
        "q": q,
        "item": item,
        "importance": importance,
    }
