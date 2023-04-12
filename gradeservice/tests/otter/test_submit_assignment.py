def test_submission_directory(tmp_path: Path):
    os.chdir(tmp_path)

    res = client.post("/student/1/2")
    assert not os.path.exists("assignments/1/2/submissions")
    assert res.status_code == 201
