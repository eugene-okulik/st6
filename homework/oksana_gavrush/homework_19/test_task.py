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


def test_create_object():
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
    assert response.status_code == 200, 'Status code is not good'
    assert response.json()['name'] == payload['name'], 'The name is not correct'


def test_get_object_by_id(post_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code is not good'
    assert response.json()['id'] == post_id, 'Id is not correct'


def test_put_object_by_id(post_id):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 1923,
            "CPU model": "Intel Core i11",
            "Hard disk size": "1.1 TB",
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
    assert response.status_code == 200, 'Status code is not good'
    assert response.json()['name'] == payload['name'], 'The name is not correct'


def test_patch_object_by_id(post_id):
    payload = {
        "name": "Samsung"
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
    assert response.status_code == 200, 'Status code is not good'
    assert response.json()['name'] == payload['name'], 'The name is not correct'


def test_delete_object_by_id(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code is not good'
    assert response.json()['message'], f'Object with id = {post_id} has been deleted.'
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 404, 'Status code is not good'
    assert response.json()['error'], f"Object with id = {post_id} doesn't exist."
