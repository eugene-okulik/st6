from playwright.sync_api import expect
from test_UI_eklimova_playwright.pages.base_page import BasePage
from test_UI_eklimova_playwright.pages.locators import CreateNewAccountPage as loc
import json
import allure


def load_credentials(file_path='creds.json'):
    with open(file_path, 'r') as file:
        return json.load(file)


class CreateNewAccount(BasePage):
    related_url = '/customer/account/create/'

    def enter_firstname(self, firstname_value):
        self.find(loc.FIRSTNAME).fill(firstname_value)

    def enter_lastname(self, lastname_value):
        self.find(loc.LASTNAME).fill(lastname_value)

    def enter_email(self, email_value):
        self.find(loc.EMAIL).fill(email_value)

    def enter_password(self, password_value):
        password = self.find(loc.PASSWORD)
        password.type(password_value, delay=100)

    def enter_confirmation_password(self, confirmation_password_value):
        password_confirmation = self.find(loc.CONFIRMATION_PASSWORD)
        password_confirmation.type(confirmation_password_value, delay=100)

    def enter_wrong_confirmation_password(self, wrong_confirmation_password_value):
        password_confirmation = self.find(loc.CONFIRMATION_PASSWORD)
        password_confirmation.type(wrong_confirmation_password_value, delay=100)

    @allure.step("Sent the correct value for all required fields")
    def send_data_to_required_fields(self, creds):
        self.enter_firstname(creds['firstname'])
        self.enter_lastname(creds['lastname'])
        self.enter_email(creds['email'])
        self.enter_password(creds['password'])
        self.enter_confirmation_password(creds['confirmation_password'])

    @allure.step("Click on 'Create on account' button")
    def click_on_create_button(self):
        self.find(loc.BUTTON_CREATE).click()

    @allure.step("Check that user name and email is correct")
    def check_user_name_and_email(self, creds):
        person_info = self.page.locator(loc.PERSON_INFO)
        expect(person_info).to_be_visible()

        element = self.page.locator(loc.PERSON_INFO_VALUE)
        html_content = element.get_attribute('innerHTML')
        person_name, person_email = [line.strip() for line in html_content.split('<br>') if line.strip()]

        expect(person_name).to_have_text(f"{creds['firstname']} {creds['lastname']}")
        expect(person_email).to_have_text(creds['email'])

    @allure.step("Send data without lastname")
    def sent_data_without_lastname(self, creds):
        self.enter_firstname(creds['firstname'])
        self.enter_email(creds['email'])
        self.enter_password(creds['password'])
        self.enter_confirmation_password(creds['confirmation_password'])

    @allure.step("Check that error message is appeared for not fielded field")
    def check_error_message_about_missed_data(self):
        warning_mes = self.page.locator(loc.LASTNAME_WARNING_MES)
        expect(warning_mes).to_be_visible()
        expect(warning_mes).to_have_text("This is a required field.")

    @allure.step('send data with different password')
    def send_data_with_different_password(self, creds):
        self.enter_firstname(creds['firstname'])
        self.enter_lastname(creds['lastname'])
        self.enter_email(creds['email'])
        self.enter_password(creds['password'])
        self.enter_confirmation_password(creds['wrong_confirmation_password'])

    @allure.step("check error message about password value")
    def check_error_message_about_password_value(self):
        warning_mes = self.page.locator(loc.PASSWORD_WARNING_MES)
        expect(warning_mes).to_be_visible()
        expect(warning_mes).to_have_text("Please enter the same value again.")
