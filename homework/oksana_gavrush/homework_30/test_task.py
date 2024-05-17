from playwright.sync_api import Page, expect


def test_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/', timeout=60000)
    search_form = page.get_by_role('link', name='Form Authentication')
    search_form.click()
    username = page.get_by_role('textbox', name='Username')
    username.fill('Username')
    password = page.get_by_role('textbox', name='Password')
    password.fill('@11DovmvE')
    button = page.get_by_role('button', name=' Login')
    button.click()
    expect(page).to_have_title('The Internet')
