from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from time import sleep


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    # sleep(3)
    yield driver
    driver.quit()


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    burger = driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon')
    burger.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


def test_drop_menu(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    men = driver.find_element(By.CSS_SELECTOR, '#ui-id-5')
    tops = driver.find_element(By.CSS_SELECTOR, '#ui-id-17')
    jackets = driver.find_element(By.CSS_SELECTOR, '#ui-id-19')
    # ActionChains(driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(men)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    sleep(2)


def test_open_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    link = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(3)


def test_dnd(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = driver.find_element(By.ID, 'rect-draggable')
    drop_here = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(drag_me, drop_here).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(drag_me)
    actions.move_to_element(drop_here)
    actions.release()
    actions.perform()
    sleep(3)


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.CSS_SELECTOR, '.a-button').click()
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    sleep(5)
    alert = Alert(driver)
    assert alert.text == 'I am an alert!'
    alert.accept()
    sleep(3)


def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.CSS_SELECTOR, '#file-upload')
    upload.send_keys('/home/eugene/Downloads/hearts.jpg')
    sleep(3)
