import allure
from test_UI_vkuklin.pages.base_page import BasePage
from test_UI_vkuklin.pages.locators.locators import CreatePage as loc
from selenium.webdriver.common.keys import Keys
# from st6.test_UI_vkuklin.pages.base_page import BasePage
# from st6.test_UI_vkuklin.pages.locators.locators import CreatePage as loc


class CreatePage(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Click create button ')
    def click_button_create(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()

    @allure.step('Check required field first name')
    def check_required_field_first_name(self):
        field_notice = self.find(loc.ERROR_FIRST_NAME)
        assert field_notice.text == 'This is a required field.'

    @allure.step('Check required field last name')
    def check_required_field_last_name(self):
        field_notice = self.find(loc.ERROR_LAST_NAME)
        assert field_notice.text == 'This is a required field.'

    @allure.step('Check required field email')
    def check_required_field_email(self):
        field_notice = self.find(loc.ERROR_EMAIL_ADDRESS)
        assert field_notice.text == 'This is a required field.'

    @allure.step('Check required field password')
    def check_required_field_password(self):
        field_notice = self.find(loc.ERROR_PASSWORD)
        assert field_notice.text == 'This is a required field.'

    @allure.step('Check required field confirm password')
    def check_required_field_confirm_passw(self):
        field_notice = self.find(loc.ERROR_CONFIRM_PASSWORD)
        assert field_notice.text == 'This is a required field.'

    @allure.step('insert email in the field')
    def insert_email(self, user_data):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(user_data)

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

    @allure.step('filling out the field first name')
    def fill_first_name(self, first_name):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.send_keys(first_name)

    @allure.step('filling out the field last name')
    def fill_last_name(self, last_name):
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.send_keys(last_name)

    @allure.step('filling out the field email address')
    def fill_email_address(self, email_address):
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)

    @allure.step('filling out the field password')
    def fill_password(self, password):
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(password)

    @allure.step('filling out the field confirm password')
    def fill_confirm_password(self, confirm_passwd):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_passwd)

    @allure.step('checking incorrect password')
    def check_incorrect_password(self):
        confirm_pass_error = self.find(loc.ERROR_CONFIRM_PASSWORD)
        assert confirm_pass_error.text == 'Please enter the same value again.'

    @allure.step('check pass equal confirm pass')
    def check_password_valid(self):
        success_create_account = self.find(loc.HEADER_MY_ACCOUNT)
        assert success_create_account.text == 'My Account'
