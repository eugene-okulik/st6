from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.close()


def test_filling_form(driver):
    driver.maximize_window()
    driver.get('https://demoqa.com/automation-practice-form')

    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys('Vasiliy')

    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Kuklin')

    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys('vasiliy@gmail.com')

    gender_radio = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    gender_radio.click()

    mobile_field = driver.find_element(By.ID, 'userNumber')
    mobile_field.send_keys('89262342323')

    birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    birth_field.send_keys(Keys.COMMAND + 'A')
    birth_field.send_keys('10 Oct 1982')
    birth_field.send_keys(Keys.ENTER)

    subjects_field = driver.find_element(By.ID, 'subjectsInput')
    subjects_field.send_keys('any_text')

    hobbies_checkbox = driver.find_element(By.CSS_SELECTOR, '[for^="hobbies-checkbox-1"]')
    hobbies_checkbox.click()

    current_address_field = driver.find_element(By.ID, 'currentAddress')
    current_address_field.send_keys('Moscow, Red place, home 1')

    state_field = driver.find_element(By.ID, 'state')
    state_field.click()
    state_field_select = driver.find_element(By.XPATH, "//div[contains(text(), 'Haryana')]")
    state_field_select.click()

    city_field = driver.find_element(By.ID, 'city')
    city_field.click()
    city_field_select = driver.find_element(By.XPATH, "//div[contains(text(), 'Panipat')]")
    city_field_select.click()

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    modal_window = driver.find_element(By.CLASS_NAME, 'modal-content')
    print(modal_window.text)
