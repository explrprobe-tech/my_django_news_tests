import pytest
from playwright.sync_api import expect



@pytest.mark.parametrize("user", [
    "editor_user",
    "admin_user"
])
def test_creation_category(request, home_page, category_page, category_add_page, login_page, user):
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
    home_page.categories_button.click()
    expect(home_page.page).to_have_url(category_page.category_url)
    category_page.category_add_button.click()
    expect(category_page.page).to_have_url(category_add_page.category_add_url)