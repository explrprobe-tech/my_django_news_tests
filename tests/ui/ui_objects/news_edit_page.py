from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent
from .news_page import NewsPage



class NewsEditPage(BasePage):
    """UI methods for News page"""

    def __init__(self, page: Page, base_url):
        import re
        super().__init__(page, base_url)
        self.headers = HeaderComponent(page)
        self.news = NewsPage(page, base_url)
        self.news_edit_url = re.compile(rf"{self.news.news_url.rstrip("/")}/\d+/edit/")

    def navigate(self):
        """Open News edit page"""
        self.news.navigate()
        self.news.first_news_edit_button.click()
        return self
    
    @property
    def news_edit_title(self):
        return self.page.locator(".container .edit-news-container h1")
    
    @property
    def news_title_title(self):
        return self.page.locator('.form-group label[for="id_title"]')
    
    @property
    def news_title_field(self):
        return self.page.locator("#id_title")
    
    @property
    def news_category_title(self):
        return self.page.locator('.form-group label[for="id_category"]')
    
    @property
    def news_category_field(self):
        return self.page.locator("#id_category")
    
    @property
    def news_short_description_title(self):
        return self.page.locator('.form-group label[for="id_short_description"]')
    
    @property
    def news_short_description_field(self):
        return self.page.locator("#id_short_description")
    
    @property
    def news_short_description_hint(self):
        return self.page.locator(".hint-text")
    
    @property
    def news_image_title(self):
        return self.page.locator(".current-image p")
    
    @property
    def news_image_delete_checkbox(self):
        return self.page.get_by_role("checkbox", name="Удалить изображение")
    
    @property
    def news_image_hint_upper(self):
        return self.page.locator('.form-group label[for="id_photo"]')
    
    @property
    def news_image_field(self):
        return self.page.locator("#id_photo")
    
    @property
    def news_image_hint_formats(self):
        return self.page.locator('.form-group:has(label[for="id_photo"]) .char-counter')
    
    @property
    def news_content_title(self):
        return self.page.locator('.form-group label[for="id_content"]')
    
    @property
    def news_content_field(self):
        return self.page.locator("#id_content")
    
    @property
    def news_public_checkbox(self):
        return self.page.get_by_role("checkbox", name="Опубликовано")
    
    @property
    def news_save_button(self):
        return self.page.get_by_role("button", name="💾 Сохранить изменения")
    
    @property
    def cancel_button(self):
        return self.page.get_by_role("link", name="❌ Отмена")

    def news_edit(self, test_news, test_category, news_data):
        """Edit news fields and save it"""
        test_news_url = test_news["test_news_url"].rstrip('/')
        test_news_edit_url = f"{test_news_url}/edit/"
        self._navigate_to(url=test_news_edit_url)
        self.news_title_field.fill(news_data["title"])
        self.news_category_field.select_option(test_category["test_category_id"])
        self.news_short_description_field.fill(news_data["short_description"])
        self.news_content_field.fill(news_data["content"])
        self.news_save_button.click()
        return self
