from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_page_practice(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    assert not choose_language.is_selected()
    dropdown = Select(choose_language)
    dropdown.select_by_value('1')
    selected_option = dropdown.first_selected_option
    assert selected_option.get_attribute('value') == '1'
    submit_button = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')
    submit_button.click()
    result = driver.find_element(By.CSS_SELECTOR, '#result-text')
    expected_text = "Python"
    assert result.text == expected_text


def test_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    element = WebDriverWait(driver, 7).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '[id="finish"] >h4'))
    )
    assert element.text == "Hello World!"
