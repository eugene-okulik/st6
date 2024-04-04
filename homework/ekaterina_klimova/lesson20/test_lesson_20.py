import pytest
import requests
from pydantic import BaseModel, Field


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

        response = requests.post("https://api.restful-api.dev/objects", json=data)
        assert response.status_code == 200
        assert response.json()['name'] == data['name'], 'Title is invalid'
        Publication(**response.json())

    def test_get_by_id(self, post_id):
        print("\nTest is running")

        response = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        assert response.status_code == 200, "Status code is not OK"
        assert response.json()['id'] == post_id, "Error of ID"

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
        request = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=put_payload)
        assert request.json()['data']['year'] == put_payload['data']['year']
        assert request.json()['data']['price'] == put_payload['data']['price']
        assert request.json()['data']['Hard disk size'] == put_payload['data']['Hard disk size']

    def test_patch_obj(self, post_id):
        patch_payload = {
            "name": "MY_Apple MacBook Pro 1610",
            "data": {
                "price": 5849.99
            }
        }
        request = requests.patch(f"https://api.restful-api.dev/objects/{post_id}", json=patch_payload)
        assert request.json()['data']['price'] == 5849.99
        assert request.json()['name'] == "MY_Apple MacBook Pro 1610"

    def test_delete_obj(self, post_id):
        response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
        check = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        assert response.status_code == 200
        assert check.json() == [], "Object wasn't deleted"
        DeleteModel(**response.json())
