import base64
import os
import subprocess

from fastapi import UploadFile


async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    folder_path = f"assignments/{course_id}/{activity_id}"
    os.makedirs(folder_path)

    contents = await file.read()
    with open(f"{folder_path}/{file.filename}", "wb") as f:
        f.write(contents)

    res = subprocess.run(
        [f"otter assign {folder_path}/{file.filename} {folder_path}/dist"],
        shell=True,
        capture_output=True,
        text=True,
    )

    f = open(f"assignments/{course_id}/{activity_id}/dist/student/demo.ipynb")


def get_assignment(course_id: int, activity_id: int):
    if not os.path.exists(f"assignments/{course_id}/{activity_id}"):
        return 0

    return 0


def grade_assignment():
    return 0
