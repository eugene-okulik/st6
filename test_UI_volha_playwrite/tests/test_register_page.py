import time

from test_UI_volha_playwrite.tests.data_test.data_test import (first_name_faker,
                                                     last_name_faker,
                                                     email_faker,
                                                     password_faker,
                                                     invalid_email)


def test_register_flow(register_page, account_page):

    register_page.open()
    register_page.fill_the_form(first_name_faker,
                                last_name_faker,
                                email_faker,
                                password_faker)
    register_page.submit_registration()

    account_page.check_account_email(email_faker)


def test_invalid_email_message(register_page):
    register_page.open()
    register_page.fill_the_form(first_name_faker,
                                last_name_faker,
                                invalid_email,
                                password_faker)
    register_page.click_submit_btn()

    register_page.check_email_invalid()


def test_fields_are_required(register_page):
    register_page.open()
    register_page.click_submit_btn()
    register_page.check_mandatory_fields()
