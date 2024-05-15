import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    base_url = 'https://magento.softwaretestingboard.com'
    relative_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, 5)

    @allure.step('Open the page')
    def open(self):
        if self.relative_url:
            self.driver.get(f'{self.base_url}{self.relative_url}')
        else:
            raise NotImplementedError('Not possible to open this page by URL')

    @allure.step('Find element')
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Find elements')
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Scroll down')
    def scroll_down(self):
        return self.driver.execute_script("window.scrollBy(0, 300);")
