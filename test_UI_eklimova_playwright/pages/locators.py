class CreateNewAccountPage:
    FIRSTNAME = "//input[@id='firstname']"
    LASTNAME = "//input[@id='lastname']"
    EMAIL = "//input[@id='email_address']"
    PASSWORD = "//input[@id='password']"
    CONFIRMATION_PASSWORD = "//input[@id='password-confirmation']"
    BUTTON_CREATE = '//button[@class="action submit primary"]'
    PERSON_INFO = '//div[@class="box box-information"]/strong[@class="box-title"]'
    PERSON_INFO_VALUE = "//div[@class='box-content']/p"
    LASTNAME_WARNING_MES = '#lastname-error'
    PASSWORD_WARNING_MES = '//div[@id="password-confirmation-error"]'


class EcoFriendlyPage:
    SEARCHING = "#search"
    PURCHASE = '.product-item-link'
    ELEMENT = '(//div[@class="product-item-info"])[1]'
    ADD_TO_CART = "(//button[@class='action tocart primary'])[1]"
    SIZE_29 = "(//div[@id='option-label-size-143-item-172'])[1]"
    ORANGE_COLOR = "(//div[@id='option-label-color-93-item-56'])[1]"
    SUCCESS_ADDING_MES = '//div[@data-ui-id="message-success"]'
    ITEM_TITLE = "(//a[@class='product-item-link'])[1]"
    CART_LINK = '//div[@data-ui-id="message-success"]/div/a'
    ITEM_IN_CART = '(//div[@class="product-item-details"]/strong[@class="product-item-name"]/a)[2]'
    MES_NEED_TO_CHOOSE = '//div[@data-ui-id="message-notice"]/div'


class SalePage:
    WOMAN_BUTTON = '//span[@class="more button"]'
    MAN_BUTTON = '(//span[@class="content"]/span[@class="more icon"])[1]'
    LUMA_BUTTON = '(//span[@class="more icon"])[2]'
    WOMAN_PAGE = '//span[@data-ui-id="page-title-wrapper"]'
    MAN_PAGE = '//span[@data-ui-id="page-title-wrapper"]'
    LUMA_PAGE = '//span[@data-ui-id="page-title-wrapper"]'
