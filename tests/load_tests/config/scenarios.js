import http from 'k6/http'
import { sleep, check } from 'k6'
import { urls } from './urls.js'

let editor_user = {
    'username': 'autotest_editor',
    'password': 'autoeditor_123456789!'
};

let admin_user = {
    'username': 'autotest_admin',
    'password': 'autoadmin_123456789!'
};

function getCsrfToken(session, url) {
    let response = session.get(url);
    let match = response.body.match(/name="csrfmiddlewaretoken" values="([^"]+)"/);
    return match ? match[1]: '';
};

function login(session, username, password) {
    let login_url = `${urls.login}${urls.base_url}`;
    let csrftoken = getCsrfToken(login_url);
    let user_login_response = session.post(login_url, {
        username: username,
        password: password,
        csrfmiddlewaretoken: csrftoken,
    });
    return user_login_response;
};

export function editorAuthentication() {
    let home_page = `${urls.base_url}`;
    let home_page_response = http.get(home_page);
    check(home_page_response, {
        'Home page response is 200:': (r) => r.status === 200,
        'Home page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let login_page = `${urls.base_url}${urls.login}`;
    let login_page_response = http.get(login_page);
    check(login_page_response, {
        'Login page is 200:': (r) => r.status === 200,
        'Login page is not empty:': (r) => r.body.includes('auth-form'),
    });
    sleep(2);

    let session = hhtp;
    let editor_login_response = login(session, editor_user.username, editor_user.password);
    check(editor_login_response, {
        'Editor login is 302': (r) => r.status === 302,
    });
    sleep(1);
};

export function adminAuthentication() {
    let home_page = `${urls.base_url}`;
    let home_page_response = http.get(home_page);
    check(home_page_response, {
        'Home page response is 200:': (r) => r.status === 200,
        'Home page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let login_page = `${urls.base_url}${urls.login}`;
    let login_page_response = http.get(login_page);
    check(login_page_response, {
        'Login page is 200:': (r) => r.status === 200,
        'Login page is not empty:': (r) => r.body.includes('auth-form'),
    });
    sleep(2);

    let session = hhtp;
    let admin_login_response = login(session, admin_user.username, admin_user.password);
    check(admin_login_response, {
        'Admin login is 302': (r) => r.status === 302,
    });
    sleep(1);
};

export function readersFlow() {
    let home_page = `${urls.base_url}`;
    let home_page_response = http.get(home_page);
    check(home_page_response, {
        'Home page response is 200:': (r) => r.status === 200,
        'Home page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let categories_list_page = `${urls.base_url}${urls.categories_list}`;
    let category_list_page_response = http.get(categories_list_page);
    check(category_list_page_response, {
        'Category list page response is 200:': (r) => r.status === 200,
        'Category list page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let category_news_page = `${urls.base_url}${urls.category_news(1)}`;
    let category_news_page_response = http.get(category_news_page);
    check(category_news_page_response, {
        'Category news page is 200:': (r) => r.status === 200,
        'Category news page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(2);

    let news_details_page = `${urls.base_url}${urls.news_details(1)}`;
    let news_details_page_response = http.get(news_details_page);
    check(news_details_page_response, {
        'News details page is 200:': (r) => r.status === 200,
        'News details page is not empty:': (r) => r.body.includes('news-detail-title'),
    });
    sleep(5);

    let news_page = `${urls.base_url}${urls.news}`;
    let news_page_response = http.get(news_page);
    check(news_page_response, {
        'News page is 200': (r) => r.status === 200,
        'News page is not empty:': (r) => r.body.includes('news-card')
    });
};

export function editorsFlow() {
    let home_page = `${urls.base_url}`;
    let home_page_response = http.get(home_page);
    check(home_page_response, {
        'Home page response is 200:': (r) => r.status === 200,
        'Home page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let categories_list_page = `${urls.base_url}${urls.categories_list}`;
    let category_list_page_response = http.get(categories_list_page);
    check(category_list_page_response, {
        'Category list page response is 200:': (r) => r.status === 200,
        'Category list page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let add_category_page = `${urls.base_url}${urls.add_category}`;
    let add_category_page_response = http.get(add_category);
    check(add_category_page_response, {
        'Add category page is 200:': (r) => r.status === 200,
        'Add category page is not empty:': (r) => r.body.includes('category-form')
    });
    sleep(1);

    let timestamp = Date.now();
    let add_category = `${urls.base_url}${urls.add_category}`;
    let add_category_response = http.post(add_category, {
        'title': `Title for test category ${timestamp}`,
        'csrfmiddlewaretoken': getCsrfToken(http, add_category)
    });
    check(add_category_response, {
        'Add category response is 200': (r) => r.status === 200,
    });
    sleep(1);

    let news_page = `${urls.base_url}${urls.news}`;
    let news_page_response = http.get(news_page);
    check(news_page_response, {
        'News page is 200': (r) => r.status === 200,
        'News page is not empty:': (r) => r.body.includes('news-card'),
    });
    sleep(2)

    let add_news_page = `${urls.base_url}${urls.add_news}`;
    let add_news_page_response = http.get(add_news_page);
    check(add_news_page_response, {
        'Add news page is 200': (r) => r.status === 200,
        'Add news page is not empty:': (r) => r.body.includes('news-form'),
    });
    let location = add_category_response.headers['Location'];
    let categoryId = location.match(/\/category\/(\d+)\//)[1];
    sleep(3)

    let add_news = `${urls.base_url}${urls.add_news}`;
    let add_news_response = http.post(add_news, {
        "title": "Title for test news",
        "content": "Content for test news",
        "is_published": True,
        "short_description": "Short description for test news",
        "tags": "test_tag_one, test_tag_two",
        "category": categoryId,
    });
    check(add_news_response, {
        'Add news response is 200:': (r) => r.status === 200,
    });
}