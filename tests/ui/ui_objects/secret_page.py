from .base_page import BasePage
from playwright.sync_api import Page



class SecretPage(BasePage):
    """UI methods for News add page"""

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.news_add_endpoint = "/secret/"
        self.news_add_url = f"{self.base_url}{self.news_add_endpoint}"

    def navigate(self):
        """Open Secret page"""
        self._navigate_to(self.news_add_endpoint)
        return self
    
    @property
    def secret_title(self):
        return self.page.locator(".container h1")
    
    @property
    def secret_solar_title(self):
        return self.page.locator(".container h2")
    
    @property
    def secret_solar_frequency_value(self):
        return self.page.locator(".data-item:nth-child(1) .data-value")
    
    @property
    def secret_solar_flux_value(self):
        return self.page.locator(".data-item:nth-child(2) .data-value")
                                 
    @property
    def secret_solar_observed_quality_value(self):
        return self.page.locator(".data-item:nth-child(3) .data-value")
    
    @property
    def secret_mars_title(self):
        return self.page.locator(".mars-header h3")
    
    @property
    def secret_mars_perseverance_value(self):
        return self.page.locator(".mars-info-item:nth-child(1) p").first
    
    @property
    def secret_mars_temperature_value(self):
        return self.page.locator(".mars-info-item:nth-child(2) p").first
    
    @property
    def secret_mars_season_value(self):
        return self.page.locator(".mars-info-item:nth-child(3) p").first
    
    @property
    def secret_mars_latest_discovery_value(self):
        return self.page.locator(".mars-info-item:nth-child(4) p").first