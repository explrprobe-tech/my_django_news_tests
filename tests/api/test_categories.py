def test_categories_news_by_category(editor_session, test_category_url):
    """Unauthorized user can see all categories"""
    response = editor_session.get(url=test_category_url)
    print(response)