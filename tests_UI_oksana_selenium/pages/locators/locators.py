from selenium.webdriver.common.by import By


class CreatePageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#lastname')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#password-confirmation')
    EMAIL = (By.CSS_SELECTOR, '#email_address')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[class="page messages"] >div>div>div>div')


class ProductCheckerLocators:
    HOVER_ELEMENT = (By.XPATH, '(//*[@class="product-image-photo"])[2]')
    WISHLIST_BUTTON = (By.XPATH, '(//*[@aria-label="Add to Wish List"])[2]')
    LOGIN_MESSAGE = (By.CSS_SELECTOR, '[class="page messages"] > div > div > div > div')
    SELECT_THIRD_PRODUCT = (By.XPATH, '(//*[@class="product-item-info"])[3]')
    PRODUCT_SIZE = (By.CSS_SELECTOR, '#option-label-size-143-item-171')
    ADD_TO_CART = (By.CSS_SELECTOR, '#product-addtocart-button')
    SELECT_COLOR = (By.CSS_SELECTOR, '#option-label-color-93-item-52')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, '[name="qty"]')
    VERIFY_QUANTITY_ERROR_MESSAGE = (By.CSS_SELECTOR, '#qty-error')


class SaleProductLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search')
    SEARCH_RESULT = (By.XPATH, "//div[@class='message notice']/div")
    BUTTON_MORE = (By.CSS_SELECTOR, '.more.button')
    PRODUCT_CLICK = (By.XPATH, '//*[@class="item product product-item"][2]')
    FIND_SHORTS = (By.LINK_TEXT, 'Shorts')
    PRODUCT_IMAGE_PHOTO = (By.CSS_SELECTOR, ".product-image-photo")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@title='Add to Cart']")
    IN_STOCK = (By.CSS_SELECTOR, '.stock.available')
