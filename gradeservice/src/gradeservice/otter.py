import base64
import os
import shutil
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

from fastapi import APIRouter, HTTPException, UploadFile

# from otter.api import grade_submission
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


@router.post("/{course_id}/{activity_id}/{student_id}")
async def submit_upload_file(course_id: int, activity_id: int, student_id: int, file: UploadFile):
    path = Path(f"assignments/{course_id}/{activity_id}")

    if not path.exists():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Activity {course_id}/{activity_id} doesn't exist.",
        )

    submission_path = path.joinpath("submissions", str(student_id))
    os.makedirs(submission_path, exist_ok=True)

    content = await file.read()

    submission_file_path = submission_path.joinpath(file.filename)

    with open(submission_file_path, mode="wb") as f:
        f.write(content)

    try:
        subprocess.run(
            [
                f"otter run -a {path}/autograder/demo-autograder_*.zip {submission_file_path} -o {submission_path}"
            ],
            shell=True,
            capture_output=True,
            check=True,
            text=True,
        )
    except CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Failed to create assignment: {e.stderr}")

    # grade_submission does not produce a file, result can be given back with an response
    #
    # res = grade_submission(
    #     submission_file_path,
    #     list(path.joinpath("autograder").glob("*.zip"))[0],
    # )
    # print(res)

    return {"message": "success"}


# export notebook as pdf for manual grading
@router.get("/export/{course_id}/{activity_id}/{student_id}")
async def get_manuel_grading(course_id: int, activity_id: int, student_id: int):
    path = Path(f"assignments/{course_id}/{activity_id}/submissions/{student_id}")

    if not path.exists():
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Student {course_id}/{activity_id}/{student_id} doesn't exist.",
        )

    try:
        subprocess.run(
            [f"otter export --filtering --pagebreaks {path}/*.ipynb"],
            shell=True,
            capture_output=True,
            check=True,
            text=True,
        )
    except CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Failed to export: {e.stderr}")

    return {"message": "success"}


# Return grades TODO
@router.get("/{course_id}/{activity_id}/{student_id}")
async def get_graded_file(course_id: int, activity_id: int, student_id: int):
    return {"message": "success return grade"}
