import pytest

@pytest.mark.parametrize("session_name", [
    "unauthenticated_session",
    "regular_session",
    "editor_session",
    "admin_session"
])
def test_get_news(request, news_api, session_name):
    """Any user can get news"""
    session = request.getfixturevalue(session_name)
    news_api.set_session(session)
    get_news_response = news_api.get_news()
    assert get_news_response.status_code == 200, f"{session_name} user should have access to news list"

@pytest.mark.parametrize("session_name", [
    "unauthenticated_session",
    "regular_session",
    "editor_session",
    "admin_session"
])
def test_get_news_by_id(request, news_api, test_news, session_name):
    """Any user can get news by id"""
    session = request.getfixturevalue(session_name)
    news_api.set_session(session)
    get_news_by_id_response = news_api.get_news_by_id(test_news["test_news_id"])
    assert get_news_by_id_response.status_code == 200, f"{session_name} user should have access to news view by id"


@pytest.mark.parametrize("session_name, expected_status, msg_err", [
    ("unauthenticated_session", 403, "Unathenticated user shouldn't have access to create news"),
    ("regular_session", 403, "Regular user shouldn't have access to create news"),
    ("editor_session", 200, "Editor user should have access to create news"),
    ("admin_session", 200, "Admin user should have access to create news")
])
def test_create_news(request, news_api, news_data, session_name, expected_status, msg_err):
    """Only admin and editor users can create news"""
    session = request.getfixturevalue(session_name)
    news_api.set_session(session)
    create_news_response = news_api.create_news(news_data)
    assert create_news_response.status_code == expected_status, msg_err

@pytest.mark.parametrize("session_name, expected_status, msg_err", [
    ("unauthenticated_session", 302, "Unathenticated user shouldn't have access to create news"),
    ("regular_session", 403, "Regular user shouldn't have access to create news"),
    ("editor_session", 200, "Editor user should have access to create news"),
    ("admin_session", 200, "Admin user should have access to create news")
])
def test_edit_news(request, news_api, test_news, news_data, session_name, expected_status, msg_err):
    session = request.getfixturevalue(session_name)
    news_api.set_session(session)
    test_edit_news_response = news_api.edit_news(test_news["test_news_id"], news_data, allow_redirects=False)
    assert test_edit_news_response.status_code == expected_status, msg_err

@pytest.mark.parametrize("session_name, expected_status, msg_err, allow_redirects", [
    ("unauthenticated_session", 302, "Unathenticated user shouldn't have access to delete news", False),
    ("regular_session", 403, "Regular user shouldn't have access to delete news", True),
    ("editor_session", 200, "Editor user should have access to delete news", True),
    ("admin_session", 200, "Admin user should have access to delete news", True)
])
def test_delete_news(request, news_api, test_news, session_name, expected_status, msg_err, allow_redirects):
    """Only admin and editor users can delete news"""
    session = request.getfixturevalue(session_name)
    news_api.set_session(session)
    delete_news_response = news_api.delete_news(test_news["test_news_id"], allow_redirects=allow_redirects)
    assert delete_news_response.status_code == expected_status, msg_err
