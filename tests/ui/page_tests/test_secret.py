import pytest
from playwright.sync_api import expect
import allure


@allure.epic("page_tests")
@allure.feature("secret")
@allure.severity(allure.severity_level.MINOR)
class TestSecret:

    @pytest.mark.parametrize("user", [
        "editor_user",
        "admin_user"
    ])
    def test_news_add_page(self, request, secret_page, login_page, user):
        """Any user can see category page"""
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        secret_page.navigate()
        expect(secret_page.secret_solar_title).not_to_be_empty()
        expect(secret_page.secret_solar_frequency_value).not_to_be_empty()
        expect(secret_page.secret_solar_flux_value).not_to_be_empty()
        expect(secret_page.secret_solar_observed_quality_value).not_to_be_empty()
        expect(secret_page.secret_mars_title).not_to_be_empty()
        expect(secret_page.secret_mars_perseverance_value).not_to_be_empty()
        expect(secret_page.secret_mars_temperature_value).not_to_be_empty()
        expect(secret_page.secret_mars_season_value).not_to_be_empty()
        expect(secret_page.secret_mars_latest_discovery_value).not_to_be_empty()