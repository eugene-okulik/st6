import requests
import allure
from tests_API_vkuklin.endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    @allure.step('Delete object')
    def delete(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.status_code = self.response.status_code
