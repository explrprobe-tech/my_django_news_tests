import requests
from bs4 import BeautifulSoup
from pathlib import Path

FILE_PATH = Path(__file__).parent

def login_user(session, base_url, credentials, csrf_extract):
    """Helper to login any user"""
    csrf_token = csrf_extract(session=session, url=f"{base_url}/login/")
    
    response = session.post(
        f"{base_url}/login/",
        data={
            "csrfmiddlewaretoken": csrf_token,
            "username": credentials["username"],
            "password": credentials["password"]
        },
        headers={"Referer": f"{base_url}login/"}
    )
    
    if response.status_code not in [200, 302]:
        pytest.skip(f"Could not login as {credentials['username']}")
    
    return session
    
def object_delete(session, url_object):
    """Uses delete method to delete object by url and return response"""
    url_delete_method = f"{url_object}delete/"
    csrftoken = session.cookies.get('csrftoken')
    response = session.post(url=url_delete_method, 
                                  data={
                                        'csrfmiddlewaretoken': csrftoken
                                       }
                                  )
    return response

def get_csrf_token(session, url: str):
    """Extract csrf token from HTML using regex"""
    html_content = session.get(url).text
    import re
    match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html_content)
    return match.group(1) if match else None

def get_object_id_by_name(session, base_url, model, name):
    """Get user ID by searching in Django admin panel
       Session should be admin"""
    object_path = {
        "user": "auth/user",
        "group": "auth/group",
        "category": "news/category",
        "news": "news/news"
    }
    import re
    search_url = f"{base_url}admin/{object_path[model]}/?q={name}"
    response = session.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_link = soup.find('a', string=name)
    match = re.search(r'/(\d+)/change/', search_link['href'])
    if match:
        return f"{model}/{match.group(1)}/"
    return None

class ResponseCapture:
    "Captures specific fields from response"
    def __init__(self):
        self.data = {}

    def capture(self, field):
        """Returns a handler that captures a specific key"""
        def handle_response(response):
            self.data[field] = response.json().get(field)
        return handle_response

    def get(self, field):
        return self.data.get(field)
    
class ObjectHelper:
    """Helps to work with objects"""
    
    OBJECT_PATHS = {
        "user": "auth/user",
        "group": "auth/group",
        "category": "news/category",
        "news": "news/news"
    }

    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        
    def get_object_id_by_name(self, model, name):
        """Get user ID by searching in Django admin panel
        Session should be admin"""
        object_path = self.OBJECT_PATHS[model]
        import re
        search_url = f"{self.base_url}admin/{object_path}/?q={name}"
        response = self.session.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_link = soup.find('a', string=name)
        match = re.search(r'/(\d+)/change/', search_link['href'])
        if match:
            return f"{model}/{match.group(1)}/"
        return None
    
    def object_delete(self, id_object):
        """Uses delete method to delete object by url and return response"""
        url_delete_method = f"{self.base_url}{id_object}delete/"
        csrftoken = self.session.cookies.get('csrftoken')
        response = self.session.post(url=url_delete_method, 
                                    data={
                                            'csrfmiddlewaretoken': csrftoken
                                        }
                                    )
        return response