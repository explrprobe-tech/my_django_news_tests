import pytest
from playwright.sync_api import expect
import allure


@allure.epic("page_tests")
@allure.feature("register")
@allure.severity(allure.severity_level.BLOCKER)
class TestRegister:

    def test_register_page(self, register_page):
        """Users can see Register page"""
        register_page.navigate()
        expect(register_page.username_field).to_be_visible()
        expect(register_page.email_field).to_be_visible()
        expect(register_page.password1_field).to_be_visible()
        expect(register_page.password2_field).to_be_visible()
        expect(register_page.register_button).to_be_visible()
        expect(register_page.login_button).to_be_visible()
        expect(register_page.back_home_button).to_be_visible()


    @pytest.mark.parametrize("user, can_register", [
        ["user_data", True],
        ["user_data_empty_username", False],
        ["user_data_username_and_password_similar", False]
    ])
    def test_user_register(self, request, register_page, home_page, object_helper, user, can_register):
        """User can register only with valid data"""
        user_data = request.getfixturevalue(user)
        register_page.register(user_data)
        if can_register:
            expect(register_page.page).to_have_url(home_page.home_page_url)
            id_object = object_helper.get_object_id_by_name(model="user", name=user_data["username"])
            object_delete_response = object_helper.object_delete(id_object)
            assert object_delete_response.status_code == 200, "Test object should be deleted after testing"
        else:
            expect(register_page.page).to_have_url(register_page.register_url)
            if user == "user_data_empty_username":
                expect(register_page.username_error_text).to_be_visible()
            if user == "user_data_username_and_password_similar":
                expect(register_page.password2_error_text).to_be_visible()
