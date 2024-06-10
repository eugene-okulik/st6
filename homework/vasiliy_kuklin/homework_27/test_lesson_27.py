from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_input = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
    dropdown = Select(select_input)
    dropdown.select_by_value(value="1")
    driver.find_element('css selector', '#submit-id-submit').click()
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == 'Python'


def test_internrt_herak(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    # button = driver.find_element(By.ID, 'start')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    result_text = driver.find_element(By.XPATH, "//div[@class='example']/div[@id='finish']/h4")
    assert result_text.text == 'Hello World!'
