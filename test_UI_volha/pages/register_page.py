import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_UI_volha.pages.base_page import BasePage
from test_UI_volha.pages.locators.locators import RegisterPage as loc


class RegisterPage(BasePage):
    relative_url = '/customer/account/create/'

    @allure.step('Fill first name input')
    def fill_first_name(self, first_name):
        input_field = self.find_element(loc.FIRSTNAME)
        input_field.send_keys(first_name)
        assert input_field.get_attribute('value') == first_name

    @allure.step('Fill last name input')
    def fill_last_name(self, last_name):
        input_field = self.find_element(loc.LASTNAME)
        input_field.send_keys(last_name)
        assert input_field.get_attribute('value') == last_name

    @allure.step('Fill email input')
    def fill_email(self, email):
        input_field = self.find_element(loc.EMAIL)
        input_field.send_keys(email)
        assert input_field.get_attribute('value') == email

    @allure.step('Fill password input')
    def fill_password(self, password):
        input_field = self.find_element(loc.PASSWORD)
        input_field.send_keys(password)
        assert input_field.get_attribute('value') == password

    @allure.step('Fill confirm password input')
    def fill_confirm_password(self, password):
        input_field = self.find_element(loc.CONFIRMPASSWORD)
        input_field.send_keys(password)
        assert input_field.get_attribute('value') == password

    @allure.step('Fill the form')
    def fill_the_form(self, first_name, last_name, email, password):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(password)

    def click_submit_btn(self):
        btn = self.find_element(loc.CREATEACCOUNTBTN)
        btn.click()

    @allure.step('Click Create an account btn')
    def submit_registration(self):
        current_url = self.driver.current_url
        self.click_submit_btn()
        WebDriverWait(self.driver, 3).until(ec.url_changes(current_url))

    def check_mandatory_fields(self):
        err_text = 'This is a required field.'
        first_name_err = self.find_element(loc.FIRSTNAMEERR)
        last_name_err = self.find_element(loc.LASTNAMEERR)
        email_err = self.find_element(loc.EMAILERR)
        passw_err = self.find_element(loc.PASSWORDERR)

        assert first_name_err.get_attribute('innerText') == err_text
        assert last_name_err.get_attribute('innerText') == err_text
        assert email_err.get_attribute('innerText') == err_text
        assert passw_err.get_attribute('innerText') == err_text

    def check_email_invalid(self):
        err_text = 'Please enter a valid email address (Ex: johndoe@domain.com).'
        email_err = self.find_element(loc.EMAILERR)
        assert email_err.get_attribute('innerText') == err_text
