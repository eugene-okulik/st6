from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com/'
    relative_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the registration page')
    def open(self):
        if self.relative_url:
            self.driver.get(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Page not open')

    @allure.step('Find element')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Find oll element')
    def find_all(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Scroll pages')
    def scroll_down(self):
        return self.driver.execute_script("window.scrollBy(0, 500);")
