import pytest
import requests
from pydantic import BaseModel, Field


class PostData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class PostResp(BaseModel):
    id: str
    name: str
    createdAt: str
    data: PostData


class DeleteRes(BaseModel):
    message: str


@pytest.mark.critical
def test_create_obj(start_end):
    body = {
        "name": "Test me",
        "data": {
            "year": 2024,
            "price": 11.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev//objects", json=body)
    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['name'] == body['name'], 'Invalid name'
    PostResp(**response.json())


def test_get_obj_lists(start_end):
    response = (requests.get("https://api.restful-api.dev/objects"))
    assert response.status_code == 200, 'Status code is not 200'


def test_get_obj_by_id(start_end, obj_id):
    response = (requests.get(f'https://api.restful-api.dev/objects?id={obj_id}'))
    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()[0]['id'] == obj_id, 'Invalid object id'


@pytest.mark.parametrize('title', ['TEST ME UPD', '', '#435&*()[]/'],
                         ids=['string', 'empty string', 'spec_chars'])
def test_change_obj(start_end, obj_id, title):
    body = {
        "name": title,
        "data": {
            "year": 2020,
            "price": 5000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "gold"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=body)
    assert response.status_code == 200, 'Status code in not 200'
    assert response.json()['id'] == obj_id, 'Invalid object id'
    assert response.json()['name'] == body['name'], 'Invalid name'
    assert response.json()['data']['year'] == body['data']['year'], 'Invalid year'
    assert response.json()['data']['price'] == body['data']['price'], 'Invalid price'
    assert response.json()['data']['color'] == body['data']['color'], 'Invalid color'


def test_change_obj_partially(start_end, obj_id):
    body = {
        "name": "TEST ME UPD again",
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=body)
    assert response.status_code == 200, 'Status code is not 200'
    assert response.json()['id'] == obj_id, 'Invalid object id'
    assert response.json()['name'] == body['name']


@pytest.mark.medium
def test_delete_obj(start_end, obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is not 200'
    assert response.text == '{"message":"Object with id = ' + obj_id + ' has been deleted."}'
    DeleteRes(**response.json())
