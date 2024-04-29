import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')

    # Поле ввода First Name
    first_name_input = driver.find_element(By.CSS_SELECTOR, '#firstName')
    first_name_input.send_keys('Aliaksandr')
    assert first_name_input.get_attribute('value') == 'Aliaksandr'

    # Поле ввода Last Name
    last_name_input = driver.find_element(By.CSS_SELECTOR, '#lastName')
    last_name_input.send_keys('Tsviatkou')
    assert last_name_input.get_attribute('value') == 'Tsviatkou'

    # Поле ввода Email
    email_input = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    email_input.send_keys('sobaka@gmail.com')
    assert email_input.get_attribute('value') == 'sobaka@gmail.com'

    # Gender radiobutton
    gender_checkbox = driver.find_element(By.CSS_SELECTOR, '#gender-radio-1')
    driver.execute_script("arguments[0].click();", gender_checkbox)
    assert gender_checkbox.is_selected()

    # Поле ввода Mobile Number
    phone_number_input = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    phone_number_input.send_keys('1234567890')
    assert phone_number_input.get_attribute('value') == '1234567890'

    # Поле Date of Birth
    birth_day_field = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
    birth_day_field.click()

    # Year dropdown
    year_drop_down = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    y_drop_down = Select(year_drop_down)
    y_drop_down.select_by_value('1988')
    assert y_drop_down.first_selected_option.text == '1988'

    # Month dropdown
    month_dropdown = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    m_drop_down = Select(month_dropdown)
    m_drop_down.select_by_index(0)
    assert m_drop_down.first_selected_option.text == 'January'

    # Date picker
    date_picker = driver.find_element(By.CSS_SELECTOR, '[class = "react-datepicker__day react-datepicker__day--028"]')
    date_picker.click()
    date_of_birthday = birth_day_field.get_attribute('value')
    assert date_of_birthday == '28 Jan 1988'

    # поле ввода Subjects
    subjects_field = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subjects_field.click()
    subjects_field.send_keys('ma')
    subjects_field.send_keys(Keys.ENTER)
    subjects_field.send_keys('his')
    subjects_field.send_keys(Keys.ENTER)
    close_button = driver.find_element(By.XPATH, '(//div [@class="css-xb97g8 '
                                                 'subjects-auto-complete__multi-value__remove"])[2]')
    close_button.click()

    # Hobbies checkboxes
    hobbies_checkboxes = driver.find_elements(By.CSS_SELECTOR, '[type="checkbox"]')
    driver.execute_script("arguments[0].click();", hobbies_checkboxes[0])
    driver.execute_script("arguments[0].click();", hobbies_checkboxes[1])
    assert hobbies_checkboxes[0].is_selected()
    assert hobbies_checkboxes[1].is_selected()

    # Address field
    address_input = driver.find_element(By.CSS_SELECTOR, '#currentAddress')
    address_input.send_keys('Belarus, Vitebsk, Frunze 13-4, 123441')
    assert address_input.get_attribute('value') == 'Belarus, Vitebsk, Frunze 13-4, 123441'

    # State and city dropdown
    state_input = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    driver.execute_script("arguments[0].click();", state_input)
    state_input.send_keys('n')
    state_input.send_keys(Keys.ENTER)
    city_input = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    driver.execute_script("arguments[0].click();", city_input)
    city_input.send_keys('g')
    city_input.send_keys(Keys.ENTER)

    # Submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, '#submit')
    assert submit_button.is_enabled()
    driver.execute_script("arguments[0].click();", submit_button)

    modal_content = driver.find_element(By.CSS_SELECTOR, '.modal-body')
    input_data = modal_content.text
    print(input_data)
