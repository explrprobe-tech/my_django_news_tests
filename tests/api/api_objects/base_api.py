

class BaseApi:
    """Base class for all API objects"""

    def __init__(self, base_url, session = None):
        self.base_url = base_url.rstrip('/')
        self.session = session

    def set_session(self, session):
        self.session = session
        return self

    def _get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)
    
    def _post(self, endpoint, data, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, **kwargs)
    
    def _delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)
    
    def get_csrf_token(self, endpoint):
        """Extract csrf token from HTML using regex"""
        html_content = self.session.get(f"{self.base_url}{endpoint}").text
        import re
        match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html_content)
        return match.group(1) if match else None