import pytest
from playwright.sync_api import Page, expect

def test_categories_page_undefiend_user(page: Page, base_url: str):
    """Undefiend user can see categories page"""
    page.goto(base_url)
    page.get_by_role("link", name="Категории").click()
    expect(page).to_have_url(f"{base_url}category/")
    expect(page.locator("h1.page-title")).to_have_text("Категории")
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    expect(page.locator(".news-card:first-child")).to_be_visible()
    expect(page.locator(".edit-news-btn").first).to_be_visible()
    expect(page.get_by_role("link", name="✍️ Добавить категорию")).not_to_be_visible()
def test_categories_page_regular_user(page: Page, base_url: str):
    """Regular user can see categories page"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_regular")
    page.locator("#id_password").fill("autoregular_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    expect(page).to_have_url(f"{base_url}category/")
    expect(page.locator("h1.page-title")).to_have_text("Категории")
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    expect(page.locator(".news-card:first-child")).to_be_visible()
    expect(page.locator(".edit-news-btn").first).to_be_visible()
    expect(page.get_by_role("link", name="✍️ Добавить категорию")).not_to_be_visible()
def test_categories_page_editor_user(page: Page, base_url: str):
    """Editor user can see categories page and add category"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_editor")
    page.locator("#id_password").fill("autoeditor_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    expect(page).to_have_url(f"{base_url}category/")
    expect(page.locator("h1.page-title")).to_have_text("Категории")
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    expect(page.locator(".news-card:first-child")).to_be_visible()
    expect(page.locator(".edit-news-btn").first).to_be_visible()
    expect(page.get_by_role("link", name="✍️ Добавить категорию")).to_be_visible()
def test_categories_page_admin_user(page: Page, base_url: str):
    """Admin user can see categories page and add category"""
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_admin")
    page.locator("#id_password").fill("autoadmin_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="Категории").click()
    expect(page).to_have_url(f"{base_url}category/")
    expect(page.locator("h1.page-title")).to_have_text("Категории")
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    expect(page.locator(".news-card:first-child")).to_be_visible()
    expect(page.locator(".edit-news-btn").first).to_be_visible()
    expect(page.get_by_role("link", name="✍️ Добавить категорию")).to_be_visible()