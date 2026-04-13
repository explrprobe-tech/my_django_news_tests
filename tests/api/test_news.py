import pytest
from helpers import get_csrf_token

#API news_list
def test_news_list_unauthenticated_user(unauthenticated_session, base_url, test_news):
    """Unauthenticated user can see news list"""
    response_news_list = unauthenticated_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_regular_user(regular_session, base_url, test_news):
    """Regular user can see news list"""
    response_news_list = regular_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Regular user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_editor_user(editor_session, base_url, test_news):
    """Editor user can see news list"""
    response_news_list = editor_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Editor user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_admin_user(admin_session, base_url, test_news):
    """Admin user can see news list"""
    response_news_list = admin_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Admin user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"

#API view_news
def test_view_news_unauthenticated_user(unauthenticated_session, test_news):
    """Unauthenticated user can see news details"""
    response_news = unauthenticated_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_regular_user(regular_session, test_news):
    """Regular user can see news details"""
    response_news = regular_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Regular user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_editor_user(editor_session, test_news):
    """Editor user can see news details"""
    response_news = editor_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Editor user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_admin_user(admin_session, test_news):
    """Admin user can see news details"""
    response_news = admin_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Admin user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"

#API add_news
def test_add_news_and_news_delete_unauthenticated_user(base_url, test_category, test_news, unauthenticated_session):
    """Unathenticated user can't create and delete news"""
    url_news_creation = f"{base_url}news/add_news/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url_news_creation)
    test_news_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_news_creation = unauthenticated_session.post(url=url_news_creation, data=test_news_data)
    assert response_news_creation.status_code == 403, "Unauthenticated user shouldn't have access to create news"
    url_news_delition = f"{test_news['test_news_url']}delete/"
    response_news_delition = unauthenticated_session.post(url=url_news_delition, data={"csrfmiddlewaretoken": csrf_token})
    assert response_news_delition.status_code == 403, "Unathenticated user shouldn't have access to delete news"
def test_add_news_and_news_delete_regular_user(base_url, test_category, test_news, regular_session):
    """Regular user can't create and delete news"""
    url_news_creation = f"{base_url}news/add_news/"
    csrf_token = get_csrf_token(session=regular_session, url=url_news_creation)
    test_news_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_news_creation = regular_session.post(url=url_news_creation, data=test_news_data)
    assert response_news_creation.status_code == 403, "Regular user shouldn't have access to create news"
    url_news_delition = f"{test_news['test_news_url']}delete/"
    response_news_delition = regular_session.post(url=url_news_delition, data={"csrfmiddlewaretoken": csrf_token})
    assert response_news_delition.status_code == 403, "Regular user shouldn't have access to delete news"
def test_add_news_and_news_delete_editor_user(base_url, test_category, editor_session):
    """Editor user can't create and delete news"""
    url_news_creation = f"{base_url}news/add_news/"
    csrf_token = get_csrf_token(session=editor_session, url=url_news_creation)
    test_news_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_news_creation = editor_session.post(url=url_news_creation, data=test_news_data)
    assert response_news_creation.status_code == 200, "Editor user should have access to create news"
    url_news_delition = f"{response_news_creation.url}delete/"
    response_news_deletion = editor_session.post(url=url_news_delition, data={"csrfmiddlewaretoken": csrf_token})
    assert response_news_deletion.status_code == 200, "Editor user should have access to delete news"
def test_add_news_and_news_delete_admin_user(base_url, test_category, admin_session):
    """Admin user can't create and delete news"""
    url_news_creation = f"{base_url}news/add_news/"
    csrf_token = get_csrf_token(session=admin_session, url=url_news_creation)
    test_news_data = {
        "title": "Test News",
        "content": "Content for Test News",
        "short_description": "Short description for Test News",
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_news_creation = admin_session.post(url=url_news_creation, data=test_news_data)
    assert response_news_creation.status_code == 200, "Admin user shouldn't have access to create news"
    url_news_delition = f"{response_news_creation.url}delete/"
    response_news_deletion = admin_session.post(url=url_news_delition, data={"csrfmiddlewaretoken": csrf_token})
    assert response_news_deletion.status_code == 200, "Admin user should have access to delete news"