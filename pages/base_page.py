import yaml
import os


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


class BasePage:
    """
    Base class for all page objects.
    Provides shared utilities — navigation, waits, config access.
    """

    def __init__(self, page):
        self.page = page
        self.config = load_config()
        self.base_url = self.config['base_url']

    def navigate(self, path=""):
        self.page.goto(f"{self.base_url}{path}")

    def get_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.url

    def is_element_visible(self, selector):
        return self.page.is_visible(selector)

    def take_screenshot(self, name):
        os.makedirs("reports/screenshots", exist_ok=True)
        self.page.screenshot(path=f"reports/screenshots/{name}.png")
  
