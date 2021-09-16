import requests
import pytest

@pytest.fixture
def baseURL():
    return "http://localhost:3000"

def test_get(baseURL):

    url = baseURL + "/planned_route"
    response = requests.get(url)
    assert response.status_code == 200

