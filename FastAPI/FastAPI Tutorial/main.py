from enum import Enum

from fastapi import FastAPI
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


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.price:
        item_dict["price"] = int(item_dict["price"] * (10 / 9))
    return {**item_dict}


@app.get("/item/")
async def get_item_detail(start: int = 0, end: int = 0):
    return {"count": end - start + 1}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}
