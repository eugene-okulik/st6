import allure
import uuid
from st6.tests_UI_oksana_PW.pages.base import BasePage
from st6.tests_UI_oksana_PW.pages.locators.locators import CreatePageLocators as loc
from playwright.sync_api import expect


class CreateNewAccount(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Enter first name')
    def create_first_name(self, first_name):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.fill(first_name)

    @allure.step('Enter last name')
    def create_last_name(self, last_name):
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.fill(last_name)

    @allure.step('Create a password')
    def create_password(self, password):
        password_field = self.find(loc.PASSWORD)
        password_field.fill(password)

    @allure.step('Confirm the password')
    def confirm_password(self, password):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.fill(password)

    @allure.step('Enter email address')
    def check_email(self, email):
        email_field = self.find(loc.EMAIL)
        email_field.clear()
        email_field.fill(email)

    @allure.step('Complete registration with provided details')
    def complete_registration(self, first_name, last_name, email, password):
        self.create_first_name(first_name)
        self.create_last_name(last_name)
        self.check_email(email)
        self.create_password(password)
        self.confirm_password(password)
        self.submit_registration_form()

    @allure.step('Submit the registration form')
    def submit_registration_form(self):
        submit_button = self.find(loc.SUBMIT_BUTTON)
        submit_button.click()

    @allure.step('Verify redirection to expected page')
    def verify_redirection(self, expected_url):
        expect(self.page).to_have_url(expected_url, timeout=10000)

    @allure.step('Verify email error message')
    def verify_email_error_message(self, error_message):
        error_message_email = self.find(loc.EMAIL_ERROR_MESSAGE)
        expect(error_message_email).to_contain_text(error_message)

    def generate_email(self, domain='example.com'):
        unique_id = uuid.uuid4()
        return f"{unique_id}@{domain}"

    @allure.step('Verify redirection to expected page')
    def verify_redirection_account_create(self, expected_url):
        expect(self.page).to_have_url(expected_url, timeout=10000)
