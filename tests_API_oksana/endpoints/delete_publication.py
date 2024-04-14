import requests
import allure
from tests_API_oksana.endpoints.base_endopoint import BaseEndpoint


class DeletePublication(BaseEndpoint):

    @allure.step("Send DELETE request and validate successful deletion")
    def delete_publication(self, post_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
        self.status_code = self.response.status_code

