from playwright.sync_api import Page, expect


def test_red_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    btn = page.locator('#colorChange')
    expect(btn).to_have_css(name='color', value='rgb(220, 53, 69)')
    btn.click()


def test_2(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    first_name = page.locator('#firstName')
    first_name.press_sequentially('Volha')
    last_name = page.locator('#lastName')
    last_name.press_sequentially('Pikulenka')
    user_email = page.locator('#userEmail')
    user_email.press_sequentially('blabla@mail.com')
    user_mobile = page.locator('#userNumber')
    user_mobile.press_sequentially('5646743132')
    user_gender = page.query_selector('#gender-radio-2')
    user_gender.evaluate('ele1 => ele1.checked=true')

    calendar = page.locator('#dateOfBirthInput')
    calendar.click()
    calendar.press('Control+a')
    calendar.press_sequentially('15 May 1990')
    calendar.press('Enter')

    sport_hobbie = page.locator('#hobbies-checkbox-1')
    sport_hobbie.evaluate('ele1 => ele1.checked=true')

    subjects_field = page.locator('#subjectsInput')
    subjects_field.click()
    subjects_field.press('a')
    subjects_field.press('Enter')
    subjects_field.press('b')
    subjects_field.press('Enter')

    user_address = page.locator('#currentAddress')
    user_address.press_sequentially('CA, LA, Wisteria lain, 14')

    state = page.locator('#react-select-3-input')
    state.press_sequentially('ha')
    state.press('Enter')
    city = page.locator('#react-select-4-input')
    city.press_sequentially('pa')
    city.press('Enter')

    page.locator('#submit').click()

    rows = page.locator('//tbody/tr[1]/td[2]')

    expect(rows).to_have_text("Volha Pikulenka")
