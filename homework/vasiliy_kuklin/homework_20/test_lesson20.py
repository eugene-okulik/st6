import requests
import pytest
from pydantic import BaseModel, Field


def test_get_single_obj(post_id, start):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    assert response.status_code == 200, 'Status code in not OK'
    assert response.json()['id'] == post_id, 'Id is not correct'


@pytest.mark.critical
@pytest.mark.parametrize('year', [1990, "zorro", []], ids=['int', 'string', 'array'])
def test_put_update_obj(post_id, year):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": year,
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


@pytest.mark.medium
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


class ObjectData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithObj(BaseModel):
    id: str
    name: str
    data: ObjectData
    createdAt: str


def test_proverka_post():
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
    response = requests.post('https://api.restful-api.dev/objects/', json=payload, headers=headers).json()
    NewObjWithObj(**response)


class DelKebenyam(BaseModel):
    message: str


def test_proverka_del():
    response = requests.delete('https://api.restful-api.dev/objects/').json()
    DelKebenyam(**response)
