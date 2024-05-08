import allure
from tests_UI_eokulik_selenium.pages.base_page import BasePage
from tests_UI_eokulik_selenium.pages.locators.locators import SearchPage as loc


class SearchPage(BasePage):

    @allure.step('Check at least one name has searched word')
    def product_names_contain_text_(self, text):
        names = self.find_all(loc.NAMES)
        assert len(list(filter(lambda x: text in x.text.lower(), names))) > 0
