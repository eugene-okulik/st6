from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_fill(driver):
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')

    # user's data
    first_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    first_name.send_keys('Volha')
    assert first_name.get_attribute('value') == 'Volha'
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Pikulenka')
    assert last_name.get_attribute('value') == 'Pikulenka'
    user_email = driver.find_element(By.ID, 'userEmail')
    user_email.send_keys('blabla@mail.com')
    assert user_email.get_attribute('value') == 'blabla@mail.com'

    # gender
    user_gender = driver.find_element(By.ID, 'gender-radio-2')
    driver.execute_script("arguments[0].click();", user_gender)
    assert user_gender.is_selected()

    # mobile
    user_mobile = driver.find_element(By.ID, 'userNumber')
    user_mobile.send_keys('5646743132')
    assert user_mobile.get_attribute('value') == '5646743132'

    # birthdate
    calendar = driver.find_element(By.ID, 'dateOfBirthInput')
    calendar.click()
    month_calendar = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    month_dropdown = Select(month_calendar)
    month_dropdown.select_by_value('6')
    year_calendar = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    year_dropdown = Select(year_calendar)
    year_dropdown.select_by_value('1999')
    date_calendar = driver.find_element(By.XPATH, '//*[@aria-label="Choose Thursday, July 1st, 1999"]')
    date_calendar.click()
    assert calendar.get_attribute('value') == '01 Jul 1999'

    # hobbies
    sport_hobbie = driver.find_element(By.ID, 'hobbies-checkbox-1')
    reading_hobbie = driver.find_element(By.ID, 'hobbies-checkbox-2')
    music_hobbie = driver.find_element(By.ID, 'hobbies-checkbox-3')
    driver.execute_script("arguments[0].click();", sport_hobbie)
    driver.execute_script("arguments[0].click();", reading_hobbie)
    driver.execute_script("arguments[0].click();", music_hobbie)
    assert sport_hobbie.is_selected()
    assert reading_hobbie.is_selected()
    assert music_hobbie.is_selected()

    # subject
    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    subjects_field.click()
    subjects_field.send_keys('a')
    subjects_field.send_keys(Keys.ENTER)

    # address
    user_address = driver.find_element(By.ID, 'currentAddress')
    user_address.send_keys('CA, LA, Wisteria lain, 14')
    assert user_address.get_attribute('value') == 'CA, LA, Wisteria lain, 14'

    # state && city
    state = driver.find_element(By.CSS_SELECTOR, '#react-select-3-input')
    driver.execute_script("arguments[0].click();", state)
    state.send_keys('ha')
    state.send_keys(Keys.ENTER)
    city = driver.find_element(By.CSS_SELECTOR, '#react-select-4-input')
    driver.execute_script("arguments[0].click();", city)
    city.send_keys('pa')
    city.send_keys(Keys.ENTER)

    # submit
    submit_button = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].click();", submit_button)

    # print results
    table = driver.find_element(By.CLASS_NAME, 'table-responsive')
    results = table.text
    print(results)
