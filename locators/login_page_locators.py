from selenium.webdriver.common.by import By


class LoginPageLocators:

    USERNAME_FIELD = (By.ID, 'user-name')

    PASSWORD_FIELD = (By.ID, 'password')

    LOGIN_BUTTON = (By.ID, 'login-button')

