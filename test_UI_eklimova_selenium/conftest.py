from selenium import webdriver
from test_UI_eklimova_selenium.pages.create_new_account_page import CreateNewAccount
from test_UI_eklimova_selenium.pages.eco_frienfly_page import EcoFriendlyPage
from test_UI_eklimova_selenium.pages.sale_page import SalePage
import pytest
import json


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def create_new_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture
def creds():
    with open('creds.json') as f:
        return json.load(f)
