import json
import os

import requests
from jsonschema import validate

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'homework19', 'json_schema')


class ObjectRest:
    def __init__(self):
        self.object_data = None
        self.base_url = "https://api.restful-api.dev"
        self.objects_url = self.base_url + "/objects"
        self.id_object_url = self.objects_url + "/{}"

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

    def create_object(self, object_data: dict) -> dict:
        return requests.post(self.objects_url, json=object_data).json()


    def get_object_by_id(self, obj_id: str):

        return requests.get(self.id_object_url.format(obj_id)).json()

    def update_all_object_data(self, object_data: dict, obj_id: str):
        requests.put(self.id_object_url.format(obj_id), json=object_data)

        return self

    def update_object_data(self, object_data: dict, obj_id: str):
        requests.patch(self.id_object_url.format(obj_id), json=object_data)

        return self

    def delete_object(self, obj_id: str):
        requests.delete(self.id_object_url.format(obj_id))

        return self

    @staticmethod
    def get_json_schema(schema_name: str) -> dict:
        with open(path + f'/{schema_name}', 'r') as file:
            schema = json.load(file)

        return schema

    def validate_json(self, json_schema_name: str, response_json: dict) -> None:
        json_schema = self.get_json_schema(json_schema_name)

        validate(instance=response_json, schema=json_schema)
