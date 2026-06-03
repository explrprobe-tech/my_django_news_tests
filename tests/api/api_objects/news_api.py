from .base_api import BaseApi

class NewsApi(BaseApi):
    """Api methods for News"""

    def get_news(self, **kwargs):
        """To get all news"""
        endpoint = "/news/"
        return self._get(endpoint, **kwargs)
    
    def get_news_by_id(self, news_id, **kwargs):
        """To get define news by id"""
        endpoint=f"/news/{news_id}/"
        return self._get(endpoint, **kwargs)
    
    def create_news(self, news_data, **kwargs):
        """Create new news"""
        import copy
        endpoint = "/news/add_news/"
        data_news = copy.deepcopy(news_data)
        csrf_token = self.get_csrf_token(endpoint)
        data_news["csrfmiddlewaretoken"] = csrf_token
        return self._post(endpoint, news_data, **kwargs)
    
    def delete_news(self, news_id, **kwargs):
        """Delete news by id"""
        endpoint=f"/news/{news_id}/delete/"
        csrf_endpoint = "/news/add_news/"
        csrf_token = self.get_csrf_token(csrf_endpoint)
        data_delete = {
            "csrfmiddlewaretoken": csrf_token
        }
        return self._post(endpoint, data_delete, **kwargs)