from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    # def test_transit_to_main_page(self):
    #     return self._get_element_text(MainPageLocators.LOGO_TEXT)

    def adding_a_product_to_the_cart(self):
        self._click_on_element(MainPageLocators.PRODUCT)

    def click_on_shopping_cart(self):
        self._click_on_element(MainPageLocators.SHOPPING_CART)

