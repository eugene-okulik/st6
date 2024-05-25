import allure
from tests_UI_eokulik_PW.pages.base_page import BasePage
from tests_UI_eokulik_PW.pages.locators.locators import SearchPage as loc


class SearchPage(BasePage):

    @allure.step('Check at least one name has searched word')
    def product_names_contain_text_(self, text):
        names = self.find(loc.NAMES).all()
        assert len(list(filter(lambda x: text in x.text_content().lower(), names))) > 0
