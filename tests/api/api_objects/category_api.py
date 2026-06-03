from .base_api import BaseApi

class CategoryApi(BaseApi):
    """Api methods for Category"""

    def get_categories(self, **kwargs):
        """Get all categories"""
        endpoint = '/category/'
        return self._get(endpoint, **kwargs)
    
    def get_news_by_category(self, category_id, **kwargs):
        """Get all news belong to category"""
        endpoint = f"/category/{category_id}/"
        return self._get(endpoint, **kwargs)
    
    def create_category(self, category_data, **kwargs):
        """Create category without news"""
        import copy
        endpoint = "/category/add_category/"
        data = copy.deepcopy(category_data)
        csrf_token = self.get_csrf_token(endpoint)
        data["csrfmiddlewaretoken"] = csrf_token
        return self._post(endpoint, data, **kwargs)
    
    def delete_category(self, category_id, **kwargs):
        """Delete category """
        endpoint = f"/category/{category_id}/delete/"
        csrf_endpoint = "/category/add_category/"
        csrf_token = self.get_csrf_token(csrf_endpoint)
        data = {"csrfmiddlewaretoken": csrf_token}
        return self._post(endpoint, data, **kwargs)