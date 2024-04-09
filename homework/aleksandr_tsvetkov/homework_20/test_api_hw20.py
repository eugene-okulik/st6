import requests
import pytest
from pydantic import BaseModel, Field


class ObjectDeleteResponse(BaseModel):
    message: str


class DataModel(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class ProductCreation(BaseModel):
    id: str
    name: str
    data: DataModel
    createdAt: str


def test_create_obj():
    payload = {
        "name": "Google Pixel X",
        "data": {
            "year": 2026,
            "price": 1299.99,
            "CPU model": "Tensor G5",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    ProductCreation(**response.json())


def test_get_obj_by_id(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    assert response.json()['id'] == obj_id, 'Object ID don\'t match'


@pytest.mark.critical
@pytest.mark.parametrize('name, price, cpu_model', [
    ('Google Pixel X', 1299.99, 'Tensor G5'),
    ('Google Pixel X', 1300, 'Tensor G6'),
    ('Google Pixel X', 1301.99, 'Tensor G7')
])
def test_put_obj(obj_id, name, price, cpu_model):
    payload = {
        "name": name,
        "data": {
            "year": 2026,
            "price": price,
            "CPU model": cpu_model,
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.json()['data']['price'] == price, 'Object was not updated'


def test_patch_obj(obj_id):
    payload = {
        "data": {
            "price": 1400,
            "Hard disk size": "512 MB"
        }
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    assert response.status_code == 200, 'Status code is not Ok'
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.json()['data']['price'] == 1400, 'Object was not updated'


@pytest.mark.medium
def test_obj_delete(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200, 'Status code is not Ok'
    ObjectDeleteResponse(**response.json())
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404, 'Object was not deleted'
