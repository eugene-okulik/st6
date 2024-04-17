import requests
import allure
from tests_API_eklimova.endpoints.base_endpoint import BaseEndpoint

HEADERS = {
    'Content-type': 'application/json'
}
PATCH_PAYLOAD = {
    "name": "MY_Apple MacBook Pro 1610",
    "data": {
        "price": 5849.99
    }
}


class PatchPublication(BaseEndpoint):

    @allure.feature('Publication')
    @allure.story('Updating publication')
    @allure.step('Send patch payload')
    def send_patch_request(self, post_id, patch_payload=None, headers=None):
        headers = headers if headers else HEADERS
        patch_payload = patch_payload if patch_payload else PATCH_PAYLOAD
        self.response = requests.patch(f"https://api.restful-api.dev/objects/{post_id}", json=patch_payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check that name is changed')
    def check_name_is_changed(self, name):
        assert self.response_json['name'] == name
