from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from st6.tests_UI_oksana_selenium.pages.create_account_page import CreateNewAccount
from st6.tests_UI_oksana_selenium.pages.eco_friendly_page import ProductChecker
from st6.tests_UI_oksana_selenium.pages.sale_page import SaleChecker


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
def create_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return ProductChecker(driver)


@pytest.fixture()
def sale_page(driver):
    return SaleChecker(driver)
