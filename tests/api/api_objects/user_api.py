from .base_api import BaseApi

class AuthApi(BaseApi):
    """Api methods for registration"""

    def register(self, username, password, email):
        """Registration user"""
        url = '/register/'
        csrf_token = self.get_csrf_token(url)
        data_register = {
            'username': username,
            'password1': password,
            'password2': password,
            'email': email,
            'csrfmiddlewaretoken': csrf_token
        }
        return self._post(url, data_register)
    
    def login(self, username, password):
        """Authentication user"""
        url = '/login/'
        csrf_token = self.get_csrf_token(url)
        data_login = {
            'username': username,
            'password': password,
            'csrfmiddlewaretoken': csrf_token
        }
        return self._post(url, data_login, allow_redirects=False)
    
    
class UserApi(BaseApi):
    """Api methods for User"""

    def delete_user(self, endpoint, **kwargs):
        """Delition user"""
        csrf_token = self.session.cookies.get("csrftoken")
        data_delete = {
            'csrfmiddlewaretoken': csrf_token
        }
        return self._post(endpoint, data_delete, **kwargs)
    
    def logout(self, **kwargs):
        """Logout user"""
        url = '/logout/'
        return self._get(url, **kwargs)