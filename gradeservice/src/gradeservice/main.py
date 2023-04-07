import os

from fastapi import FastAPI, HTTPException, UploadFile

import gradeservice.otter as otter

app = FastAPI()


@app.post("/{course_id}/{activity_id}")
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    try:
        res = await otter.create_assignment(course_id, activity_id, file)
    except OSError:
        raise HTTPException(
            status_code=400, detail=f"Activity {course_id}/{activity_id} already exists."
        )
    os.path.exists(123)
    return {"message": res}


@app.get("/{course_id}/{activity_id}")
async def get_assignment(course_id: int, activity_id: int):
    return 0
