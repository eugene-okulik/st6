from selenium.webdriver.common.by import By


class CreatePage:
    FIRST_NAME = '#firstname'
    LAST_NAME = '#lastname'
    EMAIL_ADDRESS = '#email_address'
    PASSWORD = '#password'
    CONFIRM_PASSWORD = '#password-confirmation'
    BUTTON_CREATE = '//*[@class="primary"]//button[@type="submit"]//*[text()="Create an Account"]'
    ERROR_FIRST_NAME = '#firstname-error'
    ERROR_LAST_NAME = '#lastname-error'
    ERROR_EMAIL_ADDRESS = '#email_address-error'
    ERROR_PASSWORD = '#password-error'
    ERROR_CONFIRM_PASSWORD = '#password-confirmation-error'
    HEADER_MY_ACCOUNT = '//h1[@class="page-title"]'
    EMAIL_ADDRESS_ERROR = '#email_address-error'


class EcoFriendlyPage:
    HEADER_ECO_FRIENDLY = '#page-title-heading'
    IMAGES_CARDS = '.product-image-wrapper'
    STARS_RATING = '.rating-result'


class SalePage:
    HEADER_SALE = '#page-title-heading'
    IMG_PROMO = '.blocks-promo'
    MY_WISH_LIST = '//*[contains(text(), "My Wish List")]'
