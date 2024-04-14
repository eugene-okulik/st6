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


def test_get_single_obj(post_id, start):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code in not OK'
    assert response.json()['id'] == post_id, 'Id is not correct'


def test_put_update_obj(post_id):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2017,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=payload, headers=headers)
    assert response.status_code == 200, 'Status code in NOT OK'


def test_patch_part_update_obj(post_id):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload, headers=headers)
    assert response.status_code == 200, 'Status code in NOT OK'


def test_post_create_obj():
    payload = {
        "name": "Apple Iphone 13 ProMax",
        "data": {
            "year": 2022,
            "price": 100.99,
            "CPU model": "Seleron",
            "Hard disk size": "512 Gb"
        }
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers)
    assert response.status_code == 200


def test_delete_obj(post_id, end):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code in NOT OK'
