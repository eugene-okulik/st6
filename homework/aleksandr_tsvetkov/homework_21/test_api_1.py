import requests
import pytest
from pydantic import BaseModel, Field
import allure


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


@allure.tag('Smoke')
@allure.title('Checking the creation of a product object with specified characteristics')
@allure.story('Create product')
@allure.feature('Publication')
def test_create_obj():
    with allure.step('Send POST request'):
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
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Validate JSON Schema'):
        ProductCreation(**response.json())


@allure.tag('Regression')
@allure.title('Product search by id')
@allure.story('Product search by id')
@allure.feature('Publication')
def test_get_obj_by_id(obj_id):
    with allure.step('Send GET request'):
        response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('check that the product id in the response is equal to the product id in the request'):
        assert response.json()['id'] == obj_id, 'Object ID don\'t match'


@allure.tag('Regression')
@allure.title('Complete product change')
@allure.story('Product change')
@allure.feature('Publication')
@pytest.mark.critical
@pytest.mark.parametrize('name, price, cpu_model', [
    ('Google Pixel X', 1299.99, 'Tensor G5'),
    ('Google Pixel X', 1300, 'Tensor G6'),
    ('Google Pixel X', 1301.99, 'Tensor G7')
])
def test_put_obj(obj_id, name, price, cpu_model):
    with allure.step('Send PUT request'):
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
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Check that the changed price in the request is equal to the price in the response'):
        assert response.json()['data']['price'] == price, 'Object was not updated'


@allure.tag('Smoke')
@allure.title('Product edit')
@allure.story('Product edit')
@allure.feature('Publication')
def test_patch_obj(obj_id):
    with allure.step('Send PATCH request'):
        payload = {
            "data": {
                "price": 1400,
                "Hard disk size": "512 MB"
            }
        }
    response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Check that the changed price in the request is equal to the price in the response'):
        assert response.json()['data']['price'] == 1400, 'Object was not updated'


@allure.tag('Regression')
@allure.title('Product delete')
@allure.story('Product delete')
@allure.feature('Publication')
@pytest.mark.medium
def test_obj_delete(obj_id):
    with allure.step('Send DELETE request'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 200'):
        assert response.status_code == 200, 'Status code is not Ok'
    with allure.step('Validate JSON Schema'):
        ObjectDeleteResponse(**response.json())
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    with allure.step('Checking that status code is 404'):
        assert response.status_code == 404, 'Object was not deleted'
