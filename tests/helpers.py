

def get_csrf_token(html_content: str):
    """Extract csrf token from HTML using regex"""
    import re
    match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html_content)
    return match.group(1) if match else None