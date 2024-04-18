import requests
import allure
from tests_API_vkuklin.endpoints.base_endpoint import BaseEndpoint

HEADERS = {
    'Content-type': 'application/json'
}
PAYLOAD = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2024,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}


class CreateObject(BaseEndpoint):
    @allure.step('Send object request')
    def create_new_object(self, payload=None, headers=None):
        headers = headers if headers else HEADERS
        payload = payload if payload else PAYLOAD
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
