# Import statements
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup():
    # Create Chrome options
    options = webdriver.ChromeOptions()

    # Open browser in maximized mode
    options.add_argument("--start-maximized")

    # Launch Chrome browser
    driver = webdriver.Chrome(options=options)

    # Implicit wait (fallback)
    driver.implicitly_wait(5)

    # Provide driver to test
    yield driver

    # Close browser after test
    driver.quit()