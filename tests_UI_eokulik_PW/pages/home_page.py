import allure
from playwright.sync_api import expect
from tests_UI_eokulik_PW.pages.base_page import BasePage
from tests_UI_eokulik_PW.pages.locators.locators import HomePage as loc


class HomePage(BasePage):
    relative_url = '/'

    @allure.step('Check that yoga button exists')
    def check_yoga_button(self):
        button = self.find(loc.BUTTON)
        expect(button).to_be_visible()

    @allure.step('enter text into search')
    def enter_text_into_search(self, text):
        search = self.find(loc.SEARCH)
        search.fill(text)
        search.press('Enter')

    @allure.step('Perform search operation')
    def search_text(self, text):
        current_url = self.page.url
        self.enter_text_into_search(text)
        expect(self.page).not_to_have_url(current_url)
