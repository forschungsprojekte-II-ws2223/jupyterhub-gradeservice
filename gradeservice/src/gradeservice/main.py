import os
import sys
from pathlib import Path

import gradeservice.otter as otter
from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    assignments_path: Path = Path().cwd()


settings = Settings()

# Check if the assignments path exists and is readable/writeable.
# Defaults to current working dir if ASSIGNMENTS_PATH environment variable is not set.
settings.assignments_path = settings.assignments_path.resolve()

print(f'"{settings.assignments_path}"')
if not settings.assignments_path.is_dir():
    print(f'The directory "{settings.assignments_path}" doesnt exist!')
    sys.exit()

if not os.access(settings.assignments_path, os.W_OK) or not os.access(
    settings.assignments_path, os.R_OK
):
    print(f'No read/write acces in directory "{settings.assignments_path}"!')
    sys.exit()

app = FastAPI()
app.include_router(otter.router)
