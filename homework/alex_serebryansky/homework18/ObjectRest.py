import json
import os

import allure
import requests
from jsonschema import validate

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'homework19', 'json_schema')


class ObjectRest:
    def __init__(self):
        self.object_data = None
        self.base_url = "https://api.restful-api.dev"
        self.objects_url = self.base_url + "/objects"
        self.id_object_url = self.objects_url + "/{}"

    @allure.step("Fill data")
    def fill_data(self, name=None, year=None, price=None,
                  cpu_model=None, hdd_size=None, color=None):
        self.object_data = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": cpu_model,
                "Hard disk size": hdd_size,
                "color": color
            }
        }
        return self.object_data

    @allure.step("Create object")
    def create_object(self, object_data: dict):
        return requests.post(self.objects_url, json=object_data).json()

    @allure.step("Get object by ID")
    def get_object_by_id(self, obj_id: str):
        return requests.get(self.id_object_url.format(obj_id)).json()

    @allure.step("Update all object data")
    def update_all_object_data(self, object_data: dict, obj_id: str, need_code: bool = False):
        return requests.put(self.id_object_url.format(obj_id), json=object_data) if need_code \
            else requests.put(self.id_object_url.format(obj_id), json=object_data).json()

    @allure.step("Update different object data")
    def update_object_data(self, object_data: dict, obj_id: str):
        return requests.patch(self.id_object_url.format(obj_id), json=object_data).json()

    @allure.step("Delete object")
    def delete_object(self, obj_id: str):
        return requests.delete(self.id_object_url.format(obj_id)).json()

    @staticmethod
    def get_json_schema(schema_name: str):
        with open(path + f'/{schema_name}', 'r') as file:
            schema = json.load(file)

        return schema

    @allure.step("Validate object JSON data")
    def validate_json(self, json_schema_name: str, response_json: dict):
        json_schema = self.get_json_schema(json_schema_name)

        validate(instance=response_json, schema=json_schema)

    @allure.step("Check values between response and test data")
    def check_values(self, response: dict, object_id: str, test_data: dict):
        return ((((response['id'] == object_id and
                   response['name'] == test_data['name'] and
                   response['data']['price'] == test_data['data']['price']) and
                  response['data']['CPU model'] == test_data['data']['CPU model']) and
                 response['data']['Hard disk size'] == test_data['data']['Hard disk size']) and
                response['data']['color'] == test_data['data']['color'])


def get_checks(local_variables: dict):
    checks = [value for key, value in local_variables.items()
              if key.startswith('check') and key.split('check')[1].isdigit()]
    assert checks, 'Checks list is empty'
    return (lambda _checks: all(check for check in checks))(checks)


