import requests
import pytest
from pydantic import BaseModel, Field
import allure


class DataModel(BaseModel):
    year: int
    price: int
    cpu_model: str = Field(alias='CPU model')
    disk_size: str = Field(alias='Hard disk size')


class PayloadModel(BaseModel):
    name: str
    data: DataModel


@allure.feature("Create Object")
@allure.story("Post Request to Create an Object")
@allure.title("Test Create Object with POST Request")
def test_create_object():
    with allure.step("Prepare payload"):
        payload = {
            "name": "Apple MacBook 22",
            "data": {
                "year": 2022,
                "price": 1883,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
            }
        }

    with allure.step("Send POST request and validate response"):
        response = requests.post('https://api.restful-api.dev/objects', json=payload)
        assert response.status_code == 200, 'Status code is not OK'
        assert response.json()['name'] == payload['name'], 'The name is not correct'

    with allure.step("Validate response schema"):
        PayloadModel(**response.json())


@allure.feature("Get Object")
@allure.story("Get Request to Retrieve Object by ID")
@allure.title("Test Update Object by ID with PUT Request")
@pytest.mark.critical
def test_get_object_by_id(post_id):
    with allure.step("Send GET request and validate response"):
        response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
        assert response.status_code == 200, 'Status code is not OK'
        assert response.json()['id'] == post_id, 'Id is not correct'


@allure.feature("Update Object")
@allure.story("Put Request to Update an Object by ID")
@pytest.mark.parametrize('name', ['Apple MacBook Pro 16', 88, {'Apple': 'MacBook'}], ids=['string', 'int', 'dict'])
def test_put_object_by_id(name, post_id):
    with allure.step("Prepare payload"):
        payload = {
            "name": "name",
            "data": {
                "year": 2024,
                "price": 1923,
                "CPU model": "Intel Core i11",
                "Hard disk size": "1.1 TB",
            }
        }

    with allure.step("Send PUT request and validate response"):
        response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
        assert response.status_code == 200, 'Status code is not OK'
        assert response.json()['name'] == payload['name'], 'The name is not correct'


@allure.feature("Modify Object")
@allure.story("Patch Request to Modify an Object by ID")
@pytest.mark.medium
def test_patch_object_by_id(post_id):
    with allure.step("Prepare payload for PATCH request"):
        payload = {
            "name": "Samsung"
        }

    with allure.step("Send PATCH request and validate response"):
        response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
        assert response.status_code == 200, 'Status code is not OK'
        assert response.json()['name'] == payload['name'], 'The name is not correct'


class SuccessResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    error: str


@allure.feature("Delete Object")
@allure.story("Delete Request to Remove an Object by ID")
@allure.title("Test Delete Object by ID with DELETE Request")
def test_delete_object_by_id(post_id):
    with allure.step("Send DELETE request and validate successful deletion"):
        response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
        assert response.status_code == 200, 'Status code is not OK'
        assert response.json()['message'], f'Object with id = {post_id} has been deleted.'
        SuccessResponse(**response.json())

    with allure.step("Validate deletion by sending another DELETE request"):
        response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
        assert response.status_code == 404, 'Status code is not good'
        assert response.json()['error'], f"Object with id = {post_id} doesn't exist."
        ErrorResponse(**response.json())
