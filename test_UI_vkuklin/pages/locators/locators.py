from selenium.webdriver.common.by import By


class CreatePage:
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    EMAIL_ADDRESS = (By.ID, 'email_address')
    PASSWORD = (By.ID, 'password')
    CONFIRM_PASSWORD = (By.ID, 'password-confirmation')
    BUTTON_CREATE = (By.XPATH, '//*[@class="primary"]//button[@type="submit"]//*[text()="Create an Account"]')
    ERROR_FIRST_NAME = (By.ID, 'firstname-error')
    ERROR_LAST_NAME = (By.ID, 'lastname-error')
    ERROR_EMAIL_ADDRESS = (By.ID, 'email_address-error')
    ERROR_PASSWORD = (By.ID, 'password-error')
    ERROR_CONFIRM_PASSWORD = (By.ID, 'password-confirmation-error')
    HEADER_MY_ACCOUNT = (By.XPATH, '//h1[@class="page-title"]')
    EMAIL_ADDRESS_ERROR = (By.ID, 'email_address-error')


class EcoFriendlyPage:
    HEADER_ECO_FRIENDLY = (By.ID, 'page-title-heading')
    IMAGES_CARDS = (By.CLASS_NAME, 'product-image-wrapper')
    STARS_RATING = (By.CLASS_NAME, 'rating-result')


class SalePage:
    HEADER_SALE = (By.ID, 'page-title-heading')
    IMG_PROMO = (By.CLASS_NAME, 'blocks-promo')
    MY_WISH_LIST = (By.XPATH, '//*[contains(text(), "My Wish List")]')
