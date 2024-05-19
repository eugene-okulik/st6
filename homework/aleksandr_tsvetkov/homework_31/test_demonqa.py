from playwright.sync_api import Page, expect
from faker import Faker
import os


# Путь к файлу для загрузки фото в форму
repo_path = os.path.dirname(__file__)
upload_file = os.path.join(repo_path, 'fidji.jpg')

fake = Faker('ru_RU')

first_name = fake.first_name_male()
last_name = fake.last_name_male()
email = fake.free_email()
phone_number = fake.numerify('##########')
address = 'Россия, ' + fake.address()


def test_button_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button_color = page.locator('#colorChange')
    expect(button_color).to_have_class('mt-4 text-danger btn btn-primary')
    button_color.click()


def test_registration_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    # Заполнение имени
    page.fill('#firstName', first_name)

    # Заполнение фамилии
    page.fill('#lastName', last_name)

    # Заполнение email
    page.fill('#userEmail', email)

    # Выбор пола
    page.locator('[for="gender-radio-1"]').click()

    # Заполнение номера телефона
    page.fill('#userNumber', phone_number)

    # Заполнение даты рождения
    date_input = page.locator('#dateOfBirthInput')
    date_input.click()
    month_dropdown = page.locator('.react-datepicker__month-select')
    month_dropdown.select_option('0')
    year_dropdown = page.locator('.react-datepicker__year-select')
    year_dropdown.select_option('1988')
    day_picker = page.locator('//*[@class="react-datepicker__day react-datepicker__day--028"]')
    day_picker.click()

    expect(date_input).to_have_value('28 Jan 1988')

    # Выбор предметов
    subject_input = page.locator('#subjectsInput')
    subject_input.click()
    subject_input.fill('computer')
    subject_input.press('Enter')
    subject_input.fill('en')
    subject_input.press('Enter')
    selected_subjects = page.locator('.subjects-auto-complete__multi-value__label')

    expect(selected_subjects.nth(0)).to_have_text('Computer Science')
    expect(selected_subjects.nth(1)).to_have_text('English')

    # Выбор хобби
    sport_checkbox = page.locator('//*[@for="hobbies-checkbox-1"]')
    sport_checkbox.click()
    music_checkbox = page.locator('[for="hobbies-checkbox-3"]')
    music_checkbox.click()

    expect(sport_checkbox).to_be_checked()
    expect(music_checkbox).to_be_checked()

    # Загрузка фото
    upload_picture = page.locator('#uploadPicture')
    upload_picture.set_input_files(upload_file)

    # Заполнение адреса
    address_input = page.locator('#currentAddress')
    address_input.fill(address)

    expect(address_input).to_have_value(address)

    # Выбор штата и города
    state_dropdown = page.locator('#state > div > .css-1hwfws3 > .css-1wa3eu0-placeholder')
    state_dropdown.click()
    page.locator('#react-select-3-option-1').click()

    city_dropdown = page.locator('#city > div > .css-1hwfws3 > .css-1wa3eu0-placeholder')
    city_dropdown.click()
    page.locator('#react-select-4-option-1').click()
    selected_state_and_city = page.locator('.css-1uccc91-singleValue')

    expect(selected_state_and_city.nth(0)).to_have_text('Uttar Pradesh')
    expect(selected_state_and_city.nth(1)).to_have_text('Lucknow')

    # Отправка формы
    page.locator('#submit').click()

    # Проверка данных
    student_name = page.locator('//td[text()="Student Name"]/following-sibling::td')

    expected_student_name = f'{first_name} {last_name}'
    expect(student_name).to_have_text(expected_student_name)
