import pytest
from playwright.sync_api import Page, expect

def test_category_news_list_undefined(page: Page, base_url: str):
    """Undefiend user can see news in category"""
    page.goto(base_url)
    page.get_by_role("link", name="Категории").click()
    page.locator(".edit-news-btn").first.click()
    title_element = page.locator("h1.page-title")
    expect(title_element).to_be_visible()
    title_element_text = title_element.text_content()
    assert title_element_text is not None, "Category should have title"
    assert len(title_element_text.strip()) > 0, "Category title shouldn't be empty"
    expect(page.locator(".news-card")).to_be_visible()
def test_category_news_list_page_to_home_page_by_title_button(page: Page, base_url: str):
    """Undefined user can open home page by button Главная"""
    page.goto(base_url)
    page.get_by_role("link", name="Категории").click()
    page.locator(".edit-news-btn").first.click()
    page.get_by_role("link", name="🏠 Главная").click()
    expect(page).to_have_url(base_url)
def test_category_news_list_page_to_news_page_by_title_button(page: Page, base_url: str):
    """Undefiend user can open news page by button Все новости"""
    page.goto(base_url)
    page.get_by_role("link", name="Категории").click()
    page.locator(".edit-news-btn").first.click()
    page.get_by_role("link", name="📋 Все новости").click()
    expect(page).to_have_url(f"{base_url}news/")