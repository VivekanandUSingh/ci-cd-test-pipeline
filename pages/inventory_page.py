from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page object for the SauceDemo products/inventory page.
    Encapsulates product listing, sorting, and cart interactions.
    """

    PAGE_TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_PRICES = ".inventory_item_price"
    ADD_TO_CART_BUTTON = "button[data-test^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def __init__(self, page):
        super().__init__(page)

    def get_page_title(self):
        return self.page.inner_text(self.PAGE_TITLE)

    def get_inventory_count(self):
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_all_product_names(self):
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_all_product_prices(self):
        prices = self.page.locator(self.ITEM_PRICES).all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]

    def add_first_item_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

    def add_all_items_to_cart(self):
        buttons = self.page.locator(self.ADD_TO_CART_BUTTON)
        for i in range(buttons.count()):
            buttons.nth(i).click()

    def get_cart_count(self):
        badge = self.page.locator(self.CART_BADGE)
        if badge.is_visible():
            return int(badge.inner_text())
        return 0

    def go_to_cart(self):
        self.page.click(self.CART_LINK)

    def sort_products(self, option):
        """Sort options: 'az', 'za', 'lohi', 'hilo'"""
        self.page.select_option(self.SORT_DROPDOWN, option)

    def logout(self):
        self.page.click(self.BURGER_MENU)
        self.page.click(self.LOGOUT_LINK)
    
