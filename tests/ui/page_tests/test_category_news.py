import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("user", [
    None,
    "regular_user",
    "editor_user",
    "admin_user"
])
def test_category_news_page(request, category_news_page, login_page, user):
    """Any user can see category news list page"""
    if user:
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        category_news_page.navigate()
        expect(category_news_page.headers.logout_button).to_be_visible()
        expect(category_news_page.headers.user_role_text).not_to_be_empty()
        if user in ["admin_user"]:
            expect(category_news_page.first_category_news_edit_button).to_be_visible()
    else:
        category_news_page.navigate()
        expect(category_news_page.headers.login_button).to_be_visible()
        expect(category_news_page.headers.signup_button).to_be_visible()
    expect(category_news_page.headers.home_button).to_be_visible()
    expect(category_news_page.headers.all_news_button).to_be_visible()
    expect(category_news_page.category_news_title).not_to_be_empty()
    expect(category_news_page.first_category_news_card).to_be_visible()
    expect(category_news_page.first_category_news_read_button).to_be_visible()
