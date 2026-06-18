import pytest
from playwright.sync_api import expect
import allure


@allure.epic("e2e_tests")
@allure.feature("reading_news_flow")
@allure.severity(allure.severity_level.CRITICAL)
class TestReadingNews:

    @pytest.mark.parametrize("user", [
        None,
        "regular_user",
        "editor_user",
        "admin_user"
    ])
    def test_reading_news(self, request, home_page, category_page, category_news_page, news_detail_page, news_page, login_page, user):
        """Any user can go through flow:
            - Home page
            - Category page
            - Category news page
            - News detail page
            - News
            - News detail page"""
        if user:
            user_data = request.getfixturevalue(user)
            login_page.login(user_data)
        home_page.navigate()
        expect(home_page.page).to_have_url(home_page.home_page_url)
        home_page.categories_button.click()
        expect(home_page.page).to_have_url(category_page.category_url)
        category_page.first_category_read_button.click()
        expect(category_page.page).to_have_url(category_news_page.category_news_url)
        category_news_page.first_category_news_read_button.click()
        expect(category_news_page.page).to_have_url(news_detail_page.news_detail_url)
        news_detail_page.headers.all_news_button.click()
        expect(news_detail_page.page).to_have_url(news_page.news_url)
        news_page.first_news_read_button.click()
        expect(news_page.page).to_have_url(news_detail_page.news_detail_url)