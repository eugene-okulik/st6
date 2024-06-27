from playwright.sync_api import Page, expect


def test_check_click_afte_button_became_red(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_after = page.locator('//*[@id="visibleAfter"]')
    button = page.locator('//*[@id="colorChange"]')
    expect(button_after).to_be_visible(timeout=10000)
    button.click()


def test_fill_in_the_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('//*[@id="firstName"]').fill("kate")
    page.locator('//*[@id="lastName"]').fill("klimova")
    page.locator('//*[@id="userEmail"]').fill("test@test.ru")
    page.locator('//*[@for="gender-radio-3"]').click()
    page.locator('//*[@id="userNumber"]').fill("375331234576")
    birthday = page.locator('//*[@id="dateOfBirthInput"]')
    birthday.fill("26 Jun 1990")
    birthday.press('Enter')
    subject = page.locator('//input[@id="subjectsInput"]')
    subject.fill("English")
    subject.press('Enter')
    page.locator('//*[@for="hobbies-checkbox-3"]').click()
    page.locator('//*[@id="currentAddress"]').fill('Belarus')
    state = page.locator('//*[@id="react-select-3-input"]')
    state.fill("Haryana")
    state.press('Enter')
    city = page.locator('//*[@id="react-select-4-input"]')
    city.fill("Karnal")
    city.press('Enter')
    page.locator('//*[@id="submit"]').click()

    student_name = page.locator("//tr/td[text()='Student Name']/following-sibling::td")
    expect(student_name).to_have_text("kate klimova")
