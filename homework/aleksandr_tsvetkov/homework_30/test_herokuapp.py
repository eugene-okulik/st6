from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    name_field = page.get_by_role('textbox', name='Username')
    name_field.fill('tomsmith')
    expect(name_field).to_have_value('tomsmith')
    password_field = page.get_by_role('textbox', name='Password')
    password_field.fill('SuperSecretPassword!')
    expect(password_field).to_have_value('SuperSecretPassword!')
    button_login = page.get_by_role('button', name=' Login')
    expect(button_login).to_be_enabled()
    button_login.click()
    expect(page).to_have_url('https://the-internet.herokuapp.com/secure')
    page.pause()
