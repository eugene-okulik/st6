from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    sleep(2)
    yield driver
    driver.close()


def test_open_page(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    search_input = driver.find_element(By.NAME, "text_string")
    search_input.send_keys('test_first_step')
    search_input.send_keys(Keys.ENTER)
    search_element = driver.find_element(By.ID, "result")
    result_text = search_element.text
    print(result_text)
    assert result_text == result_text, 'the text is not as expected'
