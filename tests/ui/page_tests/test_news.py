import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("user", [
    None,
    "regular_user",
    "editor_user",
    "admin_user"
])
def test_news_page(request, news_page, login_page, user):
    """Any user can see news page"""
    if user:
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        news_page.navigate()
        expect(news_page.headers.logout_button).to_be_visible()
        expect(news_page.headers.user_role_text).to_be_visible()
        if user in ["editor_user", "admin_user"]:
            expect(news_page.category_button).to_be_visible()
            expect(news_page.news_add_button).to_be_visible()
            expect(news_page.first_news_edit_button).to_be_visible()
    else:
        news_page.navigate()
    expect(news_page.news_title).not_to_be_empty()
    expect(news_page.first_news_card).to_be_visible()
    expect(news_page.first_news_read_button).to_be_visible()

