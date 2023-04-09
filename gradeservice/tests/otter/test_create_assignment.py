from fastapi.testclient import TestClient

from gradeservice.main import app

client = TestClient(app)


def test_read_main():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"msg": "Hello World"}
