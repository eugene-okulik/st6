import requests
import pytest


@pytest.fixture(scope='session', autouse=True)
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def post_id():
    payload = {
        "name": "Apple MacBook 22",
        "data": {
            "year": 2022,
            "price": 1883,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    post_id = response.json()['id']

    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
