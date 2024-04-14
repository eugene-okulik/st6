import requests
import allure
from tests_API_oksana.endpoints.base_endopoint import BaseEndpoint
from tests_API_oksana.endpoints.json_shemas import PayloadModel

PAYLOAD = {
    "name": "name",
    "data": {
        "year": 2022,
        "price": 1883,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
    }
}


class CreatePublication(BaseEndpoint):

    @allure.step("Send POST request and validate response")
    def create_new_publication(self, payload=None):
        payload = payload if payload else PAYLOAD
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.status_code = self.response.status_code
        self.response_js = self.response.json()

    @allure.step("Check name is correct")
    def check_name_is(self, name):
        assert self.response_js['name'] == name

    @allure.step("Validate response schema")
    def check_response_json_shema(self):
        PayloadModel(**self.response.json())
