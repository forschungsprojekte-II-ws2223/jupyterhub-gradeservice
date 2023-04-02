import gradeservice.otter as otter
import os

def test_something():
    res = otter.assign(f'{os.path.dirname(__file__)}/testdata')
    assert(res.returncode == 0)
