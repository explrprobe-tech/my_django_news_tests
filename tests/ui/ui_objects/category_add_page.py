from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent


class CategoryAddPage(BasePage):
    """UI methods for Category add page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.category_add_endpoint = "/category/add_category/"
        self.category_add_url = f"{self.base_url}{self.category_add_endpoint}"
        self.headers = HeaderComponent(page)

    def navigate(self):
        self._navigate_to(endpoint=self.category_add_endpoint)
        return self

    @property
    def title_field(self):
        return self.page.locator("#id_title")
    
    @property
    def category_add_button(self):
        return self.page.get_by_role("button", name="✨ Добавить категорию")
    
    @property
    def cancel_button(self):
        return self.page.get_by_role("link", name="❌ Отмена")
    
    def category_add(self, category_data):
        """Create category by title"""
        self.navigate()
        self.title_field.fill(category_data["title"])
        self.category_add_button.click()
        return self