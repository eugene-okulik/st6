from playwright.sync_api import expect
from test_UI_eklimova_playwright.pages.base_page import BasePage
from test_UI_eklimova_playwright.pages.locators import SalePage as loc
import allure


class SalePage(BasePage):
    related_url = "/sale.html"

    @allure.step("click on women's button")
    def click_on_womens_button(self):
        self.find(loc.WOMAN_BUTTON).click()

    @allure.step("check that page redirected women's page")
    def check_that_page_redirected_womens_page(self):
        woman_page = self.find(loc.WOMAN_PAGE)
        expect(woman_page).to_be_visible()

    @allure.step("click on men's button")
    def click_on_men_button(self):
        self.scroll()
        self.find(loc.MAN_BUTTON).click()

    @allure.step("check that page redirected men's page")
    def check_that_page_redirected_mens_page(self):
        expect(self.find(loc.MAN_PAGE)).to_be_visible()

    @allure.step("click on luma's button")
    def click_on_luma_button(self):
        self.scroll()
        self.find(loc.LUMA_BUTTON).click()

    @allure.step("check that page redirected luma's page")
    def check_that_page_redirected_lumas_page(self):
        expect(self.find(loc.LUMA_PAGE)).to_be_visible()
