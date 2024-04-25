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


def test_open_page(driver):
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_field = driver.find_element(By.ID, 'id_text_string')
    search_field.send_keys('find_me')
    search_field.send_keys(Keys.ENTER)
    result_field = driver.find_element(By.ID, 'result-text').text

    assert result_field == 'find_me'
    print(str(result_field))
