from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent



class NewsAddPage(BasePage):
    """UI methods for News add page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.news_add_endpoint = "/news/add_news/"
        self.news_add_url = f"{self.base_url}{self.news_add_endpoint}"
        self.headers = HeaderComponent(page)

    def navigate(self):
        """Open News add page"""
        self._navigate_to(endpoint=self.news_add_endpoint)
        return self
    
    @property
    def news_title_title(self):
        return self.page.locator("label[for='id_title']")
    
    @property
    def news_title_field(self):
        return self.page.locator("#id_title")
    
    @property
    def news_title_hint(self):
        return self.page.locator(".hint-text").nth(0)
    
    @property
    def news_category_title(self):
        return self.page.locator("label[for='id_category']")
    
    @property
    def news_category_field(self):
        return self.page.locator("#id_category")
    
    @property
    def news_category_hint(self):
        return self.page.locator(".hint-text").nth(1)
    
    @property
    def news_short_description_title(self):
        return self.page.locator("label[for='id_short_description']")
    
    @property
    def news_short_description_field(self):
        return self.page.locator("#id_short_description")
    
    @property
    def news_short_description_hint(self):
        return self.page.locator(".hint-text").nth(2)
    
    @property
    def news_content_title(self):
        return self.page.locator("label[for='id_content']")
    
    @property
    def news_content_field(self):
        return self.page.locator("#id_content")
    
    @property
    def news_content_hint(self):
        return self.page.locator(".hint-text").nth(3)
    
    @property
    def news_image_title(self):
        return self.page.locator("label[for='id_image']")
    
    @property
    def news_image_field(self):
        return self.page.locator("#id_image")
    
    @property
    def news_image_hint(self):
        return self.page.locator(".hint-text").nth(4)
    
    @property
    def news_tags_title(self):
        return self.page.locator("label[for='id_tags']")
    
    @property
    def news_tags_field(self):
        return self.page.locator("#id_tags")
    
    @property
    def news_tags_hint(self):
        return self.page.locator(".hint-text").nth(5)

    @property
    def news_add_button(self):
        return self.page.get_by_role("button", name="✨ Опубликовать новость")
    
    @property
    def cancel_button(self):
        return self.page.get_by_role("link", name="❌ Отмена")

    def news_add(self, news_data, test_category):
        """Create News with UI"""
        self.navigate()
        self.news_title_field.fill(news_data["title"])
        self.news_short_description_field.fill(news_data["short_description"])
        self.news_category_field.select_option(test_category["test_category_id"])
        self.news_content_field.fill(news_data["content"])
        self.news_image_field.set_input_files(news_data["photo"])
        self.news_tags_field.fill(news_data["tags"])
        self.news_add_button.click()
        return self