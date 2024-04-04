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


@pytest.fixture(scope='class')
def start_end():
    print("\nStart testing")
    yield
    print("\nTesting completed")
