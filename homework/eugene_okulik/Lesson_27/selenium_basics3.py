from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    # sleep(3)
    yield driver
    driver.quit()


def test_one(driver):

    driver.get('https://magento.softwaretestingboard.com/')
    # men = driver.find_element("css selector", 'ui-id-5')
    # sleep(5)
    men = driver.find_element(By.CSS_SELECTOR, '#ui-id-5')
    men.click()


def test_disabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    select_input = driver.find_element(By.CSS_SELECTOR, '#id_select_state')
    dropdown = Select(select_input)
    dropdown.select_by_value('enabled')
    driver.find_element('css selector', '#submit-id-submit').click()


def test_explicit(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    # button = driver.find_element(By.ID, 'enableAfter')
    # WebDriverWait(driver, 6).until(ec.element_to_be_clickable(button))
    wait = WebDriverWait(driver, 6)
    button = wait.until(ec.element_to_be_clickable((By.ID, 'enableAfter')))
    button.click()


def test_cookies(driver):
    driver.get('https://www.demoblaze.com/')
    driver.add_cookie({'name': 'test', 'value': 'testvalue'})
    names = driver.find_elements(By.CSS_SELECTOR, '.card-title')
    print(names)
    print(driver.get_cookies())
    print(driver.get_cookie('user'))


def test_elements(driver):
    driver.get('https://www.demoblaze.com/')
    driver.add_cookie({'name': 'test', 'value': 'testvalue'})
    names = driver.find_elements(By.CSS_SELECTOR, '.card-title')
    # for element in names:
    #     print(element.text)
    last_link = names[-1].find_element(By.TAG_NAME, 'a')
    last_link.click()
    sleep(3)


def test_tabs(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    link = driver.find_element(By.ID, 'new-page-link')
    link.click()
    initial, new_tab = driver.window_handles
    driver.switch_to.window(new_tab)
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(initial)
    link.click()


def test_stale(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()
    driver.find_element(By.ID, 'submit-id-submit').click()
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()
