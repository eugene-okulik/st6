from selenium import webdriver
import pytest
from test_UI_volha.pages.register_page import RegisterPage
from test_UI_volha.pages.account_page import AccountPage
from test_UI_volha.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_volha.pages.sale_page import SalePage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def register_page(driver):
    return RegisterPage(driver)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def eco_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
