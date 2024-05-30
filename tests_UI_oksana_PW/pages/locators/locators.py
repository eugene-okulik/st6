
class CreatePageLocators:
    FIRST_NAME = '#firstname'
    LAST_NAME = '#lastname'
    PASSWORD = '#password'
    CONFIRM_PASSWORD = '#password-confirmation'
    EMAIL = '#email_address'
    SUBMIT_BUTTON = 'button[title="Create an Account"]'
    ERROR_MESSAGE = '[role="alert"]'
    EMAIL_ERROR_MESSAGE = '#email_address-error'


class ProductCheckerLocators:
    HOVER_ELEMENT = '(//*[@class="product-image-photo"])[2]'
    WISHLIST_BUTTON = '(//*[@aria-label="Add to Wish List"])[2]'
    LOGIN_MESSAGE = 'div.page.messages > div:nth-child(2) > div > div > div'
    SELECT_THIRD_PRODUCT = '(//*[@class="product-item-info"])[3]'
    COLOR_ERROR = '[for="super_attribute[93]"]'
    PRODUCT_SIZE = '#option-label-size-143-item-171'
    ADD_TO_CART = '#product-addtocart-button'
    SELECT_COLOR = '#option-label-color-93-item-52'
    PRODUCT_QUANTITY = '[name="qty"]'
    VERIFY_QUANTITY_ERROR_MESSAGE = '#qty-error'


class SaleProductLocators:
    SEARCH_INPUT = '#search'
    SEARCH_RESULT = "//div[@class='message notice']/div"
    BUTTON_MORE = '.more.button'
    PRODUCT_CLICK = '//*[@class="item product product-item"][2]'
    FIND_SHORTS = '(//a[text()="Shorts"])[1]'
    PRODUCT_IMAGE_PHOTO = ".product-image-photo"
    ADD_TO_CART_BUTTON = "//button[@title='Add to Cart']"
    IN_STOCK = '.stock.available'
