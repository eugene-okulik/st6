from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    relative_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open page')
    def open(self):
        if self.relative_url:
            self.page.goto(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Can\'t open page by given url')

    @allure.step('Find an element')
    def find_element(self, locator) -> Locator:
        return self.page.locator(locator)
