import requests
import pytest
import allure
from pydantic import BaseModel
from tests_API_vkuklin.endpoints.create_object import CreateObject
from tests_API_vkuklin.endpoints.delete_object import DeleteObject
from tests_API_vkuklin.endpoints.get_object import GetObject
from tests_API_vkuklin.endpoints.update_object import UpdateObject
from tests_API_vkuklin.endpoints.patch_object import PatchObject
from tests_API_vkuklin.endpoints.json_schemas import Object


@allure.story('Create object')
@allure.title('Check created object')
def test_post_create_obj(create_object):
    payload = {
        "name": "Apple Iphone 13 ProMax",
        "data": {
            "year": 2022,
            "price": 100.99,
            "CPU model": "Celeron",
            "Hard disk size": "512 Gb"
        }
    }
    create_object.create_new_object(payload=payload)
    create_object.check_response_is_200()


@allure.feature('Object')
@allure.story('Getting object')
def test_get_single_obj(get_object, object_id):
    get_object.get_by_id(object_id)
    get_object.check_response_is_200()
    get_object.check_id_is_(object_id)


@allure.feature('Object')
@allure.story('Updating object')
@pytest.mark.critical
@pytest.mark.parametrize('year', [1990, "zorro", []], ids=['int', 'string', 'array'])
def test_put_update_obj(object_id, year, update_object):
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
    update_object.update_object_single(object_id, payload=payload)
    update_object.check_response_is_200()
    update_object.check_year_is_(payload['data']['year'])


@allure.story('Update object')
@allure.title('Обновление объекта')
@pytest.mark.medium
def test_patch_part_update_obj(object_id, patch_object):
    patch_object.patch_object_name(object_id)
    patch_object.check_response_is_200()


def test_delete_obj(object_id, delete_object):
    delete_object.delete(object_id=object_id)
    delete_object.check_response_is_200()


@allure.feature('Object')
@allure.story('Create object')
@allure.title('Проверка созданного объекта')
@pytest.mark.smoke
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
    response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers).json()
    with allure.step('Проверка созданного объекта на соответствие его базововой модели'):
        Object(**response)


class DelKebenyam(BaseModel):
    message: str


@allure.feature('Object')
@allure.story('Delete object')
@allure.title('Проверка удаления объекта')
def test_proverka_del(object_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}').json()
    with allure.step('Проверка удаления объекта согласно базововой модели'):
        DelKebenyam(**response)
