from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    relative_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the registration page')
    def open(self):
        if self.relative_url:
            self.page.goto(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Page not open')

    @allure.step('Find element')
    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)
