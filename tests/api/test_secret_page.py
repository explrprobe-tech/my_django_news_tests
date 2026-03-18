import requests

def test_secret_page_admin_user(admin_session, base_url):
    """Autharizated user can open secret page"""
    response = admin_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "SOLAR OBSERVATORY" in response.text

def test_secret_page_editor_user(editor_session, base_url):
    """Autharizated user can open secret page"""
    response = editor_session.get(f"{base_url}/secret/")
    assert response.status_code == 200
    assert "SOLAR OBSERVATORY" in response.text

def test_secret_page_regular_user(regular_session, base_url):
    """Autharizated user can open secret page"""
    response = regular_session.get(f"{base_url}/secret/")
    assert response.status_code == 403
    
def test_secret_page_sun_data(editor_session, base_url):
    response = editor_session.get(f"{base_url}/secret/")
    sun_data = requests.get('https://services.swpc.noaa.gov/json/solar-radio-flux.json').json()[0]
    assert sun_data.get('time_tag') in response.text
    assert sun_data.get('common_name') in response.text
    assert str(sun_data.get('details')[0]['frequency']) in response.text
    assert str(sun_data.get('details')[0]['flux']) in response.text
    assert sun_data.get('details')[0]['observed_quality'] in response.text