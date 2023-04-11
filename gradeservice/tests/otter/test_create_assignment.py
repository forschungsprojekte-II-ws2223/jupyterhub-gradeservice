import base64
import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from gradeservice.main import app

client = TestClient(app)


@pytest.fixture
def file_path():
    return Path(os.path.dirname(__file__), "testdata")


def test_success(file_path: Path, tmp_path: Path):
    os.chdir(tmp_path)

    with open(file_path.joinpath("demo.ipynb"), "rb") as fp:
        res = client.post("/1/2", files={"file": ("demo.ipynb", fp)})
        assert res.status_code == 201

        with open(Path("assignments/1/2/student/demo.ipynb"), "rb") as fp:
            assert base64.b64decode(res.json()["demo.ipynb"]) == fp.read()


def test_already_exists(file_path: Path, tmp_path: Path):
    os.chdir(tmp_path)

    with open(file_path.joinpath("demo.ipynb"), "rb") as fp:
        res = client.post("/1/2", files={"file": ("demo.ipynb", fp)})
        assert res.status_code == 201

        res = client.post("/1/2", files={"file": ("demo.ipynb", fp)})
        assert res.status_code == 400
        assert res.json() == {"detail": "Activity 1/2 already exists."}


def test_wrong_filetype(file_path: Path, tmp_path: Path):
    os.chdir(tmp_path)

    with open(file_path.joinpath("demo.ipynb"), "rb") as fp:
        res = client.post("/1/2", files={"file": ("demo.zip", fp)})
        assert res.status_code == 400
        assert res.json() == {"detail": "The file demo.zip is not a .ipynb file."}


def test_fails(file_path: Path, tmp_path: Path):
    os.chdir(tmp_path)

    with open(file_path.joinpath("demo_fails.ipynb"), "rb") as fp:
        res = client.post("/1/2", files={"file": ("demo_fails.ipynb", fp)})
        assert res.status_code == 400
        # TODO: check error message

        assert not os.path.exists("assignments/1/2")


def test_submission_directory(tmp_path: Path):
    os.chdir(tmp_path)

    res = client.post("/student/1/2")
    assert not os.path.exists("assignments/1/2/submissions")
    assert res.status_code == 201
