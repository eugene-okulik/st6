import allure
from test_UI_volha_playwrite.pages.base_page import BasePage
from playwright.sync_api import expect
from test_UI_volha_playwrite.pages.locators.locators import Sale as loc


class SalePage(BasePage):
    relative_url = '/sale.html'

    @allure.step('Check sale page title')
    def check_page_title_is_sale(self):
        title = self.find_element(loc.PAGETITLE)
        expect(title).to_have_text('Sale')

    @allure.step('Check sale page category')
    def check_page_category_is_sale(self):
        category = self.find_element(loc.PAGECATEGORY)
        expect(category).to_have_text('Sale')

    @allure.step('Check menu categories')
    def check_menu_categories(self):
        cat1 = self.find_element(loc.CATEGORYMENU1)
        cat2 = self.find_element(loc.CATEGORYMENU2)
        cat3 = self.find_element(loc.CATEGORYMENU3)
        expect(cat1).to_be_visible()
        expect(cat2).to_be_visible()
        expect(cat3).to_be_visible()
