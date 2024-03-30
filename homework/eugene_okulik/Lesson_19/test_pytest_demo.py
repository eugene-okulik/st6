import pytest
import requests
import sys


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


def test_create_publication(start_end):
    payload = {
        "title": "My title",
        "Body": "My publication content",
        "userId": 1
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
    assert response.status_code == 201, 'Status code is not Ok'
    assert response.json()['title'] == payload['title'], 'Invalid title'


def test_get_by_id(post_id, start_end):
    print('\nTest is running')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['id'] == post_id, 'Id is not correct'


class TestOne:
    @pytest.mark.skip('Bug #136')
    def test_one(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    @pytest.mark.skipif(sys.platform == 'linux', reason='Not working on Linux')
    def test_two(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1

    def test_three(self, class_process):
        assert class_process == 'HOHOHO'
        assert 1 == 1


def test_four():
    assert 1 == 1
