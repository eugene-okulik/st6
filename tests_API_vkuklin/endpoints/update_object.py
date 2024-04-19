import requests
import allure
from tests_API_vkuklin.endpoints.base_endpoint import BaseEndpoint

year = None

HEADERS = {
    'Content-type': 'application/json'
}
PAYLOAD = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": year,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}


class UpdateObject(BaseEndpoint):

    @allure.step('Updating object request')
    def update_object_single(self, object_id, payload=None, headers=None):
        headers = headers if headers else HEADERS
        payload = payload if payload else PAYLOAD
        self.response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=payload, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check that year is correct')
    def check_year_is_(self, year):
        assert self.response_json['data']['year'] == year
