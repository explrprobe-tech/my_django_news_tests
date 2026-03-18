def test_secret_page_admin_user(admin_session, base_url):
    """Admin users should have access to secret page (200 OK)"""
    response = admin_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "SOLAR OBSERVATORY" in response.text

def test_secret_page_editor_user(editor_session, base_url):
    """Editor users should have access to secret page (200 OK)"""
    response = editor_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "SOLAR OBSERVATORY" in response.text

def test_secret_page_regular_user(regular_session, base_url):
    """Regular users should have access to secret page (403 OK)"""
    response = regular_session.get(f"{base_url}/secret/")
    assert response.status_code == 403
    
def test_secret_page_sun_data(editor_session, base_url):
    response = editor_session.get(f"{base_url}/secret/")
    assert 'Station' in response.text
    assert 'Observation' in response.text
    assert 'frequency' in response.text
    assert 'flux' in response.text
    assert 'observed_quality' in response.text