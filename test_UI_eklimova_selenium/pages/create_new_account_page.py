from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_UI_eklimova_selenium.pages.base_page import BasePage
from test_UI_eklimova_selenium.pages.locators import CreateNewAccountPage as loc

import allure


class CreateNewAccount(BasePage):
    related_url = '/customer/account/create/'

    def enter_firstname(self):
        firstname = self.find(loc.FIRSTNAME)
        firstname.send_keys("kate")

    def enter_lastname(self):
        lastname = self.find(loc.LASTNAME)
        lastname.send_keys("klimova")

    def enter_email(self):
        email = self.find(loc.EMAIL)
        email.send_keys("test@test.eww")

    def enter_password(self):
        password = self.find(loc.PASSWORD)
        password.send_keys("QWerty!@3456")

    def enter_confirmation_password(self):
        password_confirmation = self.find(loc.CONFIRMATION_PASSWORD)
        password_confirmation.send_keys("QWerty!@3456")

    def enter_wrong_confirmation_password(self):
        password_confirmation = self.find(loc.CONFIRMATION_PASSWORD)
        password_confirmation.send_keys("QWerty!23456")

    @allure.step("Sent the correct value for all required fields")
    def send_data_to_required_fields(self):
        self.enter_firstname()
        self.enter_lastname()
        self.enter_email()
        self.enter_password()
        self.enter_confirmation_password()

    @allure.step("Click on 'Create on account' button")
    def click_on_create_button(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()

    @allure.step("Check that user name and email is correct")
    def check_user_name_and_email(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(loc.PERSON_INFO))

        element = self.find(loc.PERSON_INFO_VALUE)
        html_content = element.get_attribute('innerHTML')
        print(html_content)
        person_name, person_email = [line.strip() for line in html_content.split('<br>') if line.strip()]

        assert person_name == "kate klimova"
        assert person_email == "test@test.eww"

    @allure.step("Send data without lastname")
    def sent_data_without_lastname(self):
        self.enter_firstname()
        self.enter_email()
        self.enter_password()
        self.enter_confirmation_password()

    @allure.step("Check that error message is appeared for not fielded field")
    def check_error_message_about_missed_data(self):
        wait = WebDriverWait(self.driver, 10)
        warning_mes = wait.until(ec.visibility_of_element_located(loc.LASTNAME_WARNING_MES)).text

        assert warning_mes == "This is a required field."

    @allure.step('send data with different password')
    def send_data_with_different_password(self):
        self.enter_firstname()
        self.enter_lastname()
        self.enter_email()
        self.enter_password()
        self.enter_wrong_confirmation_password()

    @allure.step("check error message about password value")
    def check_error_message_about_password_value(self):
        wait = WebDriverWait(self.driver, 10)
        warning_mes = wait.until(
            ec.visibility_of_element_located(loc.PASSWORD_WARNING_MES)).text

        assert warning_mes == "Please enter the same value again."
