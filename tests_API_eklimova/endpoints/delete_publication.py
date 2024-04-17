import requests
import allure
from tests_API_eklimova.endpoints.base_endpoint import BaseEndpoint


class DeletePublication(BaseEndpoint):

    @allure.step('Delete publication')
    def delete(self, post_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{post_id}")
        self.status_code = self.response.status_code
