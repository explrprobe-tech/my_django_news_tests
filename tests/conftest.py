import pytest
import requests
from typing import Dict, Any, Generator
from faker import Faker
from helpers import get_csrf_token



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

@pytest.fixture
def test_user_data(fake) -> Dict[str, str]:
    """Generate random test user data"""
    return {
        "username": fake.user_name(),
        "password": fake.password(),
        "email": fake.email()
    }

@pytest.fixture
def admin_user() -> Dict[str, str]:
    """Provides admin user data"""
    return {
        "username": "admin123",
        "password": "admin123",
        "email": "admin@example.com"
    }   

@pytest.fixture
def test_news_data(fake) -> Dict[str, str]:
    """Generate random test news data"""
    return {
        "title": fake.sentence(nb_words=6),
        "content": "\n\n".join(fake.paragraphs(nb=3)),
        "short_description": fake.sentence(nb_words=15),
        "is_published": True
    }

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

@pytest.fixture(scope="session")
def registered_user(http_session: requests.Session,
                    base_url: str):
    """Creates user if it doesn't exist"""
    username = "autotest_user"
    password = "auto_123"

    register_url = f"{base_url}/register/"
    register_page_response = http_session.get(register_url)
    csrf_token = get_csrf_token(register_page_response.text)
    register_data ={
        "csrfmiddlewaretoken": csrf_token,
        "username": username,
        "password1": password,
        "password2": password,
        "email": "autotests_user@example.ru"
    }
    headers = {
        "Referer": register_url,
        "X-CSRFToken": csrf_token
    }
    http_session.post(register_url,
                          data=register_data,
                          headers=headers)
    return {"username": username, "password": password}


@pytest.fixture
def authenticated_session(
    http_session: requests.Session,
    registered_user: Dict,
    base_url: str,
    test_user_data: Dict
) -> Generator[requests.Session, None, None]:
    """Creates a session that is logged in"""
    print(f"\n🔐 Setting up authenticated session for {test_user_data['username']}")

    # Login
    login_url = f"{base_url}/login/"
    login_page = http_session.get(login_url)
    csrf_token = get_csrf_token(login_page.text)
    login_data = {
        "csrfmiddlewaretoken": csrf_token,
        "username": registered_user["username"],
        "password": registered_user["password"]
    }
    headers = {
        "Referer": login_url,
        "X-CSRFToken": csrf_token
    }
    response = http_session.post(login_url,
                                 data=login_data,
                                 headers=headers)

    if response.status_code != 200:
        pytest.skip(f"Could not login: {response.status_code}")

    print(f"Successfully authenticated as {test_user_data['username']}")

    # GIVE THE SESSION TO THE TEST
    yield http_session

    # CLEANUP (after test)
    print(f"Cleaning up authenticated session")
    http_session.get(f"{base_url}/logout/")

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
