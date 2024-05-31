import allure
from test_UI_volha_playwrite.pages.base_page import BasePage
from playwright.sync_api import expect
from test_UI_volha_playwrite.pages.locators.locators import EcoFriendly as loc


class EcoFriendlyPage(BasePage):
    relative_url = '/collections/eco-friendly.html'
    eco_friendly = 'Eco Friendly'

    @allure.step('Check eco page title')
    def check_page_title_is_eco(self):
        title = self.find_element(loc.PAGETITLE)
        expect(title).to_have_text(self.eco_friendly)

    @allure.step('Check eco page category')
    def check_page_category_is_eco(self):
        category = self.find_element(loc.PAGECATEGORY)
        expect(category).to_have_text(self.eco_friendly)

    @allure.step('Check default number of items on page')
    def check_default_number_of_items(self):
        default_items = self.find_element(loc.DEFAULTNUMOFITEMS)
        assert default_items.count() == 12
