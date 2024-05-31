import allure
from test_UI_volha_playwrite.pages.base_page import BasePage
from playwright.sync_api import expect
from test_UI_volha_playwrite.pages.locators.locators import RegisterPage as loc


class RegisterPage(BasePage):
    relative_url = '/customer/account/create/'

    @allure.step('Fill first name input')
    def fill_first_name(self, first_name):
        input_field = self.find_element(loc.FIRSTNAME)
        input_field.press_sequentially(first_name)

    @allure.step('Fill last name input')
    def fill_last_name(self, last_name):
        input_field = self.find_element(loc.LASTNAME)
        input_field.press_sequentially(last_name)

    @allure.step('Fill email input')
    def fill_email(self, email):
        input_field = self.find_element(loc.EMAIL)
        input_field.press_sequentially(email)

    @allure.step('Fill password input')
    def fill_password(self, password):
        input_field = self.find_element(loc.PASSWORD)
        input_field.press_sequentially(password)

    @allure.step('Fill confirm password input')
    def fill_confirm_password(self, password):
        input_field = self.find_element(loc.CONFIRMPASSWORD)
        input_field.press_sequentially(password)

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
        self.click_submit_btn()

    def check_mandatory_fields(self):
        err_text = 'This is a required field.'
        first_name_err = self.find_element(loc.FIRSTNAMEERR)
        last_name_err = self.find_element(loc.LASTNAMEERR)
        email_err = self.find_element(loc.EMAILERR)
        passw_err = self.find_element(loc.PASSWORDERR)

        expect(first_name_err).to_contain_text(err_text)
        expect(last_name_err).to_contain_text(err_text)
        expect(email_err).to_contain_text(err_text)
        expect(passw_err).to_contain_text(err_text)

    def check_email_invalid(self):
        err_text = 'Please enter a valid email address (Ex: johndoe@domain.com).'
        email_err = self.find_element(loc.EMAILERR)
        expect(email_err).to_contain_text(err_text)
