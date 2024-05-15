import allure
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from st6.tests_UI_oksana_selenium.pages.base import BasePage
from st6.tests_UI_oksana_selenium.pages.locators.locators import CreatePageLocators as loc


class CreateNewAccount(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Enter first name')
    def create_first_name(self):
        first_name = self.find(loc.FIRST_NAME)
        first_name.send_keys('John')

    @allure.step('Enter last name')
    def create_last_name(self):
        last_name = self.find(loc.LAST_NAME)
        last_name.send_keys('Smith')

    @allure.step('Create a password')
    def create_password(self, password):
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(password)

    @allure.step('Confirm the password')
    def confirm_password(self, password):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)

    @allure.step('Enter email address')
    def check_email(self, email):
        email_field = self.find(loc.EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step('Complete registration with provided details')
    def complete_registration(self, email, password):
        self.create_first_name()
        self.create_last_name()
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
        WebDriverWait(self.driver, 10).until(ec.url_to_be(expected_url))
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Redirection failed. Expected {expected_url}, got {current_url}"

    @allure.step('Verify email error message')
    def verify_email_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        error_message_email = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#email_address-error')))
        expected_error_text = 'Please enter a valid email address'
        actual_error_text = error_message_email.text
        assert expected_error_text in actual_error_text, \
            f"Expected error message not found. Actual message: {actual_error_text}"

    def generate_email(self, domain='example.com'):
        unique_id = uuid.uuid4()
        return f"{unique_id}@{domain}"

    @allure.step('Verify password match')
    def verify_password_match(self):
        password_value = self.find(loc.PASSWORD).get_attribute('value')
        confirm_password_value = self.find(loc.CONFIRM_PASSWORD).get_attribute(
            'value')
        assert password_value == confirm_password_value, "Passwords do not match"

    @allure.step('Verify specific error message')
    def verify_error_message(self, expected_message):
        error_messages = self.find(loc.ERROR_MESSAGE)
        assert expected_message in error_messages.text
