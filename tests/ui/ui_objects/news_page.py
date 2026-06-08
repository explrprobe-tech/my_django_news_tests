from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent



class NewsPage(BasePage):
    """UI methods for News page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.news_endpoint = "/news/"
        self.news_url = f"{self.base_url}{self.news_endpoint}"
        self.headers = HeaderComponent(page)


    def navigate(self):
        """Open News page"""
        self._navigate_to(endpoint=self.news_endpoint)
        return self
    
    @property
    def news_title(self):
        return self.page.locator(".page-title")
    
    @property
    def category_button(self):
        return self.page.get_by_role("link", name="Категории")
    
    @property
    def news_add_button(self):
        return self.page.get_by_role("link", name="✍️ Добавить новость")
    
    @property
    def first_news_card(self):
        return self.page.locator(".news-card").first
    
    @property
    def first_news_read_button(self):
        return self.page.get_by_role("link", name="Читать далее →").first
    
    @property
    def first_news_edit_button(self):
        return self.page.get_by_role("link", name="Редактировать новость").first