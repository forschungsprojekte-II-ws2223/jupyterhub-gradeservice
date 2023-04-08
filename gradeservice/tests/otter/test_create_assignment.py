import os

import pytest


@pytest.fixture
def file():
    return os.path.dirname(__file__)

def test_123(file):
    print(file)
