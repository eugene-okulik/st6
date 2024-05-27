from data.data_for_tests import CreateAccountData as acc


def test_create_account(create_account_page):
    create_account_page.open()
    create_account_page.name_input(acc.name)
    create_account_page.last_name_input(acc.last_name)
    create_account_page.email_input(acc.email)
    create_account_page.password_input(acc.password)
    create_account_page.confirm_password_input(acc.password)
    create_account_page.click_create_account_button()
    create_account_page.check_create_account_message()


def test_fields_and_button_is_displayed(create_account_page):
    create_account_page.open()
    create_account_page.check_all_fields_displayed()
    create_account_page.check_create_account_button_displayed()


def test_labels_match_the_fields(create_account_page):
    create_account_page.open()
    create_account_page.check_all_fields_labels()


def test_password_field_requirements(create_account_page):
    create_account_page.open()
    create_account_page.password_input('1')
    create_account_page.check_password_field_requirements_prompt()
