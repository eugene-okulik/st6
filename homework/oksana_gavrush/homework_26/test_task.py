from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(400, 1600)
    yield driver
    driver.quit()


def test_page(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    wait = WebDriverWait(driver, 10)
    firs_name = driver.find_element(By.CSS_SELECTOR, '#firstName')
    firs_name.send_keys('Edward')

    last_name = driver.find_element(By.CSS_SELECTOR, '#lastName')
    last_name.send_keys('Halpern')

    user_email = driver.find_element(By.CSS_SELECTOR, '#userEmail')
    user_email.send_keys('edward@gmail.com')

    gender = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    'label[for="gender-radio-2"]')))
    gender.click()

    mobile_number = driver.find_element(By.CSS_SELECTOR, '#userNumber')
    mobile_number.send_keys('6235052204')
    driver.execute_script("window.scrollTo(0, 5000);")

    date_input = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
    date_input.click()

    month_selector = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select")
    month_selector.send_keys("March")

    year_selector = driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select")
    year_selector.send_keys("1995")

    day_selector = wait.until(ec.element_to_be_clickable((
        By.CSS_SELECTOR, "div[class='react-datepicker__day react-datepicker__day--008']")))
    day_selector.click()

    subjects_input = wait.until(ec.element_to_be_clickable((By.ID, "subjectsInput")))
    subjects_input.send_keys("En")
    subjects_input.send_keys(Keys.ENTER)
    subjects_input.send_keys("Ph")
    subjects_input.send_keys(Keys.ENTER)

    hobbies = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')))
    hobbies.click()

    address = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#currentAddress')))
    address.send_keys('John A. Wilson Building, 1350 ')

    state = driver.find_element(By.XPATH, '(//*[@class="css-1g6gooi"])[2]//div//input')
    state.send_keys('NCR')
    state.send_keys(Keys.ENTER)

    city = driver.find_element(By.XPATH, '(//*[@class="css-1g6gooi"])[3]//div//input')
    city.send_keys('Delhi')
    city.send_keys(Keys.ENTER)
    sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, '#submit')
    button.click()

    print_rez = driver.find_element(By.CSS_SELECTOR, '.modal-body')
    print(print_rez.text)

    close_form = driver.find_element(By.CSS_SELECTOR, '#closeLargeModal')
    close_form.click()
