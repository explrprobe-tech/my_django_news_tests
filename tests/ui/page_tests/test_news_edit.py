import pytest
from playwright.sync_api import Page, expect
import allure


@allure.epic("page_tests")
@allure.feature("news_edit")
@allure.severity(allure.severity_level.NORMAL)
class TestNewsEdit:

    @pytest.mark.parametrize("user", [
        "editor_user",
        "admin_user"
    ])
    def test_news_edit_page(self, request, news_edit_page, login_page, user):
        """Admin and editor users can see news edit page"""
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        news_edit_page.navigate()
        expect(news_edit_page.headers.logout_button).to_be_visible()
        expect(news_edit_page.headers.user_role_text).to_be_visible()
        expect(news_edit_page.news_edit_title).to_be_visible()
        expect(news_edit_page.news_title_title).to_be_visible()
        expect(news_edit_page.news_title_field).not_to_be_empty()
        expect(news_edit_page.news_category_title).to_be_visible()
        expect(news_edit_page.news_category_field).not_to_be_empty()
        expect(news_edit_page.news_short_description_title).to_be_visible()
        expect(news_edit_page.news_short_description_field).to_be_visible()
        expect(news_edit_page.news_short_description_hint).to_be_visible()
        expect(news_edit_page.news_image_title).to_be_visible()
        expect(news_edit_page.news_image_hint_upper).to_be_visible()
        expect(news_edit_page.news_image_field).to_be_visible()
        expect(news_edit_page.news_image_hint_formats).to_be_visible()
        expect(news_edit_page.news_image_delete_checkbox).to_be_visible()
        expect(news_edit_page.news_content_title).to_be_visible()
        expect(news_edit_page.news_content_field).not_to_be_empty()
        expect(news_edit_page.news_public_checkbox).to_be_visible()
        expect(news_edit_page.news_save_button).to_be_visible()
        expect(news_edit_page.cancel_button).to_be_visible()

    @pytest.mark.parametrize("user", [
        "editor_user",
        "admin_user"
    ])
    def test_news_edit(self, request, news_edit_page, login_page, test_news, test_category, news_data, user):
        """Any user can see news page"""
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        news_edit_page.news_edit(test_news, test_category, news_data)
        expect(news_edit_page.page).to_have_url(test_news["test_news_url"])


