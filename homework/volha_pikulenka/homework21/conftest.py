import pytest
import requests


@pytest.fixture()
def start_end():
    print('\nStart testing')
    yield
    print('\nEnd testing')


@pytest.fixture()
def obj_id():
    body = {
        "name": "Some title",
        "data": {
            "year": 2018,
            "price": 42,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev//objects", json=body).json()
    obj_id = response['id']
    return obj_id
