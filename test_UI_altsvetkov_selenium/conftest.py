import pytest
from selenium import webdriver

from test_UI_altsvetkov_selenium.pages.create_account_page import CreateAccountPage
from test_UI_altsvetkov_selenium.pages.eco_friendly_collection_page import EcoCollectionPage
from test_UI_altsvetkov_selenium.pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def eco_collection_page(driver):
    return EcoCollectionPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
