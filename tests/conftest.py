import pytest
import requests
from faker import Faker
from helpers import login_user, get_csrf_token, object_delete, FILE_PATH, ObjectHelper
import re
from api.api_objects.user_api import AuthApi, UserApi
from api.api_objects.category_api import CategoryApi
from api.api_objects.news_api import NewsApi
from api.api_objects.secret_api import SecretApi
from playwright.sync_api import Page
from ui.ui_objects.home_page import HomePage
from ui.ui_objects.login_page import LoginPage
from ui.ui_objects.register_page import RegisterPage
from ui.ui_objects.category_add_page import CategoryAddPage
from ui.ui_objects.category_page import CategoryPage
from ui.ui_objects.category_news_page import CategoryNewsPage
from ui.ui_objects.news_page import NewsPage
from ui.ui_objects.news_edit_page import NewsEditPage
from ui.ui_objects.news_detail_page import NewsDetailPage
from ui.ui_objects.news_add_page import NewsAddPage
from ui.ui_objects.secret_page import SecretPage
import allure
import time
import os
from datetime import datetime
from playwright.sync_api import Page




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
def empty_user():
    """Empty user data"""
    test_empty_user = {
        "username": "",
        "password": ""
        }
    return test_empty_user

@pytest.fixture
def undefined_user():
    """Undefined autotest data"""
    test_undefined_user = {
        "username": "autotest_undefined",
        "password": "autoundefined_123456789!"
        }
    return test_undefined_user

@pytest.fixture
def admin_user():
    """Admin autotest data"""
    test_admin_user = {
        "username": "autotest_admin",
        "password": "autoadmin_123456789!"
        }
    return test_admin_user

@pytest.fixture
def editor_user():
    """Editor autotest data"""
    test_editor_user = {
        "username": "autotest_editor",
        "password": "autoeditor_123456789!"
        }
    return test_editor_user

@pytest.fixture
def regular_user():
    """Regular autotest data"""
    test_regular_data = {
        "username": "autotest_regular",
        "password": "autoregular_123456789!"
        }
    return test_regular_data

@pytest.fixture
def news_data():
    """News data for UI"""
    test_news_data = {
        "title": "Title for test news",
        "content": "Content for test news",
        "is_published": True,
        "photo": FILE_PATH / "files_for_tests" / "picture_or_photo.jpg",
        "short_description": "Short description for test news",
        "tags": "test_tag_one, test_tag_two"
        }
    return test_news_data

@pytest.fixture
def category_data():
    test_category_data = {
        "title": "Title for test category"
    }
    return test_category_data

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
def user_data_empty_username():
    """Provides user data"""
    test_user_data = {
        "username": " ",
        "email": "test_autouser_ui@example.ru",
        "password1": "autouserui_123456789!",
        "password2": "autouserui_123456789!"
    }
    return test_user_data

