def test_registration_with_invalid_email(create_account):
    create_account.open()
    invalid_email = "not_an_email"
    password = "John2024!"
    create_account.complete_registration(invalid_email, password)
    create_account.verify_email_error_message()


def test_successful_registration_redirection(create_account):
    create_account.open()
    new_email = create_account.generate_email()
    password = "John2024!"
    expected_redirection_url = "https://magento.softwaretestingboard.com/customer/account/"
    create_account.complete_registration(new_email, password)
    create_account.verify_redirection(expected_redirection_url)


def test_duplicate_email_registration(create_account):
    create_account.open()
    email = "user@example.com"
    password = "John2024!"
    create_account.complete_registration(email, password)
    create_account.verify_error_message("There is already an account with this email address. If ")


def test_page_compare(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.hover_over_product()
    eco_friendly_page.add_to_wishlist()
    eco_friendly_page.check_login_message()


def test_add_to_cart_without_color(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.select_third_product()
    eco_friendly_page.select_product_size()
    eco_friendly_page.add_to_cart()
    eco_friendly_page.verify_color_error_message()


def test_maximum_quantity_items(eco_friendly_page):
    eco_friendly_page.open()
    eco_friendly_page.select_third_product()
    eco_friendly_page.select_product_size()
    eco_friendly_page.select_color()
    eco_friendly_page.set_product_quantity()
    eco_friendly_page.add_to_cart()
    eco_friendly_page.verify_quantity_error_message()


def test_search_field(sale_page):
    sale_page.open()
    sale_page.search_for_product()
    sale_page.verify_search_results()


def test_home_page_load(sale_page):
    sale_page.open()
    sale_page.click_more_button()
    sale_page.double_click_second_product()
    sale_page.verify_product_availability()


def test_elements_presence(sale_page):
    sale_page.open()
    sale_page.navigate_to_shorts()
    sale_page.verify_product_images()
    sale_page.verify_add_to_cart_buttons()
