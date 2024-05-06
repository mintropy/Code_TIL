from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field, HttpUrl, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserInput(UserBase):
    password: str


class UserOutput(UserBase):
    pass


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


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/", response_model=list[Item])
async def read_item():
    return [
        Item(name="Foo", price=52),
        Item(name="Baa", price=93),
    ]


@app.post("/offers/")
async def offer(offer: Offer):
    return offer


@app.post("/images/")
async def images(images: list[Image]):
    return images
