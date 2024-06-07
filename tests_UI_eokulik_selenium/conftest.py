from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from tests_UI_eokulik_selenium.pages.home_page import HomePage
from tests_UI_eokulik_selenium.pages.search_page import SearchPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def search_page(driver):
    return SearchPage(driver)
