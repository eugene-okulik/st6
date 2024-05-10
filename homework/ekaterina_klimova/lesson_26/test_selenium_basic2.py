from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

SAIT = "https://demoqa.com/automation-practice-form"


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(730, 980)
    yield driver


@pytest.fixture()
def fill_form(driver):
    def _fill_form():
        driver.get(SAIT)
        print(driver.current_url)
        print(driver.title)

        first_name = driver.find_element(By.XPATH, "//input[@id='firstName']")
        first_name.send_keys("Ekaterina")

        second_name = driver.find_element(By.XPATH, '//input[@id="lastName"]')
        second_name.send_keys("Klimova")

        email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
        email.send_keys("test@test.by")

        gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
        gender.click()

        mobile = driver.find_element(By.XPATH, '//input[@id="userNumber"]')
        mobile.send_keys("3753312345")

        data_picker = driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]')
        data_picker.send_keys(Keys.CONTROL + 'a')
        data_picker.send_keys("09 Jul 2034")
        data_picker.send_keys(Keys.ESCAPE)

        current_address = driver.find_element(By.ID, "currentAddress")
        current_address.send_keys("str Molodezhnaya")

        hobby1 = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-1"]')
        hobby1.click()

        hobby2 = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-2"]')
        hobby2.click()

        hobby3 = driver.find_element(By.XPATH, '//*[@for="hobbies-checkbox-3"]')
        hobby3.click()

        button = driver.find_element(By.XPATH, '//button[@id="submit"]')
        driver.execute_script("arguments[0].scrollIntoView();", button)
        state = driver.find_element(By.ID, "react-select-3-input")
        state.send_keys("Haryana")
        state.send_keys(Keys.ENTER)

        driver.execute_script("arguments[0].scrollIntoView();", button)
        city = driver.find_element(By.ID, "react-select-4-input")
        city.send_keys("Karnal")
        city.send_keys(Keys.ENTER)

        subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
        subjects.send_keys("English")
        subjects.send_keys(Keys.ENTER)

        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

    return _fill_form


def test_check_fielded_form(fill_form, driver):
    fill_form()

    wait = WebDriverWait(driver, 10)

    student_name = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Student Name']/following-sibling::td"))).text
    form_mail = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Student Email']/following-sibling::td"))).text
    form_gender = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Gender']/following-sibling::td"))).text
    form_mobile = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Mobile']/following-sibling::td"))).text
    form_birthday = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Date of Birth']/following-sibling::td"))).text
    form_subjects = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Subjects']/following-sibling::td"))).text
    form_hobbies = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Hobbies']/following-sibling::td"))).text
    form_adress = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='Address']/following-sibling::td"))).text
    form_state = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//tr/td[text()='State and City']/following-sibling::td"))).text

    assert student_name == "Ekaterina Klimova"
    assert form_mail == "test@test.by"
    assert form_gender == "Female"
    assert form_mobile == "3753312345"
    assert form_birthday == "09 July,2034"
    assert form_subjects == "English"
    assert form_hobbies == "Sports, Reading, Music"
    assert form_adress == "str Molodezhnaya"
    assert form_state == "Haryana Karnal"
