import os
import subprocess
from pathlib import Path
from subprocess import CalledProcessError

from fastapi import APIRouter, HTTPException, UploadFile
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

router = APIRouter()


@router.post("/{course_id}/{activity_id}", status_code=HTTP_201_CREATED)
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    path = Path(f"assignments/{course_id}/{activity_id}")

    try:
        os.makedirs(path)
    except OSError:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"Activity {course_id}/{activity_id} already exists.",
        )

    file_path = path.joinpath(file.filename)
    if file_path.suffix != ".ipynb":
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=f"The file {file.filename} is not a .ipynb file.",
        )

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


# Gets the assignment from student
@router.post("/student/{course_id}/{activity_id}")
async def submit_upload_file(course_id: int, activity_id: int, file: UploadFile):
    submission_path = f"assignment/{course_id}/{activity_id}/submissions"
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
    grading_path = f"submissions/{course_id}/{activity_id}/dist/autograder/demo-autograder"
    files_path = f"submissions/{course_id}/{activity_id}/submissions"

    stream = os.popen(f"otter grade -p {files_path} -a {grading_path}_*.zip --pdfs -v")
    stream.close

    return {"message": "graded"}
