import pytest
import requests


@pytest.fixture(scope='session')
def obj_id():
    payload = {
        "name": "Google Pixel X",
        "data": {
            "year": 2026,
            "price": 1299.99,
            "CPU model": "Tensor G5",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


@pytest.fixture(scope='session', autouse=True)
def start_end_testing():
    print('\nStart testing')
    yield
    print('\nTesting completed')
