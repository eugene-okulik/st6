import allure
from test_UI_vkuklin.pages.base_page import BasePage
from test_UI_vkuklin.pages.locators.locators import CreatePage as loc
from selenium.webdriver.common.keys import Keys
from test_UI_vkuklin.tests.data.user_data import first_name
from test_UI_vkuklin.tests.data.user_data import last_name
from test_UI_vkuklin.tests.data.user_data import email_address
from test_UI_vkuklin.tests.data.user_data import passwd
from test_UI_vkuklin.tests.data.user_data import confirm_passwd


class CreatePage(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Check required fields into')
    def check_click_button_create(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()

    @allure.step('Check required fields results')
    def check_required_fields(self, data_field):
        field_notice = self.find(data_field)
        assert field_notice.text == 'This is a required field.'

    @allure.step('past email into')
    def past_email_into(self, data_field):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(data_field)

    @allure.step('check email field')
    def check_email_field(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('clear email field')
    def clear_field_email(self):
        current_field = self.find(loc.EMAIL_ADDRESS)
        current_field.send_keys(Keys.COMMAND + 'a')
        current_field.send_keys(Keys.BACKSPACE)

    @allure.step('check pass not equal confirm pass')
    def check_password_not_valid(self):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.send_keys(last_name)
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(passwd)
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_passwd)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        confirm_pass_error = self.find(loc.ERROR_CONFIRM_PASSWORD)
        assert confirm_pass_error.text == 'Please enter the same value again.'

    @allure.step('check pass equal confirm pass')
    def check_password_valid(self):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.send_keys(last_name)
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(passwd)
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(passwd)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        success_create_account = self.find(loc.HEADER_MY_ACCOUNT)
        assert success_create_account.text == 'My Account'
