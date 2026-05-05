# Import statements
import pytest
from ZenClass_POM_Automation.Pages.login_page import LoginPage
from ZenClass_POM_Automation.Utilities.config import Config


def test_successful_login(setup):
    # Create page object
    page = LoginPage(setup)
    page.load_page(Config.BASE_URL)
    page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    assert page.is_login_successful()


def test_unsuccessful_login(setup):
    page = LoginPage(setup)
    page.load_page(Config.BASE_URL)
    page.login(Config.INVALID_USERNAME, Config.INVALID_PASSWORD)

    assert page.is_login_failed()


def test_validate_input_fields(setup):
    page = LoginPage(setup)
    page.load_page(Config.BASE_URL)

    assert page.validate_input_fields()


def test_validate_login_button(setup):
    page = LoginPage(setup)
    page.load_page(Config.BASE_URL)

    assert page.validate_login_button()


def test_login_button_functionality(setup):
    page = LoginPage(setup)
    page.load_page(Config.BASE_URL)
    page.click(page.LOGIN_BTN)

    assert page.is_login_failed()