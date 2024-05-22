from playwright.sync_api import Page


def test_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    form_auth = page.get_by_role('link', name='Form Authentication')
    user_name = page.get_by_role('textbox').first
    passw = page.get_by_role('textbox').nth(1)
    login_button = page.get_by_role('button')
    form_auth.click()
    user_name.fill('Kate')
    passw.fill('QWerty12345^')
    login_button.click()
