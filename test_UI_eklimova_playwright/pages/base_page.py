from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    related_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Find element")
    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    @allure.step("Open the page")
    def open(self):
        if self.related_url:
            self.page.goto(f"{self.base_url}{self.related_url}")
        else:
            raise NotImplementedError('Not possible to open the page')

    def scroll(self):
        self.page.evaluate("window.scrollBy(0, 300);")
