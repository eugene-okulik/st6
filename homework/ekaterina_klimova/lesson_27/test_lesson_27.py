from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

SAIT = "https://www.qa-practice.com/elements/select/single_select"
SAIT2 = "https://the-internet.herokuapp.com/dynamic_loading/2"


class TestUI:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()

    def test_choose_language(self, driver):
        driver.get(SAIT)
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located((By.ID, "id_choose_language")))

        select_element = driver.find_element(By.ID, "id_choose_language")
        select = Select(select_element)
        select.select_by_value("1")
        wait.until(
            EC.text_to_be_present_in_element_value((By.ID, "id_choose_language"), "1"))

        submit_button = driver.find_element(By.ID, "submit-id-submit")
        submit_button.click()

        result = wait.until(EC.visibility_of_element_located((By.ID, "result-text")))
        result_text = result.text

        assert result_text == "Python"

    def test_start(self, driver):
        driver.get(SAIT2)
        wait = WebDriverWait(driver, 10)

        start_button = driver.find_element(By.CSS_SELECTOR, "#start>button")
        start_button.click()

        text = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        result_text = text.text

        assert result_text == "Hello World!"
