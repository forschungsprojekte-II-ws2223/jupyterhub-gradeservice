import subprocess

def assign(path: str):
    cmd = f'otter assign {path}/demo.ipynb {path}/dist'
    return subprocess.run([cmd], shell=True, capture_output=True, text=True)

def grade():
    return 0
