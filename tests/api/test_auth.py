from helpers import object_delete, get_csrf_token, admin_user, editor_user, regular_user

def test_register(base_url, unauthenticated_session, admin_session):
    """User can register in website"""
    url_register = f"{base_url}register/"
    data_register = {
        'username': 'Test_user',
        'password1': 'Test_user_password_123',
        'password2': 'Test_user_password_123',
        'email': 'test_user@example.ru',
        'csrfmiddlewaretoken': get_csrf_token(session=unauthenticated_session, url=url_register)
    }
    response_register = unauthenticated_session.post(url=url_register, data=data_register)
    assert response_register.status_code == 200, "Unathenticated user can't register on website"
    url_delete = f"{base_url}{response_register.json().get('user_id')}"
    response_delete = object_delete(session=admin_session, url_object=url_delete)
    assert response_delete.status_code == 200, "User wasn't deleted"

def test_delete_unathenticated_user(test_user, unauthenticated_session):
    """Unathenticated user can't delete user"""
    url_delete = f"{test_user["test_user_url"]}delete/"
    csrf_token = unauthenticated_session.cookies.get("csrftoken")
    response_delete = unauthenticated_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token})
    assert response_delete.status_code == 403, "Unathenticated user shouldn't have access to delete user"
def test_delete_regular_user(test_user, regular_session):
    """Regular user can't delete user"""
    url_delete = f"{test_user["test_user_url"]}delete/"
    csrf_token = regular_session.cookies.get("csrftoken")
    response_delete = regular_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token})
    assert response_delete.status_code == 403, "Regular user shouldn't have access to delete user"
def test_delete_editor_user(test_user, editor_session):
    """Editor user can't delete user"""
    url_delete = f"{test_user["test_user_url"]}delete/"
    csrf_token = editor_session.cookies.get("csrftoken")
    response_delete = editor_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token})
    assert response_delete.status_code == 403, "Editor user shouldn't have access to delete user"
def test_delete_admin_user(test_user, admin_session):
    """Admin user can't delete user"""
    url_delete = f"{test_user["test_user_url"]}delete/"
    csrf_token = admin_session.cookies.get("csrftoken")
    response_delete = admin_session.post(url=url_delete, data={"csrfmiddlewaretoken": csrf_token}, allow_redirects=False)
    assert response_delete.status_code == 200, "Admin user should have access to delete user"

def test_login_regular_user(base_url, unauthenticated_session):
    """Regular user can log-in"""
    url_login = f"{base_url}login/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url_login)
    regular_user['csrfmiddlewaretoken'] = csrf_token
    response_login = unauthenticated_session.post(url=url_login, data=regular_user, allow_redirects=False)
    assert response_login.status_code == 302, "Regular user should have access to log-in"
    assert response_login.headers.get('Location') == '/', "Regular user wasn't redirected"
def test_login_editor_user(base_url, unauthenticated_session):
    """Editor user can log-in"""
    url_login = f"{base_url}login/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url_login)
    editor_user['csrfmiddlewaretoken'] = csrf_token
    response_login = unauthenticated_session.post(url=url_login, data=editor_user, allow_redirects=False)
    assert response_login.status_code == 302, "Editor user should have access to log-in"
    assert response_login.headers.get('Location') == '/', "Editor user wasn't redirected"
def test_login_admin_user(base_url, unauthenticated_session):
    """Admin user can log-in"""
    url_login = f"{base_url}login/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url_login)
    admin_user['csrfmiddlewaretoken'] = csrf_token
    response_login = unauthenticated_session.post(url=url_login, data=admin_user, allow_redirects=False)
    assert response_login.status_code == 302, "Admin user should have access to log-in"
    assert response_login.headers.get('Location') == '/', "Admin user wasn't redirected"
def test_login_undefined_user(base_url, unauthenticated_session):
    """Undefined user can't log-in"""
    url_login = f"{base_url}login/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url_login)
    undefined_user = {
        "username": "Test",
        "password": "Test_123",
        "csrfmiddlewaretoken": csrf_token
    }
    response_login = unauthenticated_session.post(url=url_login, data=undefined_user)
    assert response_login.status_code == 200, "Undefined user shouldn't have access to log-in"
    assert 'Неверное имя пользователя или пароль. Попробуйте снова.' in response_login.text, "Undefined should get alert-error"

def test_logout_regular_user(base_url, regular_session):
    """Regular user can log-out"""
    url_logout = f"{base_url}logout/"
    response_logout = regular_session.get(url=url_logout, allow_redirects=False)
    assert response_logout.status_code == 302, "Regular user should have access to log-out"
    assert response_logout.headers.get('Location') == '/', 'Regular user should be redirected to home page after log-out'
def test_logout_editor_user(base_url, editor_session):
    """Editor user can log-out"""
    url_logout = f"{base_url}logout/"
    response_logout = editor_session.get(url=url_logout, allow_redirects=False)
    assert response_logout.status_code == 302, "Editor user should have access to log-out"
    assert response_logout.headers.get('Location') == '/', 'Editor user should be redirected to home page after log-out'
def test_logout_admin_user(base_url, admin_session):
    """Admin user can log-out"""
    url_logout = f"{base_url}logout/"
    response_logout = admin_session.get(url=url_logout, allow_redirects=False)
    assert response_logout.status_code == 302, "Admin user should have access to log-out"
    assert response_logout.headers.get('Location') == '/', 'Admin user should be redirected to home page after log-out'