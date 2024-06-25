from selenium.webdriver.common.by import By


class CreateNewAccountPage:
    FIRSTNAME = (By.XPATH, "//input[@id='firstname']")
    LASTNAME = (By.XPATH, "//input[@id='lastname']")
    EMAIL = (By.XPATH, "//input[@id='email_address']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    CONFIRMATION_PASSWORD = (By.XPATH, "//input[@id='password-confirmation']")
    BUTTON_CREATE = (By.XPATH, '//button[@class="action submit primary"]')
    PERSON_INFO = (By.XPATH, '//div[@class="box box-information"]/strong[@class="box-title"]')
    PERSON_INFO_VALUE = (By.XPATH, "//div[@class='box-content']/p")
    LASTNAME_WARNING_MES = (By.XPATH, '//div[@id="lastname-error"]')
    PASSWORD_WARNING_MES = (By.XPATH, '//div[@id="password-confirmation-error"]')


class EcoFriendlyPage:
    SEARCHING = (By.ID, "search")
    PURCHASE = (By.CSS_SELECTOR, '.product-item-link')
    ELEMENT = (By.XPATH, '(//div[@class="product-item-info"])[1]')
    ADD_TO_CART = (By.XPATH, "(//button[@class='action tocart primary'])[1]")
    SIZE_29 = (By.XPATH, "(//div[@id='option-label-size-143-item-172'])[1]")
    ORANGE_COLOR = (By.XPATH, "(//div[@id='option-label-color-93-item-56'])[1]")
    SUCCESS_ADDING_MES = (By.XPATH, '//div[@data-ui-id="message-success"]')
    ITEM_TITLE = (By.XPATH, "(//a[@class='product-item-link'])[1]")
    CART_LINK = (By.XPATH, '//div[@data-ui-id="message-success"]/div/a')
    ITEM_IN_CART = (By.XPATH, '(//div[@class="product-item-details"]/strong[@class="product-item-name"]/a)[2]')
    MES_NEED_TO_CHOOSE = (By.XPATH, '//div[@data-ui-id="message-notice"]/div')


class SalePage:
    WOMAN_BUTTON = (By.XPATH, '//span[@class="more button"]')
    MAN_BUTTON = (By.XPATH, '(//span[@class="content"]/span[@class="more icon"])[1]')
    LUMA_BUTTON = (By.XPATH, '(//span[@class="more icon"])[2]')
    WOMAN_PAGE = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    MAN_PAGE = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    LUMA_PAGE = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
