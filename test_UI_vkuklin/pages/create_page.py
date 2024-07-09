import allure
from test_UI_vkuklin.pages.base_page import BasePage
from test_UI_vkuklin.pages.locators.locators import CreatePage as loc
from test_UI_vkuklin.tests.data.user_data import bad_email_numbers
from test_UI_vkuklin.tests.data.user_data import bad_email_long_text
from test_UI_vkuklin.tests.data.user_data import bad_email_not_point
from test_UI_vkuklin.tests.data.user_data import bad_email_not_domain
from test_UI_vkuklin.tests.data.user_data import bad_email_not_dog
from selenium.webdriver.common.keys import Keys
from test_UI_vkuklin.tests.data.user_data import first_name
from test_UI_vkuklin.tests.data.user_data import last_name
from test_UI_vkuklin.tests.data.user_data import email_address
from test_UI_vkuklin.tests.data.user_data import passwd
from test_UI_vkuklin.tests.data.user_data import confirm_passwd


class CreatePage(BasePage):
    relative_url = 'customer/account/create/'

    @allure.step('Check required fields')
    def check_required_fields(self):
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        first_name_notice = self.find(loc.ERROR_FIRST_NAME)
        last_name_notice = self.find(loc.ERROR_LAST_NAME)
        email_address_notice = self.find(loc.ERROR_EMAIL_ADDRESS)
        password_notice = self.find(loc.ERROR_PASSWORD)
        confirm_password_notice = self.find(loc.ERROR_CONFIRM_PASSWORD)
        assert (first_name_notice.text == 'This is a required field.'
                and last_name_notice.text == 'This is a required field.'
                and email_address_notice.text == 'This is a required field.'
                and password_notice.text == 'This is a required field.'
                and confirm_password_notice.text == 'This is a required field.')

    @allure.step('check email bad numbers')
    def check_email_numbers(self):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(bad_email_numbers)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('check email bad long text')
    def check_email_long_text(self):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(bad_email_long_text)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('check email bad not dog')
    def check_email_not_dog(self):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(bad_email_not_dog)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('check email bad not point')
    def check_email_not_point(self):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(bad_email_not_point)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('check email bad not domain')
    def check_email_not_domain(self):
        email_address = self.find(loc.EMAIL_ADDRESS)
        email_address.send_keys(bad_email_not_domain)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        email_address_error = self.find(loc.EMAIL_ADDRESS_ERROR)
        assert email_address_error.text == 'Please enter a valid email address (Ex: johndoe@domain.com).'

    @allure.step('clear email field')
    def clear_field_email(self):
        current_field = self.find(loc.EMAIL_ADDRESS)
        current_field.send_keys(Keys.COMMAND + 'a')
        current_field.send_keys(Keys.BACKSPACE)

    @allure.step('check pass not equal confirm pass')
    def check_password_not_valid(self):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.send_keys(last_name)
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(passwd)
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_passwd)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        confirm_pass_error = self.find(loc.ERROR_CONFIRM_PASSWORD)
        assert confirm_pass_error.text == 'Please enter the same value again.'

    @allure.step('check pass equal confirm pass')
    def check_password_valid(self):
        first_name_field = self.find(loc.FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.find(loc.LAST_NAME)
        last_name_field.send_keys(last_name)
        email_address_field = self.find(loc.EMAIL_ADDRESS)
        email_address_field.send_keys(email_address)
        password_field = self.find(loc.PASSWORD)
        password_field.send_keys(passwd)
        confirm_password_field = self.find(loc.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(passwd)
        button_create = self.find(loc.BUTTON_CREATE)
        button_create.click()
        success_create_account = self.find(loc.HEADER_MY_ACCOUNT)
        assert success_create_account.text == 'My Account'
