from playwright.sync_api import Page, expect
from faker import Faker


def test_button_change_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', timeout=60000)
    button = page.locator('#colorChange')
    expect(button).to_have_class('mt-4 text-danger btn btn-primary')
    button.click()


fake = Faker("ru_RU")
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.ascii_free_email()
mobile_number = fake.numerify('##########')
address = 'Россия, ' + fake.address()


def test_registration_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', timeout=100000)
    firstname = page.locator('#firstName')
    lastname = page.locator('#lastName')
    email_fild = page.locator('#userEmail')
    radio_gender = page.locator('[for="gender-radio-1"]')
    mobile = page.locator('#userNumber')
    birth_day = page.locator('#dateOfBirthInput')
    hobbies = page.locator('[for="hobbies-checkbox-1"]')
    current_address = page.locator('#currentAddress')

    firstname.fill(first_name)
    lastname.fill(last_name)
    email_fild.fill(email)
    radio_gender.check()
    mobile.fill(mobile_number)
    birth_day.fill('01 Aug 1999')
    hobbies.check()
    current_address.fill(address)

    # Заполняем поле по букве и выбираем и списка
    subjects = page.locator('#subjectsInput')
    subjects.click()
    subjects.press_sequentially('Commerce', delay=100)
    subjects.press('Enter')
    subjects_selected = page.locator('.subjects-auto-complete__multi-value__label')
    expect(subjects_selected).to_have_text('Commerce')

    state_dropdown = page.locator('#state')
    state_dropdown.click()
    state_dropdown.press_sequentially('utt', delay=500)
    state_dropdown.press('Enter')
    city_dropdown = page.locator('#city')
    city_dropdown.click()
    city_dropdown.press_sequentially('mer', delay=500)
    city_dropdown.press('Enter')

    button = page.locator('#submit')
    button.click()

    modal = page.locator('//td[text()="Student Name"]//following-sibling::td')
    student_name = f'{first_name} {last_name}'
    expect(modal).to_have_text(student_name)
