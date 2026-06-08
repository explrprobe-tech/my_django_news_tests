from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent
from .category_page import CategoryPage


class CategoryNewsPage(BasePage):
    """UI methods for Category news page"""

    def __init__(self, page: Page, base_url):
        import re
        super().__init__(page, base_url)
        self.headers = HeaderComponent(page)
        self.category = CategoryPage(page, base_url)
        self.category_news_url = re.compile(rf"{self.category.category_url.rstrip("/")}/\d+/")

    def navigate(self):
        """Open Category news list page"""
        self.category.navigate()
        self.category.first_category_read_button.click()
        return self
    
    @property
    def category_news_title(self):
        return self.page.locator(".page-title")
    
    @property
    def first_category_news_card(self):
        return self.page.locator(".news-card").first
    
    @property
    def first_category_news_read_button(self):
        return self.page.get_by_role("link", name="Читать далее →").first
    
    @property
    def first_category_news_edit_button(self):
        return self.page.get_by_role("link", name="Редактировать новость")
    
