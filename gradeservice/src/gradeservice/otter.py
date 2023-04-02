import subprocess

def run_assign():
    result = subprocess.run(["ls"], shell=True, capture_output=True, text=True)
