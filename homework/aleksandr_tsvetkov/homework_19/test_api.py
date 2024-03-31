import pytest
import requests


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown():
    print('\nStart Testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def obj_id():
    payload = {
        "name": "ASUS ROG GH70",
        "data": {
            "year": 2007,
            "price": 1099.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


def test_create_obj():
    payload = {
        "name": "ASUS ROG GH70",
        "data": {
            "year": 207,
            "price": 1099.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['name'] == payload['name'] and response.json()['data'] == payload['data'], \
        'The values dont match'


def test_get_obj_by_id(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['id'] == obj_id, 'Object ID dont match'


def test_put_obj(obj_id):
    payload = {
        "name": "ASUS ROG GH71",
        "data": {
            "year": 2008,
            "price": 1199.99,
            "CPU model": "Intel Core i3",
            "Hard disk size": "512MB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['name'] == payload['name'] and response.json()['data'] == payload['data'], \
        'The values dont match'


def test_patch_obj(obj_id):
    payload = {
        'data': {
            'year': 2007
        }
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['data'] == payload['data'], 'The values dont match'


def test_delete_obj(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404, 'Object still exists after deletion'
