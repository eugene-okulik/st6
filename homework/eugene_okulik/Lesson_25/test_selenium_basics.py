from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    sleep(3)

    yield driver
    driver.close()


def test_open_page(driver):
    driver.maximize_window()
    driver.get('https://google.com')
    print(driver.current_url)
    print(driver.title)
    search_field = driver.find_element(By.NAME, 'q')
    search_field.send_keys('cat')
    search_field.send_keys(Keys.ENTER)
    # search_field.submit()
    assert driver.title.startswith('cat')


def test_header(driver):
    driver.get('https://www.qa-practice.com/')
    header = driver.find_element(By.TAG_NAME, 'h1')
    assert header.text == 'Hello!'


def test_contact(driver):
    driver.maximize_window()
    driver.get('https://www.qa-practice.com/')
    contact_link = driver.find_element(By.LINK_TEXT, 'Contact')
    # assert contact_link.get_attribute('href') == '/contact/'
    contact_link.click()
    sleep(2)
