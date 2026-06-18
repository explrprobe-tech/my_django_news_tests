import pytest
from playwright.sync_api import expect
import allure


@allure.epic("page_tests")
@allure.feature("news_detail")
@allure.severity(allure.severity_level.NORMAL)
class TestNewsDetail:

    @pytest.mark.parametrize("user", [
        None,
        "regular_user",
        "editor_user",
        "admin_user"
    ])
    def test_news_detail_page(self, request, news_detail_page, login_page, user):
        """Any user can see category page"""
        if user:
            user_data = request.getfixturevalue(user)
            login_page.login(user_data)
            news_detail_page.navigate()
            expect(news_detail_page.headers.logout_button).to_be_visible()
            expect(news_detail_page.headers.user_role_text).to_be_visible()
        else:
            news_detail_page.navigate()
            expect(news_detail_page.headers.login_button).to_be_visible()
            expect(news_detail_page.headers.signup_button).to_be_visible()
        expect(news_detail_page.news_title).to_be_visible()
        expect(news_detail_page.news_public_date_text).to_be_visible()
        expect(news_detail_page.news_category_button).to_be_visible()
        expect(news_detail_page.news_count_views_text).to_be_visible()
        expect(news_detail_page.news_author_text).to_be_visible()
        expect(news_detail_page.news_image).to_be_visible()
        expect(news_detail_page.news_share_facebook_button).to_be_visible()
        expect(news_detail_page.news_share_twitter_button).to_be_visible()
        expect(news_detail_page.news_share_telegram_button).to_be_visible()
        expect(news_detail_page.news_share_link_button).to_be_visible()
        expect(news_detail_page.news_content).to_be_visible()
        expect(news_detail_page.back_news_button).to_be_visible()
