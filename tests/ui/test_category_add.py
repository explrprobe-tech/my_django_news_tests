import pytest
from playwright.sync_api import Page, expect
from helpers import object_delete

def test_category_add_editor_user(page: Page, base_url: str, editor_user):
    """Editor user can open category add page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(editor_user["username"])
    page.locator("#id_password").fill(editor_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    expect(page).to_have_url(f"{base_url}category/add_category/")
    expect(page.locator(".add-category-header h1")).to_contain_text("📝 Добавить категорию")
    expect(page.locator('label[for="id_title"]')).to_contain_text("Название категории")
    expect(page.locator("#id_title")).to_be_visible()
    expect(page.get_by_role("button", name="✨ Добавить категорию")).to_be_visible()
    expect(page.get_by_role("link", name="❌ Отмена")).to_be_visible()
def test_category_add_admin_user(page: Page, base_url: str, admin_user):
    """Admin user can open category add page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(admin_user["username"])
    page.locator("#id_password").fill(admin_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    expect(page).to_have_url(f"{base_url}category/add_category/")
    expect(page.locator(".add-category-header h1")).to_contain_text("📝 Добавить категорию")
    expect(page.locator('label[for="id_title"]')).to_contain_text("Название категории")
    expect(page.locator("#id_title")).to_be_visible()
    expect(page.get_by_role("button", name="✨ Добавить категорию")).to_be_visible()
    expect(page.get_by_role("link", name="❌ Отмена")).to_be_visible()
def test_category_add_create_category(page: Page, base_url: str, editor_user, category_data, admin_session):
    """Editor user can create category on category add page"""
    import re
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(editor_user["username"])
    page.locator("#id_password").fill(editor_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    page.locator("#id_title").fill(category_data["title"])
    page.get_by_role("button", name="✨ Добавить категорию").click()
    expect(page).to_have_url(re.compile(rf"{base_url}category/\d+/"))
    object_url = page.url
    object_delete(session=admin_session, url_object=object_url)
def test_category_add_to_home_page(page: Page, base_url: str, editor_user):
    """Editor user can return back to home page from category add page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(editor_user["username"])
    page.locator("#id_password").fill(editor_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    page.get_by_role("link", name="❌ Отмена").click()
    expect(page).to_have_url(base_url)
def test_category_add_empty_field(page: Page, base_url: str, editor_user):
    """Editor user can't create category with empty title on category add page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(editor_user["username"])
    page.locator("#id_password").fill(editor_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    page.get_by_role("button", name="✨ Добавить категорию").click()
    expect(page).to_have_url(f"{base_url}category/add_category/")
def test_category_add_invalid_field(page: Page, base_url: str, editor_user):
    """Editor user can't create category with invalid field on category add page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill(editor_user["username"])
    page.locator("#id_password").fill(editor_user["password"])
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    page.get_by_role("link", name="✍️ Добавить категорию").click()
    page.locator("#id_title").fill("1")
    page.get_by_role("button", name="✨ Добавить категорию").click()
    expect(page).to_have_url(f"{base_url}category/add_category/")
    expect(page.locator(".form-group:has(#id_title) .errorlist")).to_be_visible()