admin_user = {"username": "autotest_admin",
              "password": "autoadmin_123456789!"}
editor_user = {"username": "autotest_editor",
               "password": "autoeditor_123456789!"}
regular_user = {"username": "autotest_regular",
                "password": "autoregular_123456789!"}

def login_user(session, base_url, credentials, csrf_extractor):
    """Helper to login any user"""
    login_page = session.get(f"{base_url}/login/")
    csrf_token = csrf_extractor(login_page.text)
    
    response = session.post(
        f"{base_url}/login/",
        data={
            "csrfmiddlewaretoken": csrf_token,
            "username": credentials["username"],
            "password": credentials["password"]
        },
        headers={"Referer": f"{base_url}/login/"}
    )
    
    if response.status_code not in [200, 302]:
        pytest.skip(f"Could not login as {credentials['username']}")
    
    return session
    

def get_csrf_token(html_content: str):
    """Extract csrf token from HTML using regex"""
    import re
    match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html_content)
    return match.group(1) if match else None