from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_yoga_button(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    button = driver.find_element(By.CLASS_NAME, 'button')
    print(button.text)
    print(button.get_attribute('innerText'))
    print(button.value_of_css_property('background'))
    button.click()
    # sleep(3)


def test_css_selector(driver):
    driver.get('https://www.google.com/')
    input_field = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
    input_field.send_keys('cat')
    sleep(3)


def test_xpath(driver):
    driver.get('https://www.google.com/')
    input_field = driver.find_element(By.XPATH, '//*[@name="q"]')
    input_field.send_keys('cat')
    sleep(1)
    print(input_field.get_attribute('value'))
    print(input_field.get_attribute('id'))
    # input_field.clear()
    input_field.send_keys(Keys.CONTROL + 'a')
    sleep(1)
    input_field.send_keys(Keys.BACKSPACE)
    sleep(2)


def test_selected(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.CSS_SELECTOR, '#id_checkbox_0')
    assert not checkbox.is_selected()
    checkbox.click()
    assert checkbox.is_selected()


def test_is_displayed(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    reqs = driver.find_element(By.CSS_SELECTOR, '#req_text')
    assert not reqs.is_displayed()
    driver.find_element(By.CSS_SELECTOR, '#req_header').click()
    assert reqs.is_displayed()


def test_enabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.CSS_SELECTOR, '#submit-id-submit')
    assert not button.is_enabled()
    select_input = driver.find_element(By.CSS_SELECTOR, '#id_select_state')
    dropdown = Select(select_input)
    dropdown.select_by_value('enabled')
    assert button.is_enabled()
