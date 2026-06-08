from playwright.sync_api import Page

class BasePage:
    """Base class for all UI objects"""

    def __init__(self, page: Page, base_url):
        self.base_url = base_url.rstrip('/')
        self.page = page

    def _navigate_to(self, url = None, endpoint = None):
        """Private method for navigate to endpoint"""
        if url:
            navigate_url = url
        elif endpoint:
            navigate_url = f"{self.base_url}{endpoint}"
        self.page.goto(navigate_url)
        return self
    