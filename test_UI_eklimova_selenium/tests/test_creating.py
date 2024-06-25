# creating a new user is successful
# registration is not possible without all required fields
# check password the same

def test_registration_is_successful(create_new_account, creds):
    create_new_account.open()
    create_new_account.send_data_to_required_fields(creds)
    create_new_account.click_on_create_button()
    create_new_account.check_user_name_and_email(creds)


def test_check_registration_without_required_fields(create_new_account, creds):
    create_new_account.open()
    create_new_account.sent_data_without_lastname(creds)
    create_new_account.click_on_create_button()
    create_new_account.check_error_message_about_missed_data()


def test_password_and_confirmation_are_same(create_new_account, creds):
    create_new_account.open()
    create_new_account.send_data_with_different_password(creds)
    create_new_account.click_on_create_button()
    create_new_account.check_error_message_about_password_value()
