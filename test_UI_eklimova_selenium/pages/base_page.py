from selenium.webdriver.remote.webdriver import WebDriver
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    related_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Open the page")
    def open(self):
        if self.related_url:
            self.driver.get(f"{self.base_url}{self.related_url}")
        else:
            raise NotImplementedError('Not possible to open the page')

    def scroll(self):
        self.driver.execute_script("window.scrollBy(0, 300);")
