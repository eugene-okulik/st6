import requests
import allure


class BaseEndpoint:
    response = None
    status_code = None
    response_js = None

    @allure.step("Check status code is 200")
    def check_response_is_200(self):
        assert self.status_code == 200

    def check_response_is_404(self):
        assert self.status_code == 404
