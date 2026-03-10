

def test_secret_page_admin_user(admin_session, base_url):
    """Autharizated user can open secret page"""
    response = admin_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "SOLAR OBSERVATORY" in response.text

# def test_secret_page_regular_user(authenticated_session, base_url):
#     """Autharizated user can open secret page"""
#     response = authenticated_session.get(f"{base_url}/secret/")
#     assert response.status_code == 403

# def test_secret_page_regular_user(unauthenticated_session, base_url):
#     """Autharizated user can open secret page"""
#     response = unauthenticated_session.get(f"{base_url}/secret/")
#     assert response.status_code == 301
#     assert response.url == f"{base_url}/login/"
    