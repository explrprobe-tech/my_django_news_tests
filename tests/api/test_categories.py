import pytest
from helpers import get_csrf_token

def test_categories_unauthenticated_user_get(unauthenticated_session, base_url, test_category):
    """Unauthorized user can see categories"""
    response_categories_list = unauthenticated_session.get(url=f"{base_url}category/")
    assert response_categories_list.status_code == 200, "Unauthenticated user should have access to categories"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
    response_category = unauthenticated_session.get(url=test_category["test_category_url"])
    assert response_category.status_code == 200, "Unauthenticated user should have access to category"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
def test_categories_regular_user_get(regular_session, base_url, test_category):
    """Regular user can see categories"""
    response_categories_list = regular_session.get(url=f"{base_url}category/")
    assert response_categories_list.status_code == 200, "Regular user should have access to categories"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
    response_category = regular_session.get(url=test_category["test_category_url"])
    assert response_category.status_code == 200, "Regular user should have access to category"
    assert test_category["test_category_data"]["title"] in response_category.text, "Created category is not on category page"
def test_categories_editor_user_get(editor_session, base_url, test_category):
    """Editor user can see categories"""
    response_categories_list = editor_session.get(url=f"{base_url}category/")
    assert response_categories_list.status_code == 200, "Editor user should have access to categories"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
    response_category = editor_session.get(url=test_category["test_category_url"])
    assert response_category.status_code == 200, "Editor user should have access to category"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
def test_categories_admin_user_get(admin_session, base_url, test_category):
    """Admin user can see categories"""
    response_categories_list = admin_session.get(url=f"{base_url}category/")
    assert response_categories_list.status_code == 200, "Admin user should have access to categories"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
    response_category = admin_session.get(url=test_category["test_category_url"])
    assert response_category.status_code == 200, "Admin user should have access to category"
    assert test_category["test_category_data"]["title"] in response_categories_list.text, "Created category is not on category page"
def test_categories_unauthenticated_user_post(unauthenticated_session, base_url, test_category):
    """Unauthenticated user can't create category"""
    url = f"{base_url}category/add_category/"
    response = unauthenticated_session.post(url=url, data=test_category["test_category_url"])
    assert response.status_code == 403, "Unauthenticated user shouldn't have access to create category"
def test_categories_regular_user_post(regular_session, base_url, test_category):
    """Unauthenticated user can't create category"""
    url = f"{base_url}category/add_category/"
    response = regular_session.post(url=url, data=test_category["test_category_url"])
    assert response.status_code == 403, "Regular user shouldn't have access to create category"
def test_categories_editor_user_post(editor_session, base_url, test_category):
    """Editor user can't create category"""
    url_create = f"{base_url}category/add_category/"
    csrf_token = get_csrf_token(session=editor_session, url=url_create)
    test_category_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_create = editor_session.post(url=url_create, data=test_category_data)
    assert response_create.status_code == 200, "Editor user should have access to create category"
    if response_create.status_code == 200:
        url_delete = f"{response_create.url}delete/"
        response_delete = editor_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token})
        assert response_delete.status_code == 200, "Editor user should have to access to delete category"
def test_categories_admin_user_post(admin_session, base_url, test_category):
    """Unauthenticated user can't create category"""
    url_create = f"{base_url}category/add_category/"
    csrf_token = get_csrf_token(session=admin_session, url=url_create)
    test_category_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_create = admin_session.post(url=url_create, data=test_category_data)
    assert response_create.status_code == 200, "Admin user should have access to create category"
    if response_create.status_code == 200:
        url_delete = f"{response_create.url}delete/"
        response_delete = admin_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token})
        assert response_delete.status_code == 200, "Admin user should have to access to delete category"