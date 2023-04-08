import os
from pathlib import Path

import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient

from gradeservice.main import app

client = TestClient(app)

def test_read_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"msg": "Hello World"}

# @pytest.fixture
# def file():
#     file_path = Path(os.path.dirname(__file__), "testdata", "demo.ipynb")

#     with open(file_path) as fp:
#         contents = fp.read()

#     file = UploadFile()
#     return contents

# def test_123( tmp_path):
#     p = Path(".test/123.ipynb")
#     print(p.suffix)
