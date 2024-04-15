import requests
import allure
from tests_API_eklimova.endpoints.json_schemas import Publications
from tests_API_eklimova.endpoints.base_endpoint import BaseEndpoint


class GetPublication(BaseEndpoint):

    @allure.step('send get request')
    def get_by_id(self, post_id):
        self.response = requests.get(f"https://api.restful-api.dev/objects?id={post_id}")
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check id')
    def check_that_id_is(self, post_id):
        assert self.response_json['id'] == post_id

    @allure.step('Check json schema')
    def check_response_json_schema(self):
        Publications(**self.response_json)
