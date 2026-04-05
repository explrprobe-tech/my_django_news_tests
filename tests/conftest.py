import pytest
import requests
from typing import Dict, Any, Generator
from faker import Faker
from helpers import admin_user, editor_user, regular_user, login_user, get_csrf_token



@pytest.fixture(scope="session")
def base_url() -> str:
    """Base url for all tests (created once for session)."""
    return "http://127.0.0.1:8000/"

@pytest.fixture(scope="session")
def api_url(base_url: str) -> str:
    """Provides API URL."""
    return f"{base_url}/api"

@pytest.fixture
def fake() -> Faker:
    """Provides a Faker instance for generating fake data.
       Create fresh for each test that needs it."""
    return Faker()

@pytest.fixture(scope="session")
def http_session() -> requests.Session:
    """Creates a requests session that can be reused"""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "MyAutotestBot/1.0",
        "Accept": "application/json"
    })
    return session

@pytest.fixture
def unauthenticated_session(http_session: requests.Session) -> requests.Session:
    """Returns clean session (not logged in)"""
    return http_session

@pytest.fixture
def admin_session(http_session, base_url):
    """Session for admin user"""
    credentials = admin_user
    session = login_user(http_session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}/logout/")

@pytest.fixture
def editor_session(http_session, base_url):
    """Session for editor user"""
    credentials = editor_user
    session = login_user(http_session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}/logout/")

@pytest.fixture
def regular_session(http_session, base_url):
    """Session for regular user"""
    credentials = regular_user
    session = login_user(http_session, base_url, credentials, get_csrf_token)
    yield session
    session.get(f"{base_url}/logout/")

@pytest.fixture
def test_category_data(fake):
    """Generate random category title"""
    return {
        "title": fake.word().capitalize()
    }

@pytest.fixture
def test_category_url(test_category_data: Dict[str, str], editor_session, base_url):
    """Create category and return category id"""
    url = f"{base_url}/category/add_category/"
    csrf_token = get_csrf_token(session=editor_session, url=url)
    test_category_data["csrfmiddlewaretoken"] = csrf_token
    category_id = editor_session.post(url=url, data=test_category_data)
    yield category_id.url
    #NEED TO DO HERE autodeletion
@pytest.fixture
def test_news_data(fake, test_category_id) -> Dict[str, str]:
    """Generate random test news data"""
    return {
        "title": fake.sentence(nb_words=6),
        "content": "\n\n".join(fake.paragraphs(nb=3)),
        "short_description": fake.sentence(nb_words=15),
        "category": test_category_id,
        "is_published": True
    }

@pytest.fixture
def test_news_url(test_news_data: Dict, editor_session, base_url):
    """Create news and return news id"""
    url = f"{base_url}/add_news/"
    news_id = editor_session.post(url=url, data=test_news_data)
    return news_id.url #replace for yield and add cleaner

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
