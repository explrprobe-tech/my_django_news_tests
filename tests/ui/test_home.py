import pytest
from playwright.sync_api import Page, expect

def test_home_page_undefined_user(page: Page, base_url: str):
    """Undefined user can see home page"""
    page.goto(base_url)
    expect(page.get_by_role("link", name="🔐 Войти")).to_be_visible()
    expect(page.get_by_role("link", name="📝 Регистрация")).to_be_visible()
    expect(page.get_by_role("link", name="🏠 Главная")).to_be_visible()
    expect(page.get_by_role("link", name="📋 Все новости")).to_be_visible()
    expect(page.get_by_role("link", name="Категории")).to_be_visible()
    expect(page.get_by_role("link", name="📰 Читать все новости")).to_be_visible()
    expect(page.locator(".news-grid .news-card:nth-child(1)")).to_be_visible()
    expect(page.locator(".news-grid .news-card:nth-child(2)")).to_be_visible()
    expect(page.locator(".news-grid .news-card:nth-child(3)")).to_be_visible()