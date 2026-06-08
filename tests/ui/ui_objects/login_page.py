from .base_page import BasePage
from .components.headers import HeaderComponent
from playwright.sync_api import Page


class LoginPage(BasePage):
    """Login component with login elements and methods"""
    
    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.login_endpoint = "/login/"
        self.login_url = f"{self.base_url}{self.login_endpoint}"
        self.headers = HeaderComponent(page)

    def navigate(self):
        self._navigate_to(endpoint=self.login_endpoint)
        return self
    
    @property
    def username_field(self):
        return self.page.locator("#id_username")
    
    @property
    def password_field(self):
        return self.page.locator("#id_password")
    
    @property
    def enter_button(self):
        return self.page.get_by_role("button", name="Войти")
    
    @property
    def back_home_button(self):
        return self.page.get_by_role("link", name="← На главную")
    
    @property
    def signup_button(self):
        return self.page.get_by_role("link", name="Зарегистрируйтесь здесь")
    
    @property
    def error_message_text(self):
        return self.page.locator(".alert.alert-error")

    def login(self, user_data):
        """Login by username and password"""
        self.navigate()
        self.username_field.fill(user_data["username"])
        self.password_field.fill(user_data["password"])
        self.enter_button.click()
        return self