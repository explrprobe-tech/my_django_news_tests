import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("user", [
    None,
    "regular_user",
    "editor_user",
    "admin_user"
])
def test_category_page(request, category_page, login_page, user):
    """Any user can see category page"""
    if user:
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        category_page.navigate()
        expect(category_page.headers.logout_button).to_be_visible()
        expect(category_page.headers.user_role_text).to_be_visible()
        if user in ["editor_user", "admin_user"]:
            expect(category_page.category_add_button).to_be_visible()
    else:
        category_page.navigate()
    expect(category_page.category_title).not_to_be_empty()
    expect(category_page.read_all_news_button).to_be_visible()
    expect(category_page.first_category_card).to_be_visible()
    expect(category_page.first_category_read_button).to_be_visible()
