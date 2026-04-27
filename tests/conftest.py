import pytest
import requests
from typing import Dict, Any, Generator
from faker import Faker
from helpers import admin_user, editor_user, regular_user, login_user, get_csrf_token, object_delete
import re



@pytest.fixture(scope="session")
def base_url() -> str:
    """Base url for all tests (created once for session)."""
    return "http://127.0.0.1:8000/"

@pytest.fixture(scope="session")
def api_url(base_url: str) -> str:
    """Provides API URL."""
    return f"{base_url}api"

@pytest.fixture
def fake() -> Faker:
    """Provides a Faker instance for generating fake data.
       Create fresh for each test that needs it."""
    return Faker()

@pytest.fixture
def user_data():
    """Provides user data"""
    test_user_data = {
        "username": "test_autouser_ui",
        "email": "test_autouser_ui@example.ru",
        "password1": "autouserui_123456789!",
        "password2": "autouserui_123456789!"
    }
    return test_user_data

@pytest.fixture
def unauthenticated_session():
    """Returns clean session (not logged in)"""
    session = requests.Session()
    session.cookies.clear()
    session.headers.update({
        "User-Agent": "MyAutotestBot/1.0",
        "Accept": "application/json"
    })
    return session

@pytest.fixture
def admin_session(base_url):
    """Session for admin user"""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "MyAutotestBot/1.0",
        "Accept": "application/json"
    })
    credentials = admin_user
    session = login_user(session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}logout/")

@pytest.fixture
def editor_session(base_url):
    """Session for editor user"""
    session = requests.Session()
    session.cookies.clear()
    session.headers.update({
        "User-Agent": "MyAutotestBot/1.0",
        "Accept": "application/json"
    })
    credentials = editor_user
    session = login_user(session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}logout/")

@pytest.fixture
def regular_session(base_url):
    """Session for regular user"""
    session = requests.Session()
    session.cookies.clear()
    session.headers.update({
        "User-Agent": "MyAutotestBot/1.0",
        "Accept": "application/json"
    })
    credentials = regular_user
    session = login_user(session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}logout/")

@pytest.fixture
def test_user(base_url, unauthenticated_session, admin_session):
    """Create test_user"""
    url = f"{base_url}register/"
    csrf_token = get_csrf_token(session=unauthenticated_session, url=url)
    test_user_data = {
        "username": "Fixture_test_user",
        "password1": "Test_user_password_12345",
        "password2": "Test_user_password_12345",
        "email": "fixture_test_user@example.ru",
        "csrfmiddlewaretoken": csrf_token
    }
    response_test_user = unauthenticated_session.post(url=url, data=test_user_data)
    test_user_url = f"{base_url}{response_test_user.json().get('user_id')}"
    test_user_id = re.search(r'/user/(\d+)/', test_user_url).group(1)
    yield {
        "test_user_url": test_user_url,
        "test_user_data": test_user_data,
        "test_user_id": test_user_id
    }
    object_delete(session=admin_session, url_object=test_user_url)

@pytest.fixture
def test_category(base_url, fake):
    """Create category and return category url, data, id"""
    url = f"{base_url}category/add_category/"
    session = requests.Session()
    admin_creditianals = admin_user
    login_user(session, base_url, admin_creditianals, get_csrf_token)
    csrf_token = get_csrf_token(session=session, url=url)
    test_category_data = {
        "title": fake.word().capitalize(),
        "csrfmiddlewaretoken": csrf_token
    }
    response_test_category = session.post(url=url, data=test_category_data)
    test_category_id = re.search(r'/category/(\d+)/', response_test_category.url).group(1)
    yield {
        "test_category_url": response_test_category.url,
        "test_category_data": test_category_data,
        "test_category_id": test_category_id
    }
    session.post(url=f"{response_test_category.url}delete/", data={"csrfmiddlewaretoken": csrf_token})

@pytest.fixture
def test_news(base_url, test_category, fake):
    """Create news and return news url, data, id"""
    url = f"{base_url}news/add_news/"
    session = requests.Session()
    admin_creditianals = admin_user
    login_user(session, base_url, admin_creditianals, get_csrf_token)
    csrf_token = get_csrf_token(session=session, url=url)
    test_news_data = {
        "title": fake.sentence(nb_words=6),
        "content": "\n\n".join(fake.paragraphs(nb=3)),
        "short_description": fake.sentence(nb_words=15),
        "category": test_category["test_category_id"],
        "is_published": True,
        "csrfmiddlewaretoken": csrf_token
    }
    response_test_news = session.post(url=url, data=test_news_data)
    test_news_id = re.search(r'/news/(\d+)/', response_test_news.url).group(1)
    yield {
        "test_news_url": response_test_news.url,
        "test_news_data": test_news_data,
        "test_news_id": test_news_id
    }
    session.post(url=f"{response_test_news.url}delete/", data={"csrfmiddlewaretoken": csrf_token})

@pytest.fixture
def db_cleanup():
    """Fixture that ensures database is clean"""
    yield

def pytest_configure(config):
    """Function to register custom markers"""
    config.addinivalue_line(
        "markers",
        "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers",
        "smoke: marks tests as smoke tests (run critical tests first)"
    )

def pytest_runtest_setup(item):
    """Runs before each test"""
    print(f"\nStarting test: {item.name}")

def pytest_runtest_teardown(item):
    """Runs after each test"""
    print(f"\nFinished test: {item.name}")
