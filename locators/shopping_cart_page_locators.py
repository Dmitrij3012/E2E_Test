from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:

    PRODUCT_NAME = (By.XPATH, "//div[@class='inventory_item_name']")

    CHECKOUT_BUTTON = (By.ID, 'checkout')

