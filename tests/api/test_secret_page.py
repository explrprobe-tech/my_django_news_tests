

def test_secret_page_with_auth(authenticated_session, base_url):
    
    response = authenticated_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "Секретная страница" in response.text