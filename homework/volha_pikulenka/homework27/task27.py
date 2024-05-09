from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_task_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    dropdown = Select(choose)
    dropdown.select_by_value('2')
    assert choose.get_attribute('value') == '2'


def test_task_2(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.XPATH, '//button')
    driver.execute_script("arguments[0].click();", button)
    wait = WebDriverWait(driver, 10)
    finish_text = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#finish')))
    assert finish_text.get_attribute('innerText') == 'Hello World!'
