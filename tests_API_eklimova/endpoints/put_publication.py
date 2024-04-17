import requests
import allure
from tests_API_eklimova.endpoints.base_endpoint import BaseEndpoint

HEADERS = {
    'Content-type': 'application/json'
}
PUT_PAYLOAD = {
    "name": "MY_Apple MacBook Pro 16100",
    "data": {
        "year": 2014,
        "price": 4849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "120 TB"
    }
}


class PutPublication(BaseEndpoint):

    @allure.step('Send put request')
    def send_put_request(self, post_id, put_payload=None, headers=None):
        headers = headers if headers else HEADERS
        put_payload = put_payload if put_payload else PUT_PAYLOAD
        self.response = requests.put(f"https://api.restful-api.dev/objects/{post_id}", json=put_payload,
                                     headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check that year is changed')
    def check_year_is_changed(self, year):
        assert self.response_json['data']['year'] == year

    @allure.step('Check that \'Hard disk size\' is changed')
    def check_hard_disk_is_changed(self, disksize):
        assert self.response_json['data']['Hard disk size'] == disksize
