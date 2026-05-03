import pytest
from playwright.sync_api import Page, expect

def test_news_details_page_undefined_user(page: Page, base_url: str):
    """Undefined user can open news details from news page"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости")
    page.get_by_role("link", name="Читать далее →").first.click()
    news_detail_title = page.locator(".news-detail-content")
    news_data_public = page.locator(".news-detail-meta span").nth(0)
    news_category = page.locator(".news-detail-meta span").nth(1)
    news_count_views = page.locator(".news-detail-meta span").nth(2)
    news_author = page.locator(".news-detail-meta span").nth(3)
    expect(news_detail_title).to_be_visible()
    expect(news_data_public).to_be_visible()
    expect(news_category).to_be_visible()
    expect(news_count_views).to_be_visible()
    expect(news_author).to_be_visible()
    assert len(news_data_public.text_content()) > 0, "News data shouldn't to be empty"
    assert len(news_category.text_content()) > 0, "News category shouldn't to be empty"
    assert len(news_count_views.text_content()) > 0, "News count views shouldn't to be empty"
    assert len(news_author.text_content()) > 0, "News author shouldn't to be empty"
    expect(page.locator("img")).to_be_visible()
    expect(page.locator(".share-buttons a.share-btn").nth(0)).to_be_visible()
    expect(page.locator(".share-buttons a.share-btn").nth(1)).to_be_visible()
    expect(page.locator(".share-buttons a.share-btn").nth(2)).to_be_visible()
    expect(page.locator(".share-buttons a.share-btn").nth(3)).to_be_visible()
    news_detail_text = page.locator(".news-detail-text p").nth(0)
    expect(news_detail_text).to_be_visible()
    assert len(news_detail_text.text_content()) > 0, "News detail text shouldn't be empty"
    expect(page.get_by_role("link", name="← Назад к списку новостей")).to_be_visible()
def test_news_details_page_to_category_news_list_page(page: Page, base_url: str):
    """Undefined user can open category news list page from news details page"""
    import re
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости")
    page.get_by_role("link", name="Читать далее →").first.click()
    page.locator(".news-detail-meta a").click()
    expect(page).to_have_url(re.compile(rf"{base_url}category/\d+/"))
def test_news_detail_page_to_news_page(page: Page, base_url: str):
    """Undefined user can return back from news detail page to news page"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости")
    page.get_by_role("link", name="Читать далее →").first.click()
    page.locator(".back-button").click()
    expect(page).to_have_url(f"{base_url}news/")
def test_news_detail_page_to_home_page_by_title_button(page: Page, base_url: str):
    """Undefined user can open home page by button Главная"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости")
    page.get_by_role("link", name="Читать далее →").first.click()
    page.get_by_role("link", name="🏠 Главная").click()
    expect(page).to_have_url(base_url)
def test_news_detail_page_to_news_page_by_title_button(page: Page, base_url: str):
    """Undefiend user can open news page by button Все новости"""
    page.goto(base_url)
    page.get_by_role("link", name="📰 Читать все новости")
    page.get_by_role("link", name="Читать далее →").first.click()
    page.get_by_role("link", name="📋 Все новости").click()
    expect(page).to_have_url(f"{base_url}news/")