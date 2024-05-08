from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_yoga_button(driver):
    with allure.step('Open the page'):
        driver.get('https://magento.softwaretestingboard.com/')
    with allure.step('check that button exists'):
        button = driver.find_element(By.CSS_SELECTOR, '.action.more.button')
        assert button.is_displayed()


def test_search(driver):
    with allure.step('Open the page'):
        driver.get('https://magento.softwaretestingboard.com/')
    current_url = driver.current_url
    with allure.step('Enter text into search'):
        search = driver.find_element(By.CSS_SELECTOR, '#search')
        search.send_keys('top')
        search.submit()
        WebDriverWait(driver, 3).until(ec.url_changes(current_url))
    with allure.step('Check at least one name has searched word'):
        names = driver.find_elements(By.CSS_SELECTOR, '.product-item-link')
        assert len(list(filter(lambda x: 'top' in x.text.lower(), names))) > 0

