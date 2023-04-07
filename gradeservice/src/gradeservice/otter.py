import subprocess
import os

def assign(path: str):
    cmd = f'otter assign {path}/demo.ipynb {path}/dist'
    return subprocess.run([cmd], shell=True, capture_output=True, text=True)

def grade():
    return 0



def handle_new_assignment(course_id: int, activity_id: int):
    try:
        os.makedirs("123")
    except OSError:
        return "exists!s"
