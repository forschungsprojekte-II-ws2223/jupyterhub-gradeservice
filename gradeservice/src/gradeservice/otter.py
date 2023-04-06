import subprocess


def assign(file_path: str, folder_path):
    cmd = f"otter assign {file_path}/demo.ipynb {folder_path}/dist"
    return subprocess.run([cmd], shell=True, capture_output=True, text=True)


def grade(submission_path: str, autograder_path: str):
    cmd = f"otter grade -p {submission_path} -a {autograder_path}_*.zip --pdfs -v"
    return subprocess.run([cmd], shell=True, capture_output=True, text=True)
