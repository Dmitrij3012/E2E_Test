from selenium.webdriver.common.by import By


class CheckoutPageLocators:

    FIRST_NAME = (By.ID, 'first-name')

    LAST_NAME = (By.ID, 'last-name')

    ZIP_CODE = (By.ID, 'postal-code')

    CONTINUE_BUTTON = (By.ID, 'continue')

    TOTAL_PRICE = (By.XPATH, "//div[@class='summary_total_label']")
