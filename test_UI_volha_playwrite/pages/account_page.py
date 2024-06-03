import allure

from test_UI_volha_playwrite.pages.base_page import BasePage
from playwright.sync_api import expect
from test_UI_volha_playwrite.pages.locators.locators import AccountPage as Loc


class AccountPage(BasePage):
    relative_url = '/customer/account/'

    @allure.step('Check account info has email')
    def check_account_email(self, email):
        account_info = self.find_element(Loc.ACCOUNT)
        expect(account_info).to_contain_text(email)
