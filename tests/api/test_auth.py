import pytest

def test_register(auth_api, object_helper):
    """User can register in website"""
    data_register = {
        'username': 'Test_user',
        'password': 'Test_user_password_123',
        'email': 'test_user@example.ru'
    }
    response_register = auth_api.register(data_register["username"], data_register["password"], data_register["email"])
    assert response_register.status_code == 200, "Unathenticated user can't register on website"
    id_object = object_helper.get_object_id_by_name("user", data_register["username"])
    object_delete = object_helper.object_delete(id_object)
    assert object_delete.status_code == 200, "User wasn't deleted"

@pytest.mark.parametrize("session_name, expected_status, allow_redirects", [
    ("unauthenticated_session", 403, True),
    ("regular_session", 403, True),
    ("editor_session", 403, True),
    ("admin_session", 200, False)
])
def test_delete_user_permision(request, test_user, user_api, session_name, expected_status, allow_redirects):
    """Only admin has permission to delete users"""
    session = request.getfixturevalue(session_name)
    user_api.set_session(session)
    response_delete = user_api.delete_user(test_user["test_user_delete_endpoint"], allow_redirects=allow_redirects)
    assert response_delete.status_code == expected_status

@pytest.mark.parametrize("session_name, expected_status, user_fixture", [
    ("unauthenticated_session", 200, "undefined_user"),
    ("regular_session", 302, "regular_user"),
    ("editor_session", 302, "editor_user"),
    ("admin_session", 302, "admin_user")])
def test_login_user(request, auth_api, session_name, expected_status, user_fixture, ):
    """Only user with valid data can log-in"""
    session = request.getfixturevalue(session_name)
    auth_api.set_session(session)
    user_data = request.getfixturevalue(user_fixture)
    username = user_data["username"]
    password = user_data["password"]
    response_login = auth_api.login(username, password)
    assert response_login.status_code == expected_status, f"{username} user should have access to log-in"
    if expected_status == 200:
        assert 'Неверное имя пользователя или пароль. Попробуйте снова.' in response_login.text, f"{username} should get alert-error"

@pytest.mark.parametrize("session_name", [
    "unauthenticated_session",
    "regular_session",
    "editor_session",
    "admin_session"
])
def test_logout_user(request, user_api, session_name):
    """Any user log-out"""
    session = request.getfixturevalue(session_name)
    user_api.set_session(session)
    response_logout = user_api.logout(allow_redirects=False)
    assert response_logout.status_code == 302, f"{session_name} user should have access to log-out"
    assert response_logout.headers.get('Location') == '/', f'{session_name} user should be redirected to home page after log-out'
