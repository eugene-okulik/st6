import pytest
from test_UI_vkuklin_PW.tests.data.user_data import bad_email_numbers
from test_UI_vkuklin_PW.tests.data.user_data import bad_email_long_text
from test_UI_vkuklin_PW.tests.data.user_data import bad_email_not_point
from test_UI_vkuklin_PW.tests.data.user_data import bad_email_not_domain
from test_UI_vkuklin_PW.tests.data.user_data import bad_email_not_dog
from test_UI_vkuklin_PW.tests.data.user_data import first_name
from test_UI_vkuklin_PW.tests.data.user_data import last_name
from test_UI_vkuklin_PW.tests.data.user_data import email_address
from test_UI_vkuklin_PW.tests.data.user_data import passwd
from test_UI_vkuklin_PW.tests.data.user_data import confirm_passwd


@pytest.mark.regression
def test_required_fields(create_page):
    create_page.open()
    create_page.click_button_create()
    create_page.check_required_field_first_name('This is a required field.')
    create_page.check_required_field_last_name('This is a required field.')
    create_page.check_required_field_email('This is a required field.')
    create_page.check_required_field_password('This is a required field.')
    create_page.check_required_field_confirm_passw('This is a required field.')


@pytest.mark.regression
def test_bad_email_numbers(create_page):
    create_page.open()
    create_page.insert_email(bad_email_numbers)
    create_page.check_email_field('Please enter a valid email address (Ex: johndoe@domain.com).')
    create_page.clear_field_email()


@pytest.mark.regression
def test_bad_email_long_text(create_page):
    create_page.open()
    # create_page.past_email_into(bad_email_long_text)
    create_page.insert_email(bad_email_long_text)
    create_page.check_email_field('Please enter a valid email address (Ex: johndoe@domain.com).')


@pytest.mark.regression
def test_bad_email_not_dog(create_page):
    create_page.open()
    create_page.insert_email(bad_email_not_dog)
    create_page.check_email_field('Please enter a valid email address (Ex: johndoe@domain.com).')


@pytest.mark.regression
def test_bad_email_not_point(create_page):
    create_page.open()
    create_page.insert_email(bad_email_not_point)
    create_page.check_email_field('Please enter a valid email address (Ex: johndoe@domain.com).')


@pytest.mark.regression
def test_bad_email_not_domain(create_page):
    create_page.open()
    create_page.insert_email(bad_email_not_domain)
    create_page.check_email_field('Please enter a valid email address (Ex: johndoe@domain.com).')


@pytest.mark.regression
def test_valid_password(create_page):
    create_page.open()
    create_page.fill_first_name(first_name)
    create_page.fill_last_name(last_name)
    create_page.fill_email_address(email_address)
    create_page.fill_password(passwd)
    create_page.fill_confirm_password(passwd)
    create_page.click_button_create()
    create_page.check_password_valid('My Account')


def test_not_valid_confirm_pas(create_page):
    create_page.open()
    create_page.fill_first_name(first_name)
    create_page.fill_last_name(last_name)
    create_page.fill_email_address(email_address)
    create_page.fill_password(passwd)
    create_page.fill_confirm_password(confirm_passwd)
    create_page.click_button_create()
    create_page.check_incorrect_password('Please enter the same value again.')
