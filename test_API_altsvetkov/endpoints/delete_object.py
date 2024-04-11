import allure
import requests
from test_API_altsvetkov.endpoints.base_endpoints import BaseEndpoints


class DeleteObject(BaseEndpoints):
    @allure.step('Send DELETE request')
    def delete_object(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()
        self.status_code = self.response.status_code



