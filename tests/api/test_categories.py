import pytest
from helpers import get_csrf_token

@pytest.mark.parametrize("session_name", [
    "unauthenticated_session",
    "regular_session",
    "editor_session",
    "admin_session"
])
def test_get_categories(request, category_api, session_name):
    """Any user has access to category list"""
    session = request.getfixturevalue(session_name)
    category_api.set_session(session)
    response_get_categories = category_api.get_categories()
    assert response_get_categories.status_code == 200, f"{session_name} user should have access to categories"


@pytest.mark.parametrize("session_name", [
    "unauthenticated_session",
    "regular_session",
    "editor_session",
    "admin_session"
])
def test_get_news_by_category(request, category_api, test_category, session_name):
    """Any user has access to news by category"""
    session = request.getfixturevalue(session_name)
    category_api.set_session(session)
    response_get_news_by_category = category_api.get_news_by_category(test_category["test_category_id"])
    assert response_get_news_by_category.status_code == 200, f"{session_name} user should have access to news by category"

@pytest.mark.parametrize("session_name, expected_status, msg_err", [
    ("unauthenticated_session", 403, "Unathenticated user shouldn't have access to create category"),
    ("regular_session", 403, "Regular user shouldn't have access to create category"),
    ("editor_session", 200, "Editor user should have access to create category"),
    ("admin_session", 200, "Admin user should have access to create category")
])
def test_create_category(request, category_api, category_data, object_helper, session_name, expected_status, msg_err):
    """Only Admin and Editor users can create category"""
    session = request.getfixturevalue(session_name)
    category_api.set_session(session)
    create_category_response = category_api.create_category(category_data)
    assert create_category_response.status_code == expected_status, msg_err
    if expected_status == 200:
        id_object = object_helper.get_object_id_by_name(model="category", name=category_data["title"])
        object_delete = object_helper.object_delete(id_object)
        assert object_delete.status_code == 200, "Test object should be deleted after testing"

@pytest.mark.parametrize("session_name, expected_status, allow_redirects", [
    ("unauthenticated_session", 403, False),
    ("regular_session", 403, False),
    ("editor_session", 200, True),
    ("admin_session", 200, True)
])
def test_delete_category(request, category_api, test_category, session_name, expected_status, allow_redirects):
    """Only Admin and Editor users can create category"""
    session = request.getfixturevalue(session_name)
    category_api.set_session(session)
    delete_category_response = category_api.delete_category(test_category["test_category_id"], allow_redirects=allow_redirects)
    # print(delete_category_response.text)
    assert delete_category_response.status_code == expected_status, f"{session_name} user should have access to create category"