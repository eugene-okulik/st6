import requests
import allure
from tests_API_vkuklin.endpoints.json_schemas import Object
from tests_API_vkuklin.endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    def get_by_id(self, object_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{object_id}')
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check object id')
    def check_id_is_(self, object_id):
        assert self.response_json['id'] == object_id

    @allure.step('Check json schema')
    def check_response_json_schema(self):
        Object(**self.response_json)
