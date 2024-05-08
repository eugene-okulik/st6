import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tests_UI_eokulik_selenium.pages.base_page import BasePage
from tests_UI_eokulik_selenium.pages.locators.locators import HomePage as loc


class HomePage(BasePage):
    relative_url = '/'

    @allure.step('Check that yoga button exists')
    def check_yoga_button(self):
        button = self.find(loc.BUTTON)
        assert button.is_displayed()

    @allure.step('enter text into search')
    def enter_text_into_search(self, text):
        search = self.find(loc.SEARCH)
        search.send_keys(text)
        search.submit()

    @allure.step('Perform search operation')
    def search_text(self, text):
        current_url = self.driver.current_url
        self.enter_text_into_search(text)
        WebDriverWait(self.driver, 3).until(ec.url_changes(current_url))
