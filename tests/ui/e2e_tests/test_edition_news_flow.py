import pytest
from playwright.sync_api import expect



@pytest.mark.parametrize("user", [
    "editor_user",
    "admin_user"
])
def test_edition_news(request, home_page, news_page, news_edit_page, login_page, user):
    """Any user can go through flow:
        - Home page
        - Category page
        - Category news page
        - News detail page
        - News
        - News detail page"""
    user_data = request.getfixturevalue(user)
    login_page.login(user_data)
    home_page.navigate()
    home_page.read_news_button.click()
    expect(home_page.page).to_have_url(news_page.news_url)
    news_page.first_news_edit_button.click()
    expect(news_page.page).to_have_url(news_edit_page.news_edit_url)