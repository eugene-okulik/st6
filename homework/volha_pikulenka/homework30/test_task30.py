from playwright.sync_api import Page, expect


def test_30(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    auth_form = page.get_by_role('link', name='Form Authentication')
    auth_form.click()

    username_input = page.get_by_role('textbox', name='Username')
    password_input = page.get_by_role('textbox', name='Password')
    login_btn = page.get_by_role('button')

    username_input.fill('tomsmith')
    password_input.fill('SuperSecretPassword!')
    login_btn.click()

    header4 = page.get_by_role('heading', name='Welcome to the Secure Area.')
    expect(header4).to_be_visible()
    1

