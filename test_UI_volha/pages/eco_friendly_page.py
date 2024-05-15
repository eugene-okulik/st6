import allure
from test_UI_volha.pages.base_page import BasePage
from test_UI_volha.pages.locators.locators import EcoFriendly as loc


class EcoFriendlyPage(BasePage):
    relative_url = '/collections/eco-friendly.html'

    @allure.step('Check eco page title')
    def check_page_title_is_eco(self):
        title = self.find_element(loc.PAGETITLE)
        assert title.text == 'Eco Friendly'

    @allure.step('Check eco page category')
    def check_page_category_is_eco(self):
        category = self.find_element(loc.PAGECATEGORY)
        assert category.text == 'Eco Friendly'

    @allure.step('Check default number of items on page')
    def check_default_number_of_items(self):
        default_items = self.find_elements(loc.DEFAULTNUMOFITEMS)
        assert len(default_items) == 12
