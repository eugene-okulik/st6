from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_UI_vkuklin.pages.create_page import CreatePage
from test_UI_vkuklin.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_vkuklin.pages.sale_page import SalePage
# from st6.test_UI_vkuklin.pages.create_page import CreatePage
# from st6.test_UI_vkuklin.pages.eco_friendly_page import EcoFriendlyPage
# from st6.test_UI_vkuklin.pages.sale_page import SalePage
import pytest


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
def create_page(driver):
    return CreatePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
