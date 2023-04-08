import base64
import os
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

from fastapi import APIRouter, HTTPException, UploadFile

router = APIRouter()

@router.post("/{course_id}/{activity_id}")
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    path = Path(f'assignments/{course_id}/{activity_id}')

    try:
        os.makedirs(path)
    except OSError:
        raise HTTPException(status_code=400, detail=f"Activity {course_id}/{activity_id} already exists.")

    file_path = path.joinpath(file.filename)
    if file_path.suffix != ".ipynb":
        raise HTTPException(status_code=400, detail=f'The file {file.filename} is not a .ipynb file.')

    contents = await file.read()

    with open(file_path, "wb") as fp:
        fp.write(contents)

    try:
        subprocess.run(
            [f"otter assign -v {file_path} {path}"],
            shell=True,
            capture_output=True,
            check=True,
        )
    except CalledProcessError as e:
        raise HTTPException(status_code=400, detail=e.stderr)

    return {"message": "success"}
