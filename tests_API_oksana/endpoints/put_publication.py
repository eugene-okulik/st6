import allure
from tests_API_oksana.endpoints.base_endopoint import BaseEndpoint
import requests


class PutPublication(BaseEndpoint):

    @allure.step("Prepare payload")
    def put_obj_by_id(self, post_id, payload=None):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_js = self.response.json()

    @allure.step("Send PUT request and validate response")
    def check_name_is(self, name):
        expected_name = str(name) if not isinstance(name, int) else str(name)
        assert self.response_js['name'] == expected_name
