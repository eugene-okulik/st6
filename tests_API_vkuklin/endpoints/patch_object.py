import requests
import allure
from tests_API_vkuklin.endpoints.base_endpoint import BaseEndpoint

PAYLOAD = {
    "name": "Cucumber MacBook Pro 16 (Updated Name)"
}
HEADERS = {
    'Content-type': 'application/json'
}


class PatchObject(BaseEndpoint):

    @allure.step('Patching object name request')
    def patch_object_name(self, object_id, payload=None, headers=None):
        headers = headers if headers else HEADERS
        payload = payload if payload else PAYLOAD
        self.response = requests.patch(f'https://api.restful-api.dev/objects/{object_id}', json=payload,
                                       headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
