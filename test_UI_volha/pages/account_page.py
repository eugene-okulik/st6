import allure

from test_UI_volha.pages.base_page import BasePage
from test_UI_volha.pages.locators.locators import AccountPage as loc


class AccountPage(BasePage):
    relative_url = '/customer/account/'

    @allure.step('Check account info has email')
    def check_account_email(self, email):
        account_info = self.find_element(loc.ACCOUNT).get_attribute('innerText')
        assert email in account_info
