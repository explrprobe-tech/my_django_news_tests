

def test_secret_page_with_auth(authenticated_session, base_url):
    """Autharizated user can open secret page"""
    response = authenticated_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "Секретная страница" in response.text

# def test_secret_page_with_auth(db_cleanup, unauthenticated_session, base_url):
#     """Unauthorized user is redirected to log-in page"""
#     response = unauthenticated_session.get(f"{base_url}/secret/")
#     assert response.status_code == 301
#     assert response.url == f"{base_url}/login/"