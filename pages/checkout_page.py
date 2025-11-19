import time

import generators
from locators.checkout_page_locators import CheckoutPageLocators
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def data_input(self):
        first_name, last_name, zip_code = generators.fake_data()
        self._send_keys_to_input(CheckoutPageLocators.FIRST_NAME, first_name)
        self._send_keys_to_input(CheckoutPageLocators.LAST_NAME, last_name)
        self._send_keys_to_input(CheckoutPageLocators.ZIP_CODE, zip_code)

    def click_on_continue_button(self):
        self._click_on_element(CheckoutPageLocators.CONTINUE_BUTTON)

    def get_total_price(self):
        return self._get_element_text(CheckoutPageLocators.TOTAL_PRICE)
