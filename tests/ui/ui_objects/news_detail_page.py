from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent
from .news_page import NewsPage



class NewsDetailPage(BasePage):
    """UI methods for News detail page"""

    def __init__(self, page: Page, base_url):
        import re
        super().__init__(page, base_url)
        self.headers = HeaderComponent(page)
        self.news = NewsPage(page, base_url)
        self.news_detail_url = re.compile(fr"{self.news.news_url.rstrip("/")}/\d+/")


    def navigate(self):
        """Open News detail page"""
        self.news.navigate()
        self.news.first_news_read_button.click()
        return self
    
    @property
    def news_title(self):
        return self.page.locator(".news-detail-title")
    
    @property
    def news_public_date_text(self):
        return self.page.locator(".news-detail-meta span").nth(0)
    
    @property
    def news_category_button(self):
        return self.page.locator(".news-detail-meta span").nth(1)
    
    @property
    def news_count_views_text(self):
        return self.page.locator(".news-detail-meta span").nth(2)
    
    @property
    def news_author_text(self):
        return self.page.locator(".news-detail-meta span").nth(3)
    
    @property
    def news_image(self):
        return self.page.locator("img")
    
    @property
    def news_share_facebook_button(self):
        return self.page.locator(".share-buttons a.share-btn").nth(0)
    
    @property
    def news_share_twitter_button(self):
        return self.page.locator(".share-buttons a.share-btn").nth(1)
    
    @property
    def news_share_telegram_button(self):
        return self.page.locator(".share-buttons a.share-btn").nth(2)
    
    @property
    def news_share_link_button(self):
        return self.page.locator(".share-buttons a.share-btn").nth(3)
    
    @property
    def news_content(self):
        return self.page.locator(".news-detail-text p").nth(0)
    
    @property
    def back_news_button(self):
        return self.page.get_by_role("link", name="← Назад к списку новостей")
