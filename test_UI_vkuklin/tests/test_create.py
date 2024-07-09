import pytest


@pytest.mark.regression
def test_required_fields(create_page):
    create_page.open()
    create_page.check_required_fields()


@pytest.mark.regression
def test_bad_email(create_page):
    create_page.open()
    create_page.check_email_numbers()
    create_page.clear_field_email()

    create_page.check_email_long_text()
    create_page.clear_field_email()

    create_page.check_email_not_dog()
    create_page.clear_field_email()

    create_page.check_email_not_point()
    create_page.clear_field_email()

    create_page.check_email_not_domain()


@pytest.mark.regression
def test_valid_password(create_page):
    create_page.open()
    create_page.check_password_valid()


@pytest.mark.regression
def test_not_valid_confirm_pas(create_page):
    create_page.open()
    create_page.check_password_not_valid()
