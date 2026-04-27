import pytest
from playwright.sync_api import Page, expect
from helpers import get_object_id_by_name, object_delete

def test_registration_valid(page: Page, base_url: str, admin_session, user_data: dict):
    """User can regist on register page"""
    page.goto(base_url)
    page.get_by_role("link", name="📝 Регистрация").click()
    page.locator("#id_username").fill(user_data["username"])
    page.locator("#id_email").fill(user_data["email"])
    page.locator("#id_password1").fill(user_data["password1"])
    page.locator("#id_password2").fill(user_data["password2"])
    page.get_by_role("button", name="Зарегистрироваться").click()
    expect(page).to_have_url(base_url)
    expect(page.get_by_text("Привет, test_autouser_ui!")).to_be_visible()
    expect(page.get_by_role("button", name="🚪 Выйти")).to_be_visible()
    expect(page.get_by_role("link", name="🔐 Войти")).not_to_be_visible()
    expect(page.get_by_role("link", name="🔒 Секретная страница")).not_to_be_visible()
    expect(page.get_by_text("(Обычные пользователи)")).to_be_visible()
    expect(page.get_by_role("link", name="✍️ Добавить новость")).not_to_be_visible()
    expect(page.get_by_role("link", name="Категории")).to_be_visible()
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    user_path = get_object_id_by_name(session=admin_session, base_url=base_url, model="user", name=user_data["username"])
    url_object = f"{base_url}{user_path}"
    print(url_object)
    object_delete(session=admin_session, url_object=url_object)
    
def test_registration_invalid_username(page: Page, base_url: str, user_data: dict):
    """User can't register without username"""
    user_data["username"] = " "
    page.goto(base_url)
    page.get_by_role("link", name="📝 Регистрация").click()
    page.locator("#id_username").fill(user_data["username"])
    page.locator("#id_email").fill(user_data["email"])
    page.locator("#id_password1").fill(user_data["password1"])
    page.locator("#id_password2").fill(user_data["password2"])
    page.get_by_role("button", name="Зарегистрироваться").click()
    expect(page.locator("#id_username_error")).to_be_visible()

def test_registration_username_and_password_similar(page: Page, base_url: str, user_data: dict):
    """User can't register with similar username and password"""
    user_data["password1"] = user_data["username"]
    user_data["password2"] = user_data["username"]
    page.goto(base_url)
    page.get_by_role("link", name="📝 Регистрация").click()
    page.locator("#id_username").fill(user_data["username"])
    page.locator("#id_email").fill(user_data["email"])
    page.locator("#id_password1").fill(user_data["password1"])
    page.locator("#id_password2").fill(user_data["password2"])
    page.get_by_role("button", name="Зарегистрироваться").click()
    expect(page.locator("#id_password2_error")).to_be_visible()

def test_registration_passwords_not_match(page: Page, base_url: str, user_data: dict):
    """User can't register with similar username and password"""
    user_data["password1"] = "autouserui_123456789"
    page.goto(base_url)
    page.get_by_role("link", name="📝 Регистрация").click()
    page.locator("#id_username").fill(user_data["username"])
    page.locator("#id_email").fill(user_data["email"])
    page.locator("#id_password1").fill(user_data["password1"])
    page.locator("#id_password2").fill(user_data["password2"])
    page.get_by_role("button", name="Зарегистрироваться").click()
    expect(page.locator("#id_password2_error")).to_be_visible()
