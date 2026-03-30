import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """E2E test suite for login functionality."""

    def test_valid_login_redirects_to_inventory(self, login_page, users):
        """Verify valid credentials land on the products page."""
        login_page.goto()
        login_page.login(
            users['standard']['username'],
            users['standard']['password']
        )
        assert "/inventory" in login_page.get_current_url(), \
            "Expected redirect to inventory page after login"

    def test_valid_login_shows_products_title(self, page, login_page, users):
        """Verify products page title is visible after login."""
        login_page.goto()
        login_page.login(
            users['standard']['username'],
            users['standard']['password']
        )
        inventory = InventoryPage(page)
        assert inventory.get_page_title() == "Products"

    def test_invalid_login_shows_error(self, login_page, users):
        """Verify invalid credentials show an error message."""
        login_page.goto()
        login_page.login(
            users['invalid']['username'],
            users['invalid']['password']
        )
        assert login_page.is_error_visible(), "Error message should be visible"

    def test_invalid_login_error_message_content(self, login_page, users):
        """Verify error message text for invalid credentials."""
        login_page.goto()
        login_page.login(
            users['invalid']['username'],
            users['invalid']['password']
        )
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_locked_user_cannot_login(self, login_page, users):
        """Verify locked out user sees appropriate error."""
        login_page.goto()
        login_page.login(
            users['locked']['username'],
            users['locked']['password']
        )
        error = login_page.get_error_message()
        assert "locked out" in error.lower()

    def test_empty_username_shows_error(self, login_page):
        """Verify submitting empty username shows validation error."""
        login_page.goto()
        login_page.click_login()
        assert login_page.is_error_visible()
        assert "Username is required" in login_page.get_error_message()

    def test_empty_password_shows_error(self, login_page, users):
        """Verify submitting without password shows validation error."""
        login_page.goto()
        login_page.enter_username(users['standard']['username'])
        login_page.click_login()
        assert login_page.is_error_visible()
        assert "Password is required" in login_page.get_error_message()

    def test_logout_redirects_to_login(self, page, login_page, users):
        """Verify logout returns user to login page."""
        login_page.goto()
        login_page.login(
            users['standard']['username'],
            users['standard']['password']
        )
        inventory = InventoryPage(page)
        inventory.logout()
        assert login_page.get_current_url() == f"{login_page.base_url}/"
    
