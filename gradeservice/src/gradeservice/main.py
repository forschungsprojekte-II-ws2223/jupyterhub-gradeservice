from fastapi import FastAPI, UploadFile, HTTPException
import gradeservice.otter as otter
import os

app = FastAPI()

@app.post("/{course_id}/{activity_id}")
async def create_assignment(course_id: int, activity_id: int, file: UploadFile):
    try:
        res = await otter.create_assignment(course_id, activity_id, file)
    except OSError:
        raise HTTPException(status_code=400, detail=f'Activity {course_id}/{activity_id} already exists.')

    return {"message": res}

@app.post("/{course_id}/{activity_id}")
async def get_assignment(course_id: int, activity_id: int):
    return 0
