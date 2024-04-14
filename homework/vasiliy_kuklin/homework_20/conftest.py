import requests
import pytest


@pytest.fixture()
def start():
    print('\nStart testing')
    yield


@pytest.fixture()
def end():
    print('\nTesting completed')
    yield


@pytest.fixture()
def post_id():
    payload = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "Silicon m4",
            "Hard disk size": "10 TB"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
