import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_result_text(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    choose_language_field = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    language = Select(choose_language_field)
    language.select_by_visible_text('Python')
    driver.find_element(By.CSS_SELECTOR, '#submit-id-submit').click()
    result_text = driver.find_element(By.CSS_SELECTOR, '#result-text')
    assert result_text.text == 'Python'


def test_text_hello_word(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start > button').click()
    hello = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#finish > h4')))
    assert hello.is_displayed()
