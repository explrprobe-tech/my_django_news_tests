import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("user", [
    "editor_user",
    "admin_user"
])
def test_category_add_page(request, category_add_page, login_page, user):
    """Admin and editor users can see category add page"""
    user_data = request.getfixturevalue(user)
    login_page.login(user_data)
    category_add_page.navigate()
    expect(category_add_page.title_field).to_be_visible()
    expect(category_add_page.category_add_button).to_be_visible()
    expect(category_add_page.cancel_button).to_be_visible()

@pytest.mark.parametrize("user", [
    "editor_user",
    "admin_user"
])
def test_user_category_add(request, category_add_page, login_page, category_data, object_helper, user):
    """Admin and editor users can add category on category add page"""
    user_data = request.getfixturevalue(user)
    login_page.login(user_data)
    category_add_page.category_add(category_data)
    category_id = object_helper.get_object_id_by_name("category", name=category_data["title"])
    expect(category_add_page.page).to_have_url(f"{category_add_page.base_url}/{category_id}")
    object_delete_response = object_helper.object_delete(category_id)
    assert object_delete_response.status_code == 200, "Test object should be deleted after testing"
