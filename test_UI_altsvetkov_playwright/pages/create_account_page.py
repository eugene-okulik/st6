import allure
from playwright.sync_api import expect

from test_UI_altsvetkov_playwright.pages.base_page import BasePage
from test_UI_altsvetkov_playwright.locators.locators import CreateAccountPageLoc as loc


class CreateAccountPage(BasePage):
    relative_url = '/customer/account/create/'

    # Заполнение полей ввода
    @allure.step('Field name entry')
    def name_input(self, name):
        self.find(loc.FIRST_NAME).fill(name)

    @allure.step('Field last name entry')
    def last_name_input(self, last_name):
        self.find(loc.LAST_NAME).fill(last_name)

    @allure.step('Field email entry')
    def email_input(self, email):
        self.find(loc.EMAIL).fill(email)

    @allure.step('Field password entry')
    def password_input(self, password):
        password_input = self.find(loc.PASSWORD)
        password_input.press_sequentially(password, delay=100)

    @allure.step('Field confirm password entry')
    def confirm_password_input(self, confirm_password):
        self.find(loc.CONFIRM_PASSWORD).fill(confirm_password)

    # Click the button create account
    @allure.step('Click on the button to create an account')
    def click_create_account_button(self):
        self.find(loc.BUTTON_CREATE_ACCOUNT).click()

    # Проверки наличия полей ввода
    @allure.step('Check the presence of the first name field')
    def check_first_name_field_is_displayed(self):
        name_field = self.find(loc.FIRST_NAME)
        expect(name_field).to_be_visible()

    @allure.step('Check the presence of the last name field')
    def check_last_name_field_displayed(self):
        last_name_field = self.find(loc.LAST_NAME)
        expect(last_name_field).to_be_visible()

    @allure.step('Check the presence of the email field')
    def check_email_field_displayed(self):
        email_field = self.find(loc.EMAIL)
        expect(email_field).to_be_visible()

    @allure.step('Check the presence of the password field')
    def check_password_field_displayed(self):
        password_field = self.find(loc.PASSWORD)
        expect(password_field).to_be_visible()

    @allure.step('Check the presence of the confirm password field')
    def check_confirm_password_field_displayed(self):
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        expect(confirm_password_field).to_be_visible()

    @allure.step('Check the presence of the create account button')
    def check_create_account_button_displayed(self):
        button_create_account = self.find(loc.BUTTON_CREATE_ACCOUNT)
        expect(button_create_account).to_be_visible()

    @allure.step('Check the presence of all fields')
    def check_all_fields_displayed(self):
        self.check_first_name_field_is_displayed()
        self.check_last_name_field_displayed()
        self.check_email_field_displayed()
        self.check_password_field_displayed()
        self.check_confirm_password_field_displayed()
        self.check_create_account_button_displayed()

    # Проверка наличия меток для полей и кнопок
    @allure.step('Check the presence of the first name field label')
    def check_first_name_field_label(self):
        name_field_label = self.find(loc.FIRST_NAME_LABEL)
        expect(name_field_label).to_have_text('First Name')

    @allure.step('Check the presence of the last name field label')
    def check_last_name_field_label(self):
        last_name_field_label = self.find(loc.LAST_NAME_LABEL)
        expect(last_name_field_label).to_have_text('Last Name')

    @allure.step('Check the presence of the email field label')
    def check_email_field_label(self):
        email_field_label = self.find(loc.EMAIL_LABEL)
        expect(email_field_label).to_have_text('Email')

    @allure.step('Check the presence of the password field label')
    def check_password_field_label(self):
        password_field_label = self.find(loc.PASSWORD_LABEL)
        expect(password_field_label).to_have_text('Password')

    @allure.step('Check the presence of the confirm password field label')
    def check_confirm_password_field_label(self):
        confirm_password_field_label = self.find(loc.CONFIRM_PASSWORD_LABEL)
        expect(confirm_password_field_label).to_have_text('Confirm Password')

    @allure.step('Check the button label')
    def check_create_account_button_label(self):
        create_account_button_label = self.find(loc.BUTTON_CREATE_ACCOUNT)
        expect(create_account_button_label).to_have_text('Create an Account')

    @allure.step('Check the presence of all fields labels')
    def check_all_fields_labels(self):
        self.check_first_name_field_label()
        self.check_last_name_field_label()
        self.check_email_field_label()
        self.check_password_field_label()
        self.check_confirm_password_field_label()
        self.check_create_account_button_label()

    # Проверка рекомендаций для ввода пароля
    @allure.step('Check message Minimum field length requirements for password')
    def check_password_field_requirements_prompt(self):
        password_hint = self.find(loc.PASSWORD_ERROR_HINT)
        expect(password_hint).to_contain_text('Minimum length of this field must be equal or greater than 8 symbols. '
                                              'Leading and trailing spaces will be ignored.')

    # Проверка сообщения об успешной регистрации
    @allure.step('Check the message about the successful creation of an account')
    def check_create_account_message(self):
        registration_message = self.find(loc.SUCCESSFUL_REGISTRATION_MESSAGE)
        expect(self.page).to_have_url('https://magento.softwaretestingboard.com/customer/account/')
        expect(registration_message).to_have_text('Thank you for registering with Main Website Store.')
