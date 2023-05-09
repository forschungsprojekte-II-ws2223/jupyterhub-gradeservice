from fastapi import FastAPI
from pydantic import BaseSettings

import gradeservice.otter as otter


class Settings(BaseSettings):
    assignments_path: str


app = FastAPI()

app.include_router(otter.router)
