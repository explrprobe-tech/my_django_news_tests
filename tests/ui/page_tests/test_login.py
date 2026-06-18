import pytest
from playwright.sync_api import expect
import allure


@allure.epic("page_tests")
@allure.feature("login")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    def test_login_page(self, login_page):
        login_page.navigate()
        expect(login_page.page).to_have_url(login_page.login_url)
        expect(login_page.headers.login_button, "Any user should see login_button").to_be_visible()
        expect(login_page.headers.signup_button, "Any user should see signup_button").to_be_visible()
        expect(login_page.headers.home_button, "Any user should see home_button").to_be_visible()
        expect(login_page.headers.all_news_button, "Any user should see all_news_button").to_be_visible()
        expect(login_page.username_field, "Any user should see username_field").to_be_visible()
        expect(login_page.password_field, "Any user should see password_field").to_be_visible()
        expect(login_page.enter_button, "Any user should see enter_button").to_be_visible()
        expect(login_page.back_home_button, "Any user should see back_home_button").to_be_visible()
        expect(login_page.signup_button, "Any user should see signup_button").to_be_visible()

    @pytest.mark.parametrize("user, can_login", [
        ["empty_user", False],
        ["undefined_user", False],
        ["regular_user", True],
        ["editor_user", True],
        ["admin_user", True]
    ])
    def test_user_login(self, request, login_page, home_page, user, can_login):
        """Only registered user can log-in through UI"""
        user_data = request.getfixturevalue(user)
        login_page.navigate()
        login_page.login(user_data)
        if can_login:
            expect(login_page.page, f"{user} should have access to log-in").to_have_url(home_page.home_page_url)
        else:
            expect(login_page.page, f"{user} shouldn't have access to log-in").to_have_url(login_page.login_url)
            expect(login_page.error_message_text, "User with wrong data should see error_message_text").to_be_visible()

