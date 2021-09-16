import requests
import pytest

@pytest.fixture
def baseURL():
    return "http://localhost:3000"

def test_a(baseURL):
    plannedDeliveries = []

    url = baseURL + "/deliveries_for_planning?current_state=planned"
    response = requests.get(url)
    assert response.status_code == 200

    for delivery in response.json():
        plannedDeliveries.append(delivery["id"])

    url = baseURL + "/planned_route"
    response = requests.get(url)
    assert response.status_code == 200

    totalDeliveries = response.json()["deliveries"]
    founds = 0

    for delivery in totalDeliveries:
        if delivery["id"] in plannedDeliveries:
            founds += 1

    assert founds == len(plannedDeliveries)

def test_b(baseURL):
    url = baseURL + "/planned_route"
    response = requests.get(url)
    assert response.status_code == 200

    deliveries = response.json()["deliveries"]
    carryingCapacity = response.json()["resource"]["carrying_capacity"]

    weight = 0
    for deliverie in deliveries:
        if deliverie["algorithm_fields"]["type"] == "delivery":
            weight +=  deliverie["algorithm_fields"]["weight"]

    assert weight <= carryingCapacity
