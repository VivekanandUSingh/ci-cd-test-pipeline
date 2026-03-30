from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Page object for the SauceDemo login page.
    Encapsulates all login-related locators and actions.
    """

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self.navigate("/")

    def enter_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.page.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.page.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Full login action — enter credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.page.inner_text(self.ERROR_MESSAGE)

    def is_error_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)
    
