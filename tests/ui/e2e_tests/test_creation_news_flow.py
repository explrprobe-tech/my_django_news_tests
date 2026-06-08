import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("user", [
    "editor_user",
    "admin_user"
])
def test_creation_news(request, home_page, news_add_page, login_page, user):
    """Editor and admin users can go through flow:
        - Home
        - Add news"""
    user_data = request.getfixturevalue(user)
    login_page.login(user_data)
    home_page.navigate()
    home_page.add_news_button.click()
    expect(home_page.page).to_have_url(news_add_page.news_add_url)