@pytest.fixture
def user_data_username_and_password_similar():
    """Provides user data"""
    test_user_data = {
        "username": "test_autouser_ui",
        "email": "test_autouser_ui@example.ru",
        "password1": "test_autouser_ui",
        "password2": "test_autouser_ui"
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
def admin_session(base_url, admin_user):
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
def editor_session(base_url, editor_user):
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
def regular_session(base_url, regular_user):
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
    test_user_delete_endpoint = f"/user/{test_user_id}/delete/"
    yield {
        "test_user_url": test_user_url,
        "test_user_data": test_user_data,
        "test_user_id": test_user_id,
        "test_user_delete_endpoint": test_user_delete_endpoint
    }
    object_delete(session=admin_session, url_object=test_user_url)

@pytest.fixture
def test_category(base_url, fake, admin_user):
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
def test_news(base_url, test_category, fake, admin_user):
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
    photo_path = FILE_PATH / "files_for_tests" / "picture_or_photo.jpg"
    with open(photo_path, 'rb') as photo:
        file = {"photo": photo}
        response_test_news = session.post(url=url, data=test_news_data, files=file)
    test_news_id = re.search(r'/news/(\d+)/', response_test_news.url).group(1)
    yield {
        "test_news_url": response_test_news.url,
        "test_news_data": test_news_data,
        "test_news_id": test_news_id
    }
    session.post(url=f"{response_test_news.url}delete/", data={"csrfmiddlewaretoken": csrf_token})


@pytest.fixture
def db_cleanup(admin_user):
    """Fixture that deletes objects by url"""
    created_objects = []
    def cleanup(url_object):
        created_objects.append(url_object)
    yield cleanup
    session = requests.Session()
    admin_creditianals = admin_user
    login_user(session, base_url, admin_creditianals, get_csrf_token)
    for url in created_objects:
        csrf_token = get_csrf_token(session=session, url=url)
        session.post(url=f"{url}delete/", data={"csrfmiddlewaretoken": csrf_token})

@pytest.fixture
def auth_api(base_url, unauthenticated_session):
    """Create AuthApi object for with auth methods"""
    return AuthApi(base_url, unauthenticated_session)

@pytest.fixture
def object_helper(base_url, admin_session):
    """Create ObjectHelper object with helper methods"""
    return ObjectHelper(base_url, admin_session)

@pytest.fixture
def user_api(base_url):
    """Create UserApi object with user methods"""
    return UserApi(base_url)

@pytest.fixture
def category_api(base_url):
    """Create CategoryApi object with category methods"""
    return CategoryApi(base_url)

@pytest.fixture
def news_api(base_url):
    """Create NewsApi object with news methods"""
    return NewsApi(base_url)

@pytest.fixture
def secret_api(base_url):
    """Create SecretApi object with secret api methods"""
    return SecretApi(base_url)

@pytest.fixture
def home_page(page: Page, base_url):
    """Create HomePage object with home page methods"""
    return HomePage(page, base_url)

@pytest.fixture
def login_page(page: Page, base_url):
    """Create LoginPage object with login page methods"""
    return LoginPage(page, base_url)

@pytest.fixture
def register_page(page: Page, base_url):
    """Create RegisterPage object with register page methos"""
    return RegisterPage(page, base_url)

@pytest.fixture
def category_add_page(page: Page, base_url):
    """Create CategoryAddPage object with Category Add page methods"""
    return CategoryAddPage(page, base_url)

@pytest.fixture
def category_page(page: Page, base_url):
    """Create CategoryPage object with Category page methods"""
    return CategoryPage(page, base_url)

@pytest.fixture
def category_news_page(page: Page, base_url):
    """Create CategoryNewsPage object with Category news page methods"""
    return CategoryNewsPage(page, base_url)

@pytest.fixture
def news_page(page: Page, base_url):
    """Create NewsPage object with News page methods"""
    return NewsPage(page, base_url)

@pytest.fixture
def news_edit_page(page: Page, base_url):
    """Create NewsEditPage object with News edit page methods"""
    return NewsEditPage(page, base_url)

@pytest.fixture
def news_detail_page(page: Page, base_url):
    """Create NewsDetailPage object with News detail page methods"""
    return NewsDetailPage(page, base_url)

@pytest.fixture
def news_add_page(page: Page, base_url):
    """Create NewsAddPage object with News add page methods"""
    return NewsAddPage(page, base_url)

@pytest.fixture
def secret_page(page: Page, base_url):
    """Create SecretPage object with Secret page methods"""
    return SecretPage(page, base_url)


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

def pytest_sessionfinish(session, exitstatus):
    """Generate environment properties for Allure report"""
    allure_dir = "allure-results"
    os.makedirs(allure_dir, exist_ok=True)
    
    with open(f"{allure_dir}/environment.properties", "w") as f:
        f.write(f"Browser=Chromium\n")
        f.write(f"Base_URL={os.environ.get('BASE_URL', 'http://localhost:8000')}\n")
        f.write(f"Test_Environment=Staging\n")
        f.write(f"Python_Version={os.sys.version}\n")
        f.write(f"Test_Date={datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
            screenshot_dir = "allure-results/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            
            screenshot_path = f"{screenshot_dir}/{item.name}_{datetime.now()}.png"
            page.screenshot(path=screenshot_path)
            
            allure.attach.file(
                screenshot_path,
                name=f"Failed: {item.name}",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Add dynamic test title to Allure"""
    item._start_time = time.perf_counter()
    if hasattr(item, 'callspec'):
        params = item.callspec.params
        if params:
            param_str = ", ".join([f"{k}={v}" for k, v in params.items()])
            allure.dynamic.title(f"{item.name} [{param_str}]")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item):
    """Runs after each test"""
    if hasattr(item, '_start_time'):
        duration = time.perf_counter() - item._start_time
        allure.attach(
            f"Test duration: {duration:.3f}s",
            name="⏱️ Execution Time",
            attachment_type=allure.attachment_type.TEXT
        )
        if duration > 5:
            allure.attach(
                f"⚠️ Test took {duration:.3f}s (over 5s threshold)",
                name="⚠️ Performance Warning",
                attachment_type=allure.attachment_type.TEXT
            )
    print(f"\nFinished test: {item.name}")
