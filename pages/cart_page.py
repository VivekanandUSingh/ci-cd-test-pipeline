from pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page object for the SauceDemo shopping cart page.
    """

    CART_ITEMS = ".cart_item"
    ITEM_NAMES = ".inventory_item_name"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING = "[data-test='continue-shopping']"
    REMOVE_BUTTON = "button[data-test^='remove']"

    def __init__(self, page):
        super().__init__(page)

    def get_cart_item_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def get_cart_item_names(self):
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    def click_continue_shopping(self):
        self.page.click(self.CONTINUE_SHOPPING)

    def remove_first_item(self):
        self.page.locator(self.REMOVE_BUTTON).first.click()

    def is_empty(self):
        return self.page.locator(self.CART_ITEMS).count() == 0
    
