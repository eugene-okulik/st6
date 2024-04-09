import random
import allure
import pytest
import requests


@pytest.fixture()
def post_id():
    data = {
        "name": "MY_Apple MacBook Pro 16100",
        "data": {
            "year": 2022,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "12 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=data)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f"https://api.restful-api.dev/objects/{post_id}")


@pytest.fixture(scope='session')
def start_end():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@allure.feature('Publication')
@allure.story("Creation publication")
def test_post_obj(start_end):
    data = {
        "name": "MY_Apple MacBook Pro 16100",
        "data": {
            "year": 2022,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "12 TB"
        }
    }

    response = requests.post("https://api.restful-api.dev/objects", json=data)
    assert response.status_code == 200
    assert response.json()['name'] == data['name'], 'Title is invalid'


@allure.feature('Publication')
@allure.story("Get publication")
def test_get_by_id(post_id):
    print("\nTest is running")

    response = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
    assert response.status_code == 200, "Status code is not OK"
    assert response.json()['id'] == post_id, "Error of ID"


@allure.feature('Publication')
@allure.story('Updating publication')
def test_put_obj(post_id):
    put_payload = {
        "name": "MY_Apple MacBook Pro 16100",
        "data": {
            "year": 2024,
            "price": 4849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "120 TB"
        }
    }
    request = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=put_payload)
    assert request.json()['data']['year'] == 2024
    assert request.json()['data']['price'] == 4849.99
    assert request.json()['data']['Hard disk size'] == "120 TB"


@allure.feature('Publication')
@allure.story('Updating publication')
def test_patch_obj(post_id):
    patch_payload = {
        "name": "MY_Apple MacBook Pro 1610",
        "data": {
            "price": 5849.99
        }
    }
    request = requests.patch(f"https://api.restful-api.dev/objects/{post_id}", json=patch_payload)
    assert request.json()['data']['price'] == 5849.99
    assert request.json()['name'] == "MY_Apple MacBook Pro 1610"


@allure.feature('Publication')
@allure.story('Deleting publication')
def test_delete_obj(post_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
    check = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
    assert response.status_code == 200
    assert check.json() == [], "Object wasn't deleted"


@allure.feature('Random-test')
@allure.story('Just for comparison')
def test_random():
    assert 1 == random.randrange(0, 5)
