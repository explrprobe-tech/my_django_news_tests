import pytest
from playwright.sync_api import Page, expect

def test_news_page_undefined_user(page: Page, base_url: str):
    """Undefiend user can see news page"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости").click()
    expect(page.locator("h1.page-title")).to_have_text("Все новости")
    expect(page.locator(".news-card").first).to_be_visible()
    expect(page.get_by_role("link", name="Читать далее →").first).to_be_visible()
def test_news_page_regular_user(page: Page, base_url: str):
    "Regular user can see news page"
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_regular")
    page.locator("#id_password").fill("autoregular_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="📰 Читать все новости").click()
    expect(page.locator("h1.page-title")).to_have_text("Все новости")
    expect(page.locator(".news-card").first).to_be_visible()
    expect(page.get_by_role("link", name="Читать далее →").first).to_be_visible()
def test_news_page_editor_user(page: Page, base_url: str):
    "Editor user can see news page and add news"
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_editor")
    page.locator("#id_password").fill("autoeditor_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="📰 Читать все новости").click()
    expect(page.locator("h1.page-title")).to_have_text("Все новости")
    expect(page.locator(".news-card").first).to_be_visible()
    expect(page.get_by_role("link", name="Читать далее →").first).to_be_visible()
def test_news_page_admin_user(page: Page, base_url: str):
    "Admin user can see news page and add news"
    page.goto(base_url)
    page.get_by_role("link", name="🔐 Войти").click()
    page.locator("#id_username").fill("autotest_admin")
    page.locator("#id_password").fill("autoadmin_123456789!")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="📰 Читать все новости").click()
    expect(page.locator("h1.page-title")).to_have_text("Все новости")
    expect(page.locator(".news-card").first).to_be_visible()
    expect(page.get_by_role("link", name="Читать далее →").first).to_be_visible()
def test_news_page_to_home_page_by_title_button(page: Page, base_url: str):
    """Undefined user can open home page by button Главная"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости").click()
    page.get_by_role("link", name="🏠 Главная").click()
    expect(page).to_have_url(base_url)