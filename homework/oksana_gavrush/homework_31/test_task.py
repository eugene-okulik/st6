from playwright.sync_api import Page, expect


def test_visible_color_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    button.wait_for(state="visible")
    expect(button).to_have_css('color', 'rgb(220, 53, 69)')
    button.click()


def test_authentication(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.locator('#firstName').fill('Edward')
    page.locator('#lastName').fill('Halpern')
    page.locator('#userEmail').fill('edward@gmail.com')
    page.locator('label[for="gender-radio-1"]').click()
    page.locator('#userNumber').fill('6235052204')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.click()
    date_of_birth.press('Meta+A')
    date_of_birth.press_sequentially('10 March 1998')
    date_of_birth.press('Enter')

    subjects = page.locator('#subjectsContainer')
    subjects.click()
    subjects.type('English', delay=100)
    subjects.press('Enter')
    subjects.type('Physics', delay=100)
    subjects.press('Enter')

    hobbies = page.locator('label[for="hobbies-checkbox-1"]')
    hobbies.click()

    page.wait_for_timeout(3000)
    address = page.locator('#currentAddress')
    address.fill('John A. Wilson Building, 1350 ')
    page.evaluate("window.scrollTo(0, 5000)")

    page.wait_for_timeout(3000)
    state = page.locator('(//*[@class="css-1g6gooi"])[2]//div//input')
    state.press_sequentially('n')
    state.press('Enter')

    city = page.locator('(//*[@class="css-1g6gooi"])[3]//div//input')
    city.press_sequentially('d')
    city.press('Enter')

    button = page.locator('#submit')
    button.click()
    page.wait_for_timeout(3000)

    email_check = page.locator('//tbody/tr[2]/td[2]')
    expect(email_check).to_have_text('edward@gmail.com')
