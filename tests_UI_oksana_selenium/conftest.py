from selenium import webdriver
import pytest
from st6.tests_UI_oksana_selenium.pages.create_account_page import CreateNewAccount
from st6.tests_UI_oksana_selenium.pages.eco_friendly_page import ProductChecker
from st6.tests_UI_oksana_selenium.pages.sale_page import SaleChecker


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return ProductChecker(driver)


@pytest.fixture()
def sale_page(driver):
    return SaleChecker(driver)
