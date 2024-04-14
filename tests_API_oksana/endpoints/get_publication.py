import requests
import allure
from tests_API_oksana.endpoints.base_endopoint import BaseEndpoint


class GetPublication(BaseEndpoint):

    @allure.step("Send GET request and validate response")
    def get_by_id(self, post_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
        self.status_code = self.response.status_code
        self.response_js = self.response.json()

    def check_id_is_correct(self, post_id):
        assert self.response.json()['id'] == post_id

