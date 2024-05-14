from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_UI_eklimova_selenium.pages.base_page import BasePage
from test_UI_eklimova_selenium.pages.locators import SalePage as loc
import allure


class SalePage(BasePage):
    related_url = "/sale.html"

    @allure.step("click on women's button")
    def click_on_womens_button(self):
        button = self.find(loc.WOMAN_BUTTON)
        button.click()

    @allure.step("check that page redirected women's page")
    def check_that_page_redirected_womens_page(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.WOMAN_PAGE))

    @allure.step("click on men's button")
    def click_on_men_button(self):
        self.scroll()
        button = self.find(loc.MAN_BUTTON)
        button.click()

    @allure.step("check that page redirected men's page")
    def check_that_page_redirected_mens_page(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.MAN_PAGE))

    @allure.step("click on luma's button")
    def click_on_luma_button(self):
        self.scroll()
        button = self.find(loc.LUMA_BUTTON)
        button.click()

    @allure.step("check that page redirected luma's page")
    def check_that_page_redirected_lumas_page(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc.LUMA_PAGE))
