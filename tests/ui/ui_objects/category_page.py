from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent


class CategoryPage(BasePage):
    """UI methods for Category page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.category_endpoint = "/category/"
        self.category_url = f"{self.base_url}{self.category_endpoint}"
        self.headers = HeaderComponent(page)

    def navigate(self):
        """Open Category page"""
        self._navigate_to(endpoint=self.category_endpoint)
        return self
    
    @property
    def category_title(self):
        return self.page.locator(".page-title")
    
    @property
    def read_all_news_button(self):
        return self.page.get_by_role("link", name="📰 Читать все новости")
    
    @property
    def category_add_button(self):
        return self.page.get_by_role("link", name="✍️ Добавить категорию")
    
    @property
    def first_category_card(self):
        return self.page.locator(".news-card:first-child")
    
    @property
    def first_category_read_button(self):
        return self.page.locator(".edit-news-btn").first
    
