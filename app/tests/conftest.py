import pytest
import json


@pytest.fixture
def launches_data():
    with open('fixtures/launches.json') as f:
        data = json.loads(f.read())
    return data


@pytest.fixture
def single_launch_data(launches_data):
    return launches_data[0]
