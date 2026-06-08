from playwright.async_api import Page

class HeaderComponent:
    """Header components on top of the page"""

    def __init__(self, page: Page):
        self.page = page

    @property
    def login_button(self):
        return self.page.get_by_role("link", name="🔐 Войти")
        
    @property
    def signup_button(self):
        return self.page.get_by_role("link", name="📝 Регистрация")
        
    @property
    def home_button(self):
        return self.page.get_by_role("link", name="🏠 Главная")

    @property
    def all_news_button(self):
        return self.page.get_by_role("link", name="📋 Все новости")

    @property
    def logout_button(self):
        return self.page.get_by_role("button", name="🚪 Выйти")

    @property
    def user_role_text(self):
        return self.page.locator(".user-role")

    @property
    def secret_button(self):
        return self.page.get_by_role("link", name="🔒 Секретная страница")