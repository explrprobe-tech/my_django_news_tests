import { BaseApi } from "../pages/base_api.js";
import { CategoryApi } from "../pages/category_api.js";
import { HomeApi } from "../pages/home_api.js";
import { LoginApi } from "../pages/login_api.js";
import { NewsApi } from "../pages/news_api.js";
import { sleep } from 'k6'

let editor_user = {
    username: 'autotest_editor',
    password: 'autoeditor_123456789!'
};

let admin_user = {
    username: 'autotest_admin',
    password: 'autoadmin_123456789!'
};

function authentication(user_data) {
    let home_api = new HomeApi;
    let login_api = new LoginApi;

    let home_page_response = home_api.openHomePage();
    home_api.checkOpenHomePage(home_page_response);
    sleep(1);

    let login_page_response = login_api.openLoginPage();
    login_api.checkOpenLoginPage(login_page_response);
    sleep(1);

    let login_editor_response = login_api.login(user_data);
    login_api.checkLogin(login_editor_response);
    sleep(1);
};

function getObjectId(object_response, object_type) {
    let location = object_response.headers['Location'];
    let regex = new RegExp(`\\/${object_type}\\/(\\d+)\\/`, 'i');
    let match = location ? location.match(regex) : null;
    return match ? match[1] : null;
}

function editorAuthentication() {
    authentication(editor_user);
}

function adminAuthentication() {
    authentication(admin_user);
}

function readersFlow() {
    let home_api = new HomeApi;
    let category_api = new CategoryApi;
    let news_api = new NewsApi;

    let home_page_response = home_api.openHomePage();
    home_api.checkOpenHomePage(home_page_response);
    sleep(2);

    let category_page_response = category_api.openCategoryPage();
    category_api.checkOpenCategoryPage(category_page_response);
    sleep(2);

    let category_news_page_response = category_api.openCategoryNewsPage(1);
    category_api.checkOpenCategoryNewsPage(category_news_page_response);
    sleep(2);

    let news_details_page_response = news_api.openNewsDetailsPage(1);
    news_api.checkNewsDetailsPage(news_details_page_response);
    sleep(3);

    let news_page_response = news_api.openNewsPage();
    news_api.checkOpenNewsPage(news_page_response);
    sleep(2);
};

function editorsFlow() {
    let home_api = new HomeApi;
    let category_api = new CategoryApi;
    let news_api = new NewsApi;

    let home_page_response = home_api.openHomePage();
    home_api.checkOpenHomePage(home_page_response);
    sleep(2);

    let category_page_response = category_api.openCategoryPage();
    category_api.checkOpenCategoryPage(category_page_response);
    sleep(2);

    let add_category_page = category_api.openAddCategoryPage();
    category_api.checkOpenAddCategoryPage(add_category_page);
    sleep(3);

    let add_category_response = category_api.addCategory();
    category_api.checkAddCategory(add_category_response);
    sleep(1);

    let news_page_response = news_api.openNewsPage();
    news_api.checkOpenNewsPage(news_page_response);
    sleep(2);

    let add_news_page_response = news_api.openAddNewsPage();
    news_api.checkOpenAddNewsPage(add_news_page_response);
    sleep(4);

    let category_id = getObjectId(add_category_response, 'category')
    let add_news_response = news_api.addNews(category_id);
    news_api.checkAddNews(add_news_response);
    sleep(1);
}

export function testReadersFlow() {
    readersFlow();
}

export function testEditorFlow() {
    editorAuthentication();
    editorsFlow();
}

export function testAdminFlow() {
    adminAuthentication();
}