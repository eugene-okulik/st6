import allure
from test_UI_volha.pages.base_page import BasePage
from test_UI_volha.pages.locators.locators import Sale as loc


class SalePage(BasePage):
    relative_url = '/sale.html'

    @allure.step('Check sale page title')
    def check_page_title_is_sale(self):
        title = self.find_element(loc.PAGETITLE)
        assert title.text == 'Sale'

    @allure.step('Check sale page category')
    def check_page_category_is_sale(self):
        category = self.find_element(loc.PAGECATEGORY)
        assert category.get_attribute('outerText') == "Sale"

    @allure.step('Check menu categories')
    def check_menu_categories(self):
        cat1 = self.find_element(loc.CATEGORYMENU1)
        cat2 = self.find_element(loc.CATEGORYMENU2)
        cat3 = self.find_element(loc.CATEGORYMENU3)
        assert cat1.get_attribute('outerText') == "WOMEN'S DEALS"
        assert cat2.get_attribute('outerText') == "MENS'S DEALS"
        assert cat3.get_attribute('outerText') == "GEAR DEALS"
