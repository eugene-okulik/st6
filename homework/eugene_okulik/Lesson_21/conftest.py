import pytest
import requests


@pytest.fixture()
def post_id():
    payload = {
        "title": "My title",
        "Body": "My publication content",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture()
def start_end():
    print('\nStart test')
    yield
    print('\nEnd test')


@pytest.fixture(scope='session')
def testing_process():
    print('Session fixture called')
    yield
    print('End of session fixture')


@pytest.fixture(scope='class')
def class_process():
    print('Class fixture called')
    yield 'HOHOHO'
    print('End of class fixture')
