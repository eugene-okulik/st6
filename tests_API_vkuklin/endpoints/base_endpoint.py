import allure


class BaseEndpoint:
    response = None
    status_code = None
    response_json = None
    object_id = None

    @allure.step('Check status code 200')
    def check_response_is_200(self):
        assert self.status_code == 200

    @allure.step('Check status code 400')
    def check_response_is_404(self):
        assert self.status_code == 404
