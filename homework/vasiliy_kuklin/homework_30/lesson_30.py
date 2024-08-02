from playwright.sync_api import Page


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_form_authentication = page.get_by_role('link', name='Form Authentication')
    search_form_authentication.click()
    username_fild = page.get_by_role('textbox', name='username')
    username_fild.fill('brozzz')
    password_fild = page.get_by_role('textbox', name='password')
    password_fild.fill('123456')
    login_button = page.get_by_role('button')
    login_button.click()
