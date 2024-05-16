from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    relative_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open page')
    def open(self):
        if self.relative_url:
            self.driver.get(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Can\'t open page by given url')

    @allure.step('Find an element')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Find all page elements')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
