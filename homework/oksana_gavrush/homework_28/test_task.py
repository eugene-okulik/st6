from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1180)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_page_first(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    product_url = product.get_attribute('href')
    driver.execute_script(f"window.open('{product_url}');")
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    button = driver.find_element(By.XPATH, '//a[text()="Add to cart"]')
    button.click()
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(windows[0])
    cart = driver.find_element(By.CSS_SELECTOR, '#cartur')
    cart.click()
    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'page-wrapper'))
    )
    product_quantity = driver.find_element(By.XPATH, "//td[text()='Samsung galaxy s6']")
    assert product_quantity.text == 'Samsung galaxy s6'


def test_page_second(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    driver.execute_script("window.scrollBy(0, 300)")
    product = driver.find_element(By.CSS_SELECTOR, '.product-image-container')
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    compare = driver.find_element(By.XPATH, '(//*[@class="actions-secondary"])[1]//a[2]')
    actions.click(compare).perform()
    product = driver.find_element(By.CSS_SELECTOR, '[class="page messages"] >div >div > div >div')
    assert product.text == "You added product Push It Messenger Bag to the comparison list."


def test_page_third(driver):
    driver.get('https://www.qa-practice.com/elements/popup/iframe_popup')
    driver.find_element(By.CSS_SELECTOR, 'button[type="button"]').click()
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    text_find = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '#text-to-copy')))
    text = text_find.text
    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, 'button[form="empty-form"]').click()
    text_input = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, '[name="text_from_iframe"]'))
    )
    text_input.send_keys(text)
    submit = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')
    submit.click()
    result = driver.find_element(By.CSS_SELECTOR, '#check-result')
    assert result.text == 'Correct!'
