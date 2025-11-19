from selenium.webdriver.common.by import By


class MainPageLocators:

    LOGO_TEXT = (By.XPATH, "//div[contains(text(), 'Swag Labs')]")

    PRODUCT = (By.ID, 'add-to-cart-sauce-labs-backpack')

    REMOVE_PRODUCT_TEXT = (By.ID, 'remove-sauce-labs-backpack')

    SHOPPING_CART = (By.XPATH, "//a[@class='shopping_cart_link']")