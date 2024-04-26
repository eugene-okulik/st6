from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

SAIT = "https://www.qa-practice.com/elements/input/simple"


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver


def test_open_page(driver):
    driver.get(SAIT)
    print(driver.current_url)
    print(driver.title)
    search_field = driver.find_element(By.ID, "id_text_string")
    search_field.send_keys("WellDone")
    search_field.send_keys(Keys.ENTER)
    expected_text = driver.find_element(By.ID, "result-text").text
    assert expected_text == "WellDone"

