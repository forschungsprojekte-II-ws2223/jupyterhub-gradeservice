import os

from fastapi import FastAPI, HTTPException, UploadFile

import gradeservice.otter as otter

app = FastAPI()


async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    try:
        res = await otter.create_assignment(course_id, activity_id, file)
    except OSError:
        raise HTTPException(
            status_code=400, detail=f"Activity {course_id}/{activity_id} already exists."
        )
    os.path.exists(123)
    return {"message": res}


@app.post("/student/{course_id}/{activity_id}")
async def submit_upload_file(course_id: int, activity_id: int, file: UploadFile):
    submission_path = f"submissions/{course_id}/{activity_id}/submissions"
    os.makedirs(submission_path, exist_ok=True)

    submissionpath = f"{submission_path}/{file.filename}"

    try:
        content = file.file.read()
        with open(submissionpath, mode="wb") as f:
            f.write(content)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": "Submitted"}


@app.get("/grade/{course_id}/{activity_id}")
async def grade(course_id: int, activity_id: int):
    grading_path = f"submissions/{course_id}/{activity_id}/dist/autograder/demo-autograder"
    filepath = f"submissions/{course_id}/{activity_id}/submissions"

    stream = os.popen(f"otter grade -p {filepath} -a {grading_path}_*.zip --pdfs -v")
    stream.close

    return {"message": "graded"}
