from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import TIMEOUT_VALUE


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _load_page(self, page):
        self.driver.get(page)

    def _wait_for_element(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def _wait_for_element_clicked(self, locator, timeout=TIMEOUT_VALUE):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def _click_on_element(self, locator, timeout=TIMEOUT_VALUE):
        element = self._wait_for_element_clicked(locator, timeout)
        element.click()

    def _send_keys_to_input(self, locator, keys, timeout=TIMEOUT_VALUE):
        element = self._wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    def _get_element_text(self, locator, timeout=TIMEOUT_VALUE):
        element = self._wait_for_element(locator, timeout)
        return element.text
