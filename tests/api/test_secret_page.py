import pytest
import allure


@allure.epic("API")
@allure.feature("Secret")
@allure.severity(allure.severity_level.MINOR)
class TestSecret:

    @pytest.mark.parametrize("session_name, expected_status, msg_err", [
        ("unauthenticated_session", 403, "Unathenticated user shouldn't have access to secret page api"),
        ("regular_session", 403, "Regular user shouldn't have access to secret page api"),
        ("editor_session", 200, "Editor user should have access to secret page api"),
        ("admin_session", 200, "Admin user should have access to secret page api")
    ])
    def test_get_secret_page(self, request, secret_api, session_name, expected_status, msg_err):
        """Only admin and editor user have access to secret page api"""
        session = request.getfixturevalue(session_name)
        secret_api.set_session(session)
        secret_page_response = secret_api.get_secret()
        assert secret_page_response.status_code == expected_status, msg_err
        if secret_page_response.status_code == 200:
            assert "SOLAR OBSERVATORY" in secret_page_response.text
            assert 'Station' in secret_page_response.text
            assert 'Observation' in secret_page_response.text
            assert 'frequency' in secret_page_response.text
            assert 'flux' in secret_page_response.text
            assert 'observed_quality' in secret_page_response.text
