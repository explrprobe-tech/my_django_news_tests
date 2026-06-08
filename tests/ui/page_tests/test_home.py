import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("user", [
    None,
    "regular_user",
    "editor_user",
    "admin_user"
])
def test_home_page(request, home_page, login_page, user):
    """Any user can see home page"""
    if user:
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        home_page.navigate()
        expect(home_page.headers.logout_button, f"{user} should see logout button.").to_be_visible()
        expect(home_page.headers.user_role_text, f"{user} should see user_role_text").to_be_visible()
        if user in ["editor_user", "admin_user"]:
            expect(home_page.headers.secret_button, f"{user} should see secret button").to_be_visible()
            expect(home_page.add_news_button, f"{user} should see news button").to_be_visible()        
    else:
        home_page.navigate()
        expect(home_page.headers.login_button, "Any user should see login button").to_be_visible()
        expect(home_page.headers.signup_button, "Any user should see singup button").to_be_visible()
    expect(home_page.headers.home_button, "Any user should see home button").to_be_visible()
    expect(home_page.headers.all_news_button, "Any user should see all_news_button").to_be_visible()
    expect(home_page.categories_button, "Any user should see categories button").to_be_visible()
    expect(home_page.read_news_button, "Any user should see read_news_button").to_be_visible()
    expect(home_page.first_news_card, "Any user should see first_news_card").to_be_visible()
    expect(home_page.second_news_card, "Any user should see second_news_card").to_be_visible()
    expect(home_page.third_news_card, "Any user should see third_news_card").to_be_visible()
    