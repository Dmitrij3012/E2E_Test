import data
import url
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.shopping_cart_page import ShoppingCartPage


class TestUiE2e:

    def test_ui_e2e(self, driver):

        login_page = LoginPage(driver)
        login_page._load_page(url.LOGIN_URL)
        login_page.authorization(data.USERNAME, data.PASSWORD)

        main_page = MainPage(driver)
        main_page.adding_a_product_to_the_cart()
        main_page.click_on_shopping_cart()

        shopping_cart_page = ShoppingCartPage(driver)
        text = shopping_cart_page.return_product_name()

        assert text == 'Sauce Labs Backpack'

        shopping_cart_page.click_on_checkout_button()

        checkout_page = CheckoutPage(driver)
        checkout_page.data_input()
        checkout_page.click_on_continue_button()
        text = checkout_page.get_total_price()

        assert text == 'Total: $32.39'
