import requests
import pytest
from datetime import datetime

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

def test_c(baseURL):
    url = baseURL + "/planned_route"
    response = requests.get(url)
    assert response.status_code == 200

    deliveries = response.json()["deliveries"]
    minDate = datetime.strptime(response.json()["route_min_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    maxDate = datetime.strptime(response.json()["route_max_time"], "%Y-%m-%dT%H:%M:%S.%fZ") 

    for deliverie in deliveries:
        if deliverie["algorithm_fields"]["type"] == "delivery":
            etaDate = datetime.strptime(ç, "%Y-%m-%dT%H:%M:%S.%fZ")
            assert minDate <= etaDate <= maxDate  


def test_d(baseURL):
    url = baseURL + "/planned_route"
    response = requests.get(url)
    assert response.status_code == 200

    deliveries = response.json()["deliveries"]
    for deliverie in deliveries:
        
        etaDate = datetime.strptime(deliverie["algorithm_fields"]["eta"], "%Y-%m-%dT%H:%M:%S.%fZ")
        minDate = datetime.strptime(deliverie["min_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
        maxDate = datetime.strptime(deliverie["max_time"], "%Y-%m-%dT%H:%M:%S.%fZ") 
        
        assert minDate <= etaDate <= maxDate   
            