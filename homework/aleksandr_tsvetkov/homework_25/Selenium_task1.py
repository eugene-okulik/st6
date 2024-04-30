import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_input_field(driver):
    driver.get('https://www.qa-practice.com/')
    search_link_text_input = driver.find_element(By.LINK_TEXT, 'Text input')
    search_link_text_input.click()
    search_input_field = driver.find_element(By.ID, 'id_text_string')
    assert search_input_field.is_displayed()
    search_input_field.send_keys('Hello')
    search_input_field.send_keys(Keys.ENTER)
    search_result_text = driver.find_element(By.ID, 'result-text')
    print(search_result_text.text)
    assert search_result_text.text == 'Hello'
