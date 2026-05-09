import pytest
from playwright.sync_api import Page, expect

def test_category_add_editor_user(page: Page, base_url: str):
    """Editor user can open category add page"""