import base64
import os
import pathlib
import subprocess

from fastapi import UploadFile


async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    path = pathlib.Path("assignments" , course_id, activity_id)
    os.makedirs(path)

    file_path = path.joinpath(file.filename)
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
    await file.close()

    res = subprocess.run(
        [f"otter assign {file_path} {path}"],
        shell=True,
        capture_output=True,
        text=True,
    )

    f = open(f"assignments/{course_id}/{activity_id}/dist/student/demo.ipynb", "r")


def get_assignment(course_id: int, activity_id: int):
    if not os.path.exists(f"assignments/{course_id}/{activity_id}"):
        return 0

    return 0


def grade_assignment():
    return 0
