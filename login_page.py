# Import statements
from selenium.webdriver.common.by import By
from ZenClass_POM_Automation.Pages.base_page import BasePage
import time


class LoginPage(BasePage):

    # Locator for login form
    FORM = (By.TAG_NAME, "form")

    # Locator for Email input field
    EMAIL = (By.XPATH, "//input[@placeholder='Enter your mail']")

    # Locator for Password field
    PASSWORD = (By.XPATH, "//input[@type='password']")

    # Locator for Login button
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    def load_page(self, url):
        # Opens the given URL in browser
        self.driver.get(url)

        # Waits until login form is visible
        self.wait_for_element(self.FORM)

    def login(self, email, password):
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)
        time.sleep(3)

    # Checks login is success for using URL change
    def is_login_successful(self):
        # If 'login' is NOT in URL → login successful
        return "login" not in self.driver.current_url.lower()

    # Check login failure using URL
    def is_login_failed(self):
        # If still on login page → login failed
        return "login" in self.driver.current_url.lower()

    def validate_input_fields(self):
        # Check both email and password fields are visible
        return (
            self.wait_for_element(self.EMAIL).is_displayed()
            and self.wait_for_element(self.PASSWORD).is_displayed()
        )

    def validate_login_button(self):
        # Check login button is clickable/enabled
        return self.wait_for_clickable(self.LOGIN_BTN).is_enabled()