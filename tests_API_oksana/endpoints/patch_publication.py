import requests
import allure
from tests_API_oksana.endpoints.base_endopoint import BaseEndpoint


class PatchPublication(BaseEndpoint):
    @allure.step("Send PATCH request")
    def patch_obj_by_id(self, post_id, payload):
        self.response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_js = self.response.json()

    @allure.step("Validate response")
    def validate_patch_response(self, expected_name):
        # assert self.status_code == 200, 'Status code is not OK'
        assert self.response_js['name'] == expected_name, 'The name is not correct'
