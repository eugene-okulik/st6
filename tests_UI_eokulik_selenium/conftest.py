from selenium import webdriver
import pytest
from tests_UI_eokulik_selenium.pages.home_page import HomePage
from tests_UI_eokulik_selenium.pages.search_page import SearchPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def search_page(driver):
    return SearchPage(driver)
