from selenium.webdriver.common.by import By


class HomePage:
    SEARCH = (By.CSS_SELECTOR, '#search')
    BUTTON = (By.CSS_SELECTOR, '.action.more.button')


class SearchPage:
    NAMES = (By.CSS_SELECTOR, '.product-item-link')
