from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    id: int
    name: str
    description: str | None = Field(default=None, max_length=300)
    price: int
    image: list[Image] | None = None


class Offer(BaseModel):
    name: str
    price: float
    items: list[Item]


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


@app.post("/offers/")
async def offer(offer: Offer):
    return offer


@app.post("/images/")
async def images(images: list[Image]):
    return images
