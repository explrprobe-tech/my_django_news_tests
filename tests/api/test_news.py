import pytest
from helpers import get_csrf_token

#API news_list
def test_news_list_unauthenticated_user(unauthenticated_session, base_url, test_news):
    """Unauthenticated user can see news list"""
    response_news_list = unauthenticated_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_regular_user(regular_session, base_url, test_news):
    """Unauthenticated user can see news list"""
    response_news_list = regular_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_editor_user(editor_session, base_url, test_news):
    """Unauthenticated user can see news list"""
    response_news_list = editor_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
def test_news_list_admin_user(admin_session, base_url, test_news):
    """Unauthenticated user can see news list"""
    response_news_list = admin_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"

#API view_news
def test_view_news_unauthenticated_user(unauthenticated_session, test_news):
    """Unauthenticated user can see news details"""
    response_news = unauthenticated_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_regular_user(regular_session, test_news):
    """Unauthenticated user can see news details"""
    response_news = regular_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_editor_user(editor_session, test_news):
    """Unauthenticated user can see news details"""
    response_news = editor_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_view_news_admin_user(admin_session, test_news):
    """Unauthenticated user can see news details"""
    response_news = admin_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"