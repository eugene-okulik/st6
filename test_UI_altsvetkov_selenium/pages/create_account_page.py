import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from test_UI_altsvetkov_selenium.pages.base_page import BasePage
from test_UI_altsvetkov_selenium.locators.locators import CreateAccountPageLoc as loc


class CreateAccountPage(BasePage):

    relative_url = '/customer/account/create/'

    # Заполнение полей ввода
    @allure.step('Field name entry')
    def name_input(self, name):
        self.find(loc.FIRST_NAME).send_keys(name)

    @allure.step('Field last name entry')
    def last_name_input(self, last_name):
        self.find(loc.LAST_NAME).send_keys(last_name)

    @allure.step('Field email entry')
    def email_input(self, email):
        self.find(loc.EMAIL).send_keys(email)

    @allure.step('Field password entry')
    def password_input(self, password):
        self.find(loc.PASSWORD).send_keys(password)

    @allure.step('Field confirm password entry')
    def confirm_password_input(self, confirm_password):
        self.find(loc.CONFIRM_PASSWORD).send_keys(confirm_password)

    # Click the button create account
    @allure.step('Click on the button to create an account')
    def click_create_account_button(self):
        self.find(loc.BUTTON_CREATE_ACCOUNT).click()

    # Проверки наличия полей ввода
    @allure.step('Check the presence of the first name field')
    def check_first_name_field_is_displayed(self):
        assert self.find(loc.FIRST_NAME).is_displayed()

    @allure.step('Check the presence of the last name field')
    def check_last_name_field_displayed(self):
        assert self.find(loc.LAST_NAME).is_displayed()

    @allure.step('Check the presence of the email field')
    def check_email_field_displayed(self):
        assert self.find(loc.EMAIL).is_displayed()

    @allure.step('Check the presence of the password field')
    def check_password_field_displayed(self):
        assert self.find(loc.PASSWORD).is_displayed()

    @allure.step('Check the presence of the confirm password field')
    def check_confirm_password_field_displayed(self):
        assert self.find(loc.CONFIRM_PASSWORD).is_displayed()

    @allure.step('Check the presence of the create account button')
    def check_create_account_button_displayed(self):
        assert self.find(loc.BUTTON_CREATE_ACCOUNT).is_displayed()

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
        assert self.find(loc.FIRST_NAME_LABEL).text == 'First Name'

    @allure.step('Check the presence of the last name field label')
    def check_last_name_field_label(self):
        assert self.find(loc.LAST_NAME_LABEL).text == 'Last Name'

    @allure.step('Check the presence of the email field label')
    def check_email_field_label(self):
        assert self.find(loc.EMAIL_LABEL).text == 'Email'

    @allure.step('Check the presence of the password field label')
    def check_password_field_label(self):
        assert self.find(loc.PASSWORD_LABEL).text == 'Password'

    @allure.step('Check the presence of the confirm password field label')
    def check_confirm_password_field_label(self):
        assert self.find(loc.CONFIRM_PASSWORD_LABEL).text == 'Confirm Password'

    @allure.step('Check the button label')
    def check_create_account_button_label(self):
        assert self.find(loc.BUTTON_CREATE_ACCOUNT).text == 'Create an Account'

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
        wait = WebDriverWait(self.driver, 5)
        password_req = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '#password-error')))
        assert password_req.text == ('Minimum length of this field must be equal or greater than 8 symbols. '
                                     'Leading and trailing spaces will be ignored.')

    # Проверка сообщения об успешной регистрации
    @allure.step('Check the message about the successful creation of an account')
    def check_create_account_message(self):
        assert self.driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/'
        assert self.driver.find_element(By.CSS_SELECTOR, '.message-success').text == ('Thank you for registering '
                                                                                      'with Main Website Store.')
