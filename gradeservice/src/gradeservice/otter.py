import base64
import os
import shutil
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

from fastapi import APIRouter, HTTPException, UploadFile
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .config import settings

router = APIRouter()


# create directory and otter assign
@router.post("/{course_id}/{activity_id}", status_code=HTTP_201_CREATED)
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    path = Path(f"{settings.assignments_path}/{course_id}/{activity_id}")

    file_path = path.joinpath(file.filename)
    if file_path.suffix != ".ipynb":
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"The file {file.filename} is not a .ipynb file.",
        )

    try:
        os.makedirs(path)
    except OSError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Activity {course_id}/{activity_id} already exists.",
        )

    try:
        contents = await file.read()

        with open(file_path, "wb") as fp:
            fp.write(contents)

        try:
            subprocess.run(
                [f"otter assign {file_path} {path}"],
                shell=True,
                capture_output=True,
                check=True,
                text=True,
            )
        except CalledProcessError as e:
            raise HTTPException(status_code=400, detail=f"Failed to create assignment: {e.stderr}")

        with open(path.joinpath("student", file.filename), "rb") as fp:
            s = base64.b64encode(fp.read())
    except (OSError, HTTPException):
        shutil.rmtree(path)
        raise

    return {file.filename: s}


@router.post("/{course_id}/{activity_id}/{student_id}")
async def submit_upload_file(course_id: int, activity_id: int, student_id: int, file: UploadFile):
    path = Path(f"{settings.assignments_path}/{course_id}/{activity_id}")

    if not path.exists():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Activity {course_id}/{activity_id} doesn't exist.",
        )

    submission_path = path.joinpath("submissions", str(student_id))

    if submission_path.exists():
        shutil.rmtree(submission_path)

    os.makedirs(submission_path)

    content = await file.read()

    submission_file_path = submission_path.joinpath(file.filename)

    with open(submission_file_path, mode="wb") as f:
        f.write(content)

    try:
        subprocess.run(
            [
                f"otter grade -p {submission_file_path} -a {path}/autograder/*-autograder_*.zip -o {submission_path} --pdfs -v"
            ],
            shell=True,
            capture_output=True,
            check=True,
            text=True,
        )
    except CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Failed to grade assignment: {e.stderr}")

    with open(f"{submission_path}/final_grades.csv", "r") as f:
        res = f.read()

    pdf = Path(file.filename).with_suffix(".pdf")
    with open(f"{submission_path}/submission_pdfs/{pdf}", "rb") as fp:
        s = base64.b64encode(fp.read())

    return {"result": res, "pdf": s}
