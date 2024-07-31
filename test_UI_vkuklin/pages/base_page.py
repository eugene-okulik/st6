import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    relative_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the page')
    def open(self):
        if self.relative_url:
            self.driver.get(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Not possible to open this page by URL')

    @allure.step('Find element')
    def find(self, locator):
        return self.driver.find_element(*locator)
