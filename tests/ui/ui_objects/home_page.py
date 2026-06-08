from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent


class HomePage(BasePage):
    """UI methods for Home page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.home_page_endpoint = "/"
        self.home_page_url = f"{self.base_url}{self.home_page_endpoint}"
        self.headers = HeaderComponent(page)
    
    def navigate(self):
        """Navigate to Home page"""
        self._navigate_to(endpoint=self.home_page_endpoint)
        return self

    @property
    def categories_button(self):
        return self.page.get_by_role("link", name="Категории")
    
    @property
    def read_news_button(self):
        return self.page.get_by_role("link", name="📰 Читать все новости")
    
    @property
    def add_news_button(self):
        return self.page.get_by_role("link", name="✍️ Добавить новость")
    
    @property
    def first_news_card(self):
        return self.page.locator(".news-grid .news-card:nth-child(1)")
    
    @property
    def second_news_card(self):
        return self.page.locator(".news-grid .news-card:nth-child(2)")
    
    @property
    def third_news_card(self):
        return self.page.locator(".news-grid .news-card:nth-child(3)")