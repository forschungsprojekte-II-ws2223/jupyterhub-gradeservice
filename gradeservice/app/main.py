from typing import Union

from fastapi import FastAPI

import os

app = FastAPI()


@app.get("/")
async def read_root():
    stream = os.popen('otter --version')
    output = stream.read()
    return {"Hello": "World",
            "ooutput": output,
            }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
