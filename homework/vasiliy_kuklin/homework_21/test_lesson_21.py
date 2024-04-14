import requests
import pytest
from pydantic import BaseModel, Field
import allure


@allure.feature('Object')
@allure.story('Getting object')
def test_get_single_obj(post_id, start):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, 'Status code in not OK'
    with allure.step('Проверка id'):
        assert response.json()['id'] == post_id, 'Id is not correct'


@allure.feature('Object')
@allure.story('Updating object')
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
    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, 'Status code in NOT OK'


@allure.story('Update object')
@allure.title('Обновление объекта')
@pytest.mark.medium
def test_patch_part_update_obj(post_id):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {
        'Content-type': 'application/json'
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload, headers=headers)
    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200, 'Status code in NOT OK'


@allure.story('Create object')
@allure.title('Проверка созданного объекта')
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
    with allure.step('Проверка статус кода 200'):
        assert response.status_code == 200

@allure.title('Проверка удаления объекта')
def test_delete_obj(post_id, end):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    with allure.step('Проверка статус кода 200'):
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
    response = requests.post('https://api.restful-api.dev/objects/', json=payload, headers=headers).json()
    with allure.step('Проверка созданного объекта на соответствие его базововой модели'):
        NewObjWithObj(**response)


class DelKebenyam(BaseModel):
    message: str


@allure.feature('Object')
@allure.story('Delete object')
@allure.title('Проверка удаления объекта')
def test_proverka_del():
    response = requests.delete('https://api.restful-api.dev/objects/').json()
    with allure.step('Проверка удаления объекта согласно базововой модели'):
        DelKebenyam(**response)
