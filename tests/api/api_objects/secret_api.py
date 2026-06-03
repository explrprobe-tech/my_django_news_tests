from .base_api import BaseApi

class SecretApi(BaseApi):
    """Api methods for secret page"""

    def get_secret(self, **kwargs):
        """To get secret page"""
        endpoint = "/secret/"
        return self._get(endpoint)