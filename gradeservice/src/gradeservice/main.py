from fastapi import FastAPI

import gradeservice.otter as otter

app = FastAPI()

app.include_router(otter.router)


@app.get("/")
async def root():
    return {"msg": "Hello World"}
