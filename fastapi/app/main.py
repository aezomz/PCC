from typing import Optional
from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(
                                    None,
                                    min_length=3,
                                    title="Query string",
                                    description="Query string for the items to search in the database that have a good match",
                                    max_length=50, regex="^fixedquery$"
                                    )
                                ):
    result = {"item_id": item_id}
    if item_id == 0:
        result["q"] = "first number"
    if item_id == 322:
        result["q"] = "dont do that"
    return result


@app.post("/items_post/")
async def create_item(item: Item):
    item_dict = item.dict()
    print(item.dict())
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}    


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# pass in function parameter to get query parameters ?skip=0&limit=10
# required query parameters -> don't declare any default value
# optional query paramertes -> declare None as default
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    return fake_items_db[skip : skip + limit]    