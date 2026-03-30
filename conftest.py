import pytest
import yaml
import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture(scope="session")
def config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def users(config):
    return config['users']


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def logged_in(page, users):
    """Pre-authenticated session — skips login for tests that don't test auth."""
    login = LoginPage(page)
    login.goto()
    login.login(users['standard']['username'], users['standard']['password'])
    return page
