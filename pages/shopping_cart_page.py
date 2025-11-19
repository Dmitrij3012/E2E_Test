from locators.shopping_cart_page_locators import ShoppingCartPageLocators
from pages.base_page import BasePage


class ShoppingCartPage(BasePage):

    def return_product_name(self):
        return self._get_element_text(ShoppingCartPageLocators.PRODUCT_NAME)

    def click_on_checkout_button(self):
        self._wait_for_element_clicked(ShoppingCartPageLocators.CHECKOUT_BUTTON)
        self._click_on_element(ShoppingCartPageLocators.CHECKOUT_BUTTON)

