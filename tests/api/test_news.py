import pytest
from helpers import get_csrf_token

def test_news_unauthenticated_user_get(unauthenticated_session, base_url, test_news):
    """Unauthenticated user can see news"""
    response_news_list = unauthenticated_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Unauthenticated user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
    response_news = unauthenticated_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Unauthenticated user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_news_regular_user_get(regular_session, base_url, test_news):
    """Regular user can see news"""
    response_news_list = regular_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Regular user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
    response_news = regular_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Regular user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_news_editor_user_get(editor_session, base_url, test_news):
    """Regular user can see news"""
    response_news_list = editor_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Ediitor user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
    response_news = editor_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Ediitor user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"
def test_news_admin_user_get(admin_session, base_url, test_news):
    """Regular user can see news"""
    response_news_list = admin_session.get(url=f"{base_url}news/")
    assert response_news_list.status_code == 200, "Admin user should have access to news list"
    assert test_news["test_news_data"]["title"] in response_news_list.text, "Created news is not on news list page"
    response_news = admin_session.get(url=test_news["test_news_url"])
    assert response_news.status_code == 200, "Admin user should have access to news"
    assert test_news["test_news_data"]["title"] in response_news.text, "Created news is not accessable"