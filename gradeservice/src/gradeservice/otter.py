import base64
import os
import shutil
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

from fastapi import APIRouter, HTTPException, UploadFile
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

router = APIRouter()


@router.post("/{course_id}/{activity_id}", status_code=HTTP_201_CREATED)
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    path = Path(f"assignments/{course_id}/{activity_id}")

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


# Gets the assignment from student
@router.post("/student/{course_id}/{activity_id}")
async def submit_upload_file(course_id: int, activity_id: int, file: UploadFile):
    submission_path = Path(f"assignments/{course_id}/{activity_id}/submissions")
    os.makedirs(submission_path, exist_ok=True)

    file_path = submission_path.joinpath(file.filename)

    content = await file.read()

    try:
        with open(file_path, mode="wb") as f:
            f.write(content)
    except HTTPException:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Could not read file content")
    finally:
        file.file.close()

    return {"message": "success"}


# grades the submissions, needs to be tested
@router.get("/grade/{course_id}/{activity_id}")
async def grade(course_id: int, activity_id: int):
    grading_path = f"assignments/{course_id}/{activity_id}/autograder/demo-autograder"
    files_path = f"assignments/{course_id}/{activity_id}/submissions"

    await subprocess.run(
        [f"otter grade -p {files_path} -a {grading_path}_*.zip --pdfs -vz"],
        shell=True,
        capture_output=True,
        check=True,
    )

    return {"message": "graded"}
