from .base_page import BasePage
from playwright.sync_api import Page
from .components.headers import HeaderComponent

class RegisterPage(BasePage):
    """UI methods for Register Page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.register_endpoint = "/register/"
        self.register_url = f"{self.base_url}{self.register_endpoint}"
        self.headers = HeaderComponent(page)

    def navigate(self):
        self._navigate_to(endpoint=self.register_endpoint)
        return self

    @property
    def username_field(self):
        return self.page.locator("#id_username")
    
    @property
    def email_field(self):
        return self.page.locator("#id_email")
    
    @property
    def password1_field(self):
        return self.page.locator("#id_password1")
    
    @property
    def password2_field(self):
        return self.page.locator("#id_password2")
    
    @property
    def register_button(self):
        return self.page.get_by_role("button", name="Зарегистрироваться")
    
    @property
    def login_button(self):
        return self.page.get_by_role("link", name="Войдите здесь")
    
    @property
    def back_home_button(self):
        return self.page.get_by_role("link", name="← На главную")
    
    @property
    def username_error_text(self):
        return self.page.locator("#id_username_error")
    
    @property
    def email_error_text(self):
        return self.page.locator("#id_email_error")
    
    @property
    def password1_error_text(self):
        return self.page.locator("#id_password1_error")
    
    @property
    def password2_error_text(self):
        return self.page.locator("#id_password2_error")
    
    def register(self, user_data):
        """Register user by username, email, password1 and password2"""
        self.navigate()
        self.username_field.fill(user_data["username"])
        self.email_field.fill(user_data["email"])
        self.password1_field.fill(user_data["password1"])
        self.password2_field.fill(user_data["password2"])
        self.register_button.click()
        return self