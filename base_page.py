# Import statements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        # Store driver instance (likes browsers)
        self.driver = driver

        # Create WebDriverWait object with in 25 seconds timeout
        self.wait = WebDriverWait(driver, 25)

    def wait_for_element(self, locator):
        try:
            # Waits until element is visible on the page
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            # Raises the error if element is not found
            raise Exception(f"Element not visible: {locator}")

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def send_keys(self, locator, value):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(value)