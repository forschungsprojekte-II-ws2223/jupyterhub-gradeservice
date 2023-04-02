from fastapi import FastAPI, File, UploadFile

import os

app = FastAPI()

@app.post("/{course_id}/{activity_id}")
async def create_upload_file(course_id: int, activity_id: int, file: UploadFile):
    folder_path = f'submissions/{course_id}/{activity_id}'
    os.makedirs(folder_path, exist_ok=True)

    filepath = f'{folder_path}/{file.filename}'

    try:
        contents = file.file.read()
        with open(filepath, mode='wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    stream = os.popen(f'otter assign {filepath} {folder_path}/dist')
    output = stream.read()

    return {"message": output}
