import allure
from test_UI_vkuklin_PW.pages.base_page import BasePage
from test_UI_vkuklin_PW.pages.locators.locators import CreatePage as loc
from playwright.sync_api import expect


class CreatePage(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Click create button ')
    def click_button_create(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()

    @allure.step('Check required field first name')
    def check_required_field_first_name(self, message):
        field_notice = self.find(loc.ERROR_FIRST_NAME)
        expect(field_notice).to_have_text(message)

    @allure.step('Check required field last name')
    def check_required_field_last_name(self, message):
        field_notice = self.find(loc.ERROR_LAST_NAME)
        expect(field_notice).to_have_text(message)

    @allure.step('Check required field email')
    def check_required_field_email(self, message):
        field_notice = self.find(loc.ERROR_EMAIL_ADDRESS)
        expect(field_notice).to_have_text(message)

    @allure.step('Check required field password')
    def check_required_field_password(self, message):
        field_notice = self.find(loc.ERROR_PASSWORD)
        expect(field_notice).to_have_text(message)

    @allure.step('Check required field confirm password')
    def check_required_field_confirm_passw(self, message):
        field_notice = self.find(loc.ERROR_CONFIRM_PASSWORD)
        expect(field_notice).to_have_text(message)

    @allure.step('insert email in the field')
    def insert_email(self, user_data):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.fill(user_data)
        # email_address.press('Enter')

    @allure.step('check email field')
    def check_email_field(self, message):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        expect(email_address_error).to_have_text(message)

    @allure.step('clear email field')
    def clear_field_email(self):
        current_field = self.find(loc.EMAIL_ADDRESS)
        current_field.press_sequentially('Command' + 'a')
        current_field.press('Backspace')

    @allure.step('filling out the field first name')
    def fill_first_name(self, first_name):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.fill(first_name)

    @allure.step('filling out the field last name')
    def fill_last_name(self, last_name):
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.fill(last_name)

    @allure.step('filling out the field email address')
    def fill_email_address(self, email_address):
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.fill(email_address)

    @allure.step('filling out the field password')
    def fill_password(self, password):
        password_field = self.find(loc.PASSWORD)
        password_field.fill(password)

    @allure.step('filling out the field confirm password')
    def fill_confirm_password(self, confirm_passwd):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.fill(confirm_passwd)

    @allure.step('checking incorrect password')
    def check_incorrect_password(self, message):
        confirm_pass_error = self.find(loc.ERROR_CONFIRM_PASSWORD)
        expect(confirm_pass_error).to_have_text(message)

    @allure.step('check pass equal confirm pass')
    def check_password_valid(self, message):
        success_create_account = self.find(loc.HEADER_MY_ACCOUNT)
        expect(success_create_account).to_have_text(message)
