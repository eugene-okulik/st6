import pytest
import requests
from pydantic import BaseModel, Field
import allure


class DataModel(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class Publication(BaseModel):
    name: str
    data: DataModel


class DeleteModel(BaseModel):
    message: str


class TestingAPI:

    @allure.title("Create Publication")
    @allure.description(
        "This test creates of a new publication.")
    @allure.tag("NewPub")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Ekaterina Klimova")
    @allure.issue("Tratata-123")
    @allure.testcase("Test-001")
    @allure.feature('Publication')
    @allure.story('Creation publication')
    @pytest.mark.critical
    def test_post_obj(self):
        data = {
            "name": "MY_Apple MacBook Pro 16100",
            "data": {
                "year": 2022,
                "price": 2849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "12 TB"
            }
        }

        with allure.step('Send post request'):
            response = requests.post("https://api.restful-api.dev/objects", json=data)
        with allure.step('Check that status is 200'):
            assert response.status_code == 200

            assert response.json()['name'] == data['name'], 'Title is invalid'
        Publication(**response.json())

    @allure.feature('Publication')
    @allure.story('Get publication')
    def test_get_by_id(self, post_id):
        print("\nTest is running")

        with allure.step('send get request'):
            response = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        with allure.step('Check that status is 200'):
            assert response.status_code == 200, "Status code is not OK"
        with allure.step('Check id'):
            assert response.json()['id'] == post_id, "Error of ID"

    @allure.feature('Publication')
    @allure.story('Updating publication')
    @pytest.mark.medium
    @pytest.mark.parametrize("year", [2014, 'twenty', 10], ids=['int', 'string', 'int'])
    def test_put_obj(self, post_id, year):
        put_payload = {
            "name": "MY_Apple MacBook Pro 16100",
            "data": {
                "year": year,
                "price": 4849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "120 TB"
            }
        }
        with allure.step('Send put payload'):
            request = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=put_payload)
        with allure.step('Check that year is changed'):
            assert request.json()['data']['year'] == put_payload['data']['year']
        with allure.step('Check that price is changed'):
            assert request.json()['data']['price'] == put_payload['data']['price']
        with allure.step('Check that \'Hard disk size\' is changed'):
            assert request.json()['data']['Hard disk size'] == put_payload['data']['Hard disk size']

    @allure.feature('Publication')
    @allure.story('Updating publication')
    def test_patch_obj(self, post_id):
        patch_payload = {
            "name": "MY_Apple MacBook Pro 1610",
            "data": {
                "price": 5849.99
            }
        }
        with allure.step('Send patch payload'):
            request = requests.patch(f"https://api.restful-api.dev/objects/{post_id}", json=patch_payload)
        with allure.step('Check that price is changed'):
            assert request.json()['data']['price'] == 5849.99
        with allure.step('Check that name is changed'):
            assert request.json()['name'] == "MY_Apple MacBook Pro 1610"

    @allure.feature('Publication')
    @allure.story('Deleting publication')
    def test_delete_obj(self, post_id):
        with allure.step('Send delete request'):
            response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
        with allure.step('Check that publication was deleted'):
            check = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        with allure.step('Check that status is 200'):
            assert response.status_code == 200
        with allure.step('Check response of deleting'):
            assert check.json() == [], "Object wasn't deleted"
        DeleteModel(**response.json())
