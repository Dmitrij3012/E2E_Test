from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def authorization(self, username, password):
        self._send_keys_to_input(LoginPageLocators.USERNAME_FIELD, username)
        self._send_keys_to_input(LoginPageLocators.PASSWORD_FIELD, password)
        self._click_on_element(LoginPageLocators.LOGIN_BUTTON)
