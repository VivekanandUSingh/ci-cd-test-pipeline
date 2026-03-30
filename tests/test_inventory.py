import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestInventory:
    """E2E test suite for product inventory page."""

    def test_inventory_displays_six_products(self, logged_in):
        """Verify exactly 6 products are displayed."""
        inventory = InventoryPage(logged_in)
        assert inventory.get_inventory_count() == 6, \
            f"Expected 6 products but got {inventory.get_inventory_count()}"

    def test_inventory_page_title(self, logged_in):
        """Verify page title shows 'Products'."""
        inventory = InventoryPage(logged_in)
        assert inventory.get_page_title() == "Products"

    def test_all_products_have_names(self, logged_in):
        """Verify all products have non-empty names."""
        inventory = InventoryPage(logged_in)
        names = inventory.get_all_product_names()
        assert len(names) == 6
        for name in names:
            assert len(name) > 0, f"Product name should not be empty"

    def test_all_products_have_positive_prices(self, logged_in):
        """Verify all product prices are positive numbers."""
        inventory = InventoryPage(logged_in)
        prices = inventory.get_all_product_prices()
        for price in prices:
            assert price > 0, f"Price {price} should be positive"

    def test_add_item_to_cart_updates_badge(self, logged_in):
        """Verify cart badge increments when item is added."""
        inventory = InventoryPage(logged_in)
        assert inventory.get_cart_count() == 0
        inventory.add_first_item_to_cart()
        assert inventory.get_cart_count() == 1

    def test_sort_products_low_to_high(self, logged_in):
        """Verify low-to-high sort returns ascending prices."""
        inventory = InventoryPage(logged_in)
        inventory.sort_products("lohi")
        prices = inventory.get_all_product_prices()
        assert prices == sorted(prices), \
            f"Prices not in ascending order: {prices}"

    def test_sort_products_high_to_low(self, logged_in):
        """Verify high-to-low sort returns descending prices."""
        inventory = InventoryPage(logged_in)
        inventory.sort_products("hilo")
        prices = inventory.get_all_product_prices()
        assert prices == sorted(prices, reverse=True), \
            f"Prices not in descending order: {prices}"

    def test_sort_products_alphabetical(self, logged_in):
        """Verify A-Z sort returns alphabetically ordered products."""
        inventory = InventoryPage(logged_in)
        inventory.sort_products("az")
        names = inventory.get_all_product_names()
        assert names == sorted(names), \
            f"Products not in alphabetical order: {names}"


class TestCart:
    """E2E test suite for shopping cart functionality."""

    def test_navigate_to_cart(self, logged_in):
        """Verify clicking cart icon navigates to cart page."""
        inventory = InventoryPage(logged_in)
        inventory.go_to_cart()
        assert "/cart" in logged_in.url

    def test_added_item_appears_in_cart(self, logged_in):
        """Verify item added from inventory appears in cart."""
        inventory = InventoryPage(logged_in)
        names_before = inventory.get_all_product_names()
        first_product = names_before[0]
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart = CartPage(logged_in)
        cart_names = cart.get_cart_item_names()
        assert first_product in cart_names

    def test_cart_item_count_matches(self, logged_in):
        """Verify cart page item count matches badge count."""
        inventory = InventoryPage(logged_in)
        inventory.add_first_item_to_cart()
        badge_count = inventory.get_cart_count()
        inventory.go_to_cart()
        cart = CartPage(logged_in)
        assert cart.get_cart_item_count() == badge_count

    def test_remove_item_from_cart(self, logged_in):
        """Verify removing item from cart empties the cart."""
        inventory = InventoryPage(logged_in)
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart = CartPage(logged_in)
        cart.remove_first_item()
        assert cart.is_empty(), "Cart should be empty after removing item"
    
