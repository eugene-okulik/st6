from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


def test1(driver):

    driver.get('https://www.demoblaze.com/index.html')

    # откройте товар в новой вкладке
    phones = driver.find_elements(By.ID, 'tbodyid')
    phone1_link = phones[0].find_element(By.TAG_NAME, 'a')
    phone1_name = phones[0].find_element(By.CLASS_NAME, 'card-title').get_attribute('textContent')

    ActionChains(driver).key_down(Keys.CONTROL).click(phone1_link).key_up(Keys.CONTROL).perform()

    # Перейдите на вкладку с товаром
    initial, new_tab = driver.window_handles
    driver.switch_to.window(new_tab)

    # Добавьте товар в корзину
    wait = WebDriverWait(driver, 10)
    add_to_card_btn = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Add to cart')))
    add_to_card_btn.click()
    # закрываем алерт
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    # Закройте вкладку с товаром
    driver.close()
    # Переключаемся на первоначальную вкладку
    driver.switch_to.window(initial)

    # На начальной вкладке откройте корзину
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # Убедитесь, что в корзине тот товар, который вы добавляли
    (WebDriverWait(driver, 6).
     until(ec.element_to_be_clickable(driver.find_element(By.LINK_TEXT, 'Delete'))))
    cart_item1 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]").get_attribute('outerText')

    assert cart_item1 == phone1_name


def test2(driver):
    driver.maximize_window()
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    driver.execute_script("window.scrollBy(0, 320)")
    products = driver.find_elements(By.CSS_SELECTOR, '.item.product.product-item')
    actions = ActionChains(driver)
    actions.move_to_element(products[0])
    compare = driver.find_element(By.XPATH, '//*[@title="Add to Compare"][1]')
    actions.click(compare).perform()
    wait = WebDriverWait(driver, 5)
    wait.until(ec.text_to_be_present_in_element
               ((By.CSS_SELECTOR, '.product-item-name a'),
                'Push It Messenger Bag'))


def test3(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    driver.find_element(By.XPATH, '//*[@type="button"][1]').click()
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    copy_text = driver.find_element(By.CSS_SELECTOR, '#text-to-copy').text
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, '#id_text_from_iframe').send_keys(copy_text)
    driver.find_element(By.CSS_SELECTOR, '#submit-id-submit').click()
    result = driver.find_element(By.CSS_SELECTOR, '#check-result').get_attribute('outerText')
    assert result == 'Correct!'
