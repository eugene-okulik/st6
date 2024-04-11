import requests
import pytest
from pydantic import BaseModel, Field


class DataModel(BaseModel):
    year: int
    price: int
    cpu_model: str = Field(alias='CPU model')
    disk_size: str = Field(alias='Hard disk size')


class PayloadModel(BaseModel):
    name: str
    data: DataModel


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
    assert response.status_code == 200, 'Status code is not OK'
    assert response.json()['name'] == payload['name'], 'The name is not correct'

    PayloadModel(**response.json())


@pytest.mark.critical
def test_get_object_by_id(post_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code is not OK'
    assert response.json()['id'] == post_id, 'Id is not correct'


@pytest.mark.parametrize('name', ['Apple MacBook Pro 16', 88, {'Apple': 'MacBook'}], ids=['string', 'int', 'dict'])
def test_put_object_by_id(name, post_id):
    payload = {
        "name": "name",
        "data": {
            "year": 2024,
            "price": 1923,
            "CPU model": "Intel Core i11",
            "Hard disk size": "1.1 TB",
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
    assert response.status_code == 200, 'Status code is not OK'
    assert response.json()['name'] == payload['name'], 'The name is not correct'


@pytest.mark.medium
def test_patch_object_by_id(post_id):
    payload = {
        "name": "Samsung"
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
    assert response.status_code == 200, 'Status code is not OK'
    assert response.json()['name'] == payload['name'], 'The name is not correct'


class SuccessResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    error: str


def test_delete_object_by_id(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code is not OK'
    assert response.json()['message'], f'Object with id = {post_id} has been deleted.'

    SuccessResponse(**response.json())

    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 404, 'Status code is not good'
    assert response.json()['error'], f"Object with id = {post_id} doesn't exist."

    ErrorResponse(**response.json())
