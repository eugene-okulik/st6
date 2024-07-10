import pytest
from test_UI_vkuklin.pages.locators.locators import CreatePage as loc
from test_UI_vkuklin.tests.data.user_data import bad_email_numbers
from test_UI_vkuklin.tests.data.user_data import bad_email_long_text
from test_UI_vkuklin.tests.data.user_data import bad_email_not_point
from test_UI_vkuklin.tests.data.user_data import bad_email_not_domain
from test_UI_vkuklin.tests.data.user_data import bad_email_not_dog


@pytest.mark.regression
def test_required_fields(create_page):
    create_page.open()
    create_page.check_click_button_create()
    create_page.check_required_fields(loc.ERROR_FIRST_NAME)
    create_page.check_required_fields(loc.ERROR_LAST_NAME)
    create_page.check_required_fields(loc.ERROR_EMAIL_ADDRESS)
    create_page.check_required_fields(loc.ERROR_PASSWORD)
    create_page.check_required_fields(loc.ERROR_CONFIRM_PASSWORD)


@pytest.mark.regression
def test_bad_email_numbers(create_page):
    create_page.open()
    create_page.past_email_into(bad_email_numbers)
    create_page.check_email_field()
    create_page.clear_field_email()


@pytest.mark.regression
def test_bad_email_long_text(create_page):
    create_page.open()
    create_page.past_email_into(bad_email_long_text)
    create_page.check_email_field()


@pytest.mark.regression
def test_bad_email_not_dog(create_page):
    create_page.open()
    create_page.past_email_into(bad_email_not_dog)
    create_page.check_email_field()


@pytest.mark.regression
def test_bad_email_not_point(create_page):
    create_page.open()
    create_page.past_email_into(bad_email_not_point)
    create_page.check_email_field()


@pytest.mark.regression
def test_bad_email_not_domain(create_page):
    create_page.open()
    create_page.past_email_into(bad_email_not_domain)
    create_page.check_email_field()


@pytest.mark.regression
def test_valid_password(create_page):
    create_page.open()
    create_page.check_password_valid()


@pytest.mark.regression
def test_not_valid_confirm_pas(create_page):
    create_page.open()
    create_page.check_password_not_valid()
