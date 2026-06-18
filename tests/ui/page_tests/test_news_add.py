import pytest
from playwright.sync_api import Page, expect
from helpers import object_delete
import allure


@allure.epic("page_tests")
@allure.feature("news_add")
@allure.severity(allure.severity_level.NORMAL)
class TestNewsAdd:

    @pytest.mark.parametrize("user", [
        "editor_user",
        "admin_user"
    ])
    def test_news_add_page(self, request, news_add_page, login_page, user):
        """Any user can see category page"""
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        news_add_page.navigate()
        expect(news_add_page.headers.logout_button).to_be_visible()
        expect(news_add_page.headers.user_role_text).to_be_visible()
        expect(news_add_page.news_title_title).to_be_visible()
        expect(news_add_page.news_title_field).to_be_visible()
        expect(news_add_page.news_title_hint).to_be_visible()
        expect(news_add_page.news_category_title).to_be_visible()
        expect(news_add_page.news_category_field).to_be_visible()
        expect(news_add_page.news_category_hint).to_be_visible()
        expect(news_add_page.news_short_description_title).to_be_visible()
        expect(news_add_page.news_short_description_field).to_be_visible()
        expect(news_add_page.news_short_description_hint).to_be_visible()
        expect(news_add_page.news_content_title).to_be_visible()
        expect(news_add_page.news_content_field).to_be_visible()
        expect(news_add_page.news_content_hint).to_be_visible()
        expect(news_add_page.news_image_title).to_be_visible()
        expect(news_add_page.news_image_field).to_be_visible()
        expect(news_add_page.news_image_hint).to_be_visible()
        expect(news_add_page.news_tags_title).to_be_visible()
        expect(news_add_page.news_tags_field).to_be_visible()
        expect(news_add_page.news_tags_hint).to_be_visible()
        expect(news_add_page.news_add_button).to_be_visible()
        expect(news_add_page.cancel_button).to_be_visible()

    @pytest.mark.parametrize("user", [
        "editor_user",
        "admin_user"
    ])
    def test_news_add(self, request, news_add_page, login_page, news_data, test_category, object_helper, user):
        """Any user can see category page"""
        import re
        user_data = request.getfixturevalue(user)
        login_page.login(user_data)
        news_add_page.news_add(news_data, test_category)
        expect(news_add_page.page).to_have_url(re.compile(rf"{news_add_page.base_url}/news/\d+/"))
        test_news_id = object_helper.get_object_id_by_name(model="news", name=news_data["title"])
        object_delete_response = object_helper.object_delete(test_news_id)
        assert object_delete_response.status_code == 200, "Test news should be deleted after tests"


    def test_news_add_editor_user(self, page: Page, base_url: str, editor_user):
        """Editor user can open add news page"""
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill(editor_user["username"])
        page.locator("#id_password").fill(editor_user["password"])
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        expect(page.locator("label[for='id_title']")).to_contain_text("Заголовок новости")
        expect(page.locator("#id_title")).to_be_visible()
        expect(page.locator(".hint-text").nth(0)).to_contain_text("Заголовок должен быть кратким и информативным")
        expect(page.locator("label[for='id_category']")).to_contain_text("Категория")
        expect(page.locator("#id_category")).to_be_visible()
        expect(page.locator(".hint-text").nth(1)).to_contain_text("Выберите наиболее подходящую категорию")
        expect(page.locator("label[for='id_short_description']")).to_contain_text("Краткое описание")
        expect(page.locator("#id_short_description")).to_be_visible()
        expect(page.locator(".hint-text").nth(2)).to_contain_text("Это описание будет отображаться в списке новостей")
        expect(page.locator("label[for='id_content']")).to_contain_text("Полный текст новости")
        expect(page.locator("#id_content")).to_be_visible()
        expect(page.locator(".hint-text").nth(3)).to_contain_text("Подробно опишите событие, добавьте детали и контекст")
        expect(page.locator("label[for='id_image']")).to_contain_text("Изображение (необязательно)")
        expect(page.locator("#id_image")).to_be_visible()
        expect(page.locator(".hint-text").nth(4)).to_contain_text("Рекомендуемый размер: 1200x630px. Максимальный размер: 5MB")
        expect(page.locator("label[for='id_tags']")).to_contain_text("Теги (через запятую)")
        expect(page.locator("#id_tags")).to_be_visible()
        expect(page.locator(".hint-text").nth(5)).to_contain_text("Теги помогут читателям находить похожие новости")
        expect(page.get_by_role("button", name="✨ Опубликовать новость")).to_be_visible()
        expect(page.get_by_role("link", name="❌ Отмена")).to_be_visible()
    def test_news_add_admin_user(self, page: Page, base_url: str, admin_user):
        """Admin user can open add news page"""
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill(admin_user["username"])
        page.locator("#id_password").fill(admin_user["password"])
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        expect(page.locator("label[for='id_title']")).to_contain_text("Заголовок новости")
        expect(page.locator("#id_title")).to_be_visible()
        expect(page.locator(".hint-text").nth(0)).to_contain_text("Заголовок должен быть кратким и информативным")
        expect(page.locator("label[for='id_category']")).to_contain_text("Категория")
        expect(page.locator("#id_category")).to_be_visible()
        expect(page.locator(".hint-text").nth(1)).to_contain_text("Выберите наиболее подходящую категорию")
        expect(page.locator("label[for='id_short_description']")).to_contain_text("Краткое описание")
        expect(page.locator("#id_short_description")).to_be_visible()
        expect(page.locator(".hint-text").nth(2)).to_contain_text("Это описание будет отображаться в списке новостей")
        expect(page.locator("label[for='id_content']")).to_contain_text("Полный текст новости")
        expect(page.locator("#id_content")).to_be_visible()
        expect(page.locator(".hint-text").nth(3)).to_contain_text("Подробно опишите событие, добавьте детали и контекст")
        expect(page.locator("label[for='id_image']")).to_contain_text("Изображение (необязательно)")
        expect(page.locator("#id_image")).to_be_visible()
        expect(page.locator(".hint-text").nth(4)).to_contain_text("Рекомендуемый размер: 1200x630px. Максимальный размер: 5MB")
        expect(page.locator("label[for='id_tags']")).to_contain_text("Теги (через запятую)")
        expect(page.locator("#id_tags")).to_be_visible()
        expect(page.locator(".hint-text").nth(5)).to_contain_text("Теги помогут читателям находить похожие новости")
        expect(page.get_by_role("button", name="✨ Опубликовать новость")).to_be_visible()
        expect(page.get_by_role("link", name="❌ Отмена")).to_be_visible()
    def test_news_add_create_news(self, page: Page, base_url: str, test_category, admin_session, news_data):
        """Editor user can create news with news add page"""
        import re
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill("autotest_editor")
        page.locator("#id_password").fill("autoeditor_123456789!")
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        page.locator("#id_title").fill(news_data["title"])
        page.locator("#id_category").select_option(test_category["test_category_id"])
        page.locator("#id_short_description").fill(news_data["short_description"])
        page.locator("#id_content").fill(news_data["content"])
        page.locator("#id_image").set_input_files(news_data["photo"])
        page.locator("#id_tags").fill(news_data["tags"])
        page.get_by_role("button", name="✨ Опубликовать новость").click()
        expect(page).to_have_url(re.compile(rf"{base_url}news/\d+/"))
        object_url = page.url
        object_delete(session=admin_session, url_object=object_url)
    def test_news_add_to_home_page(self, page: Page, base_url: str, editor_user):
        """Editor user can returb back to home page from news add page"""
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill(editor_user["username"])
        page.locator("#id_password").fill(editor_user["password"])
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        page.get_by_role("link", name="❌ Отмена").click()
        expect(page).to_have_url(base_url)
    def test_news_add_empty_fields(self, page: Page, base_url: str, editor_user):
        """Editor user can't create news with empty fields"""
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill(editor_user["username"])
        page.locator("#id_password").fill(editor_user["password"])
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        page.get_by_role("button", name="✨ Опубликовать новость").click()
        expect(page).to_have_url(f"{base_url}news/add_news/")
    def test_news_add_invalid_fields(self, page: Page, base_url: str, editor_user, news_data):
        """Editor user can't create news with incorrect fields"""
        page.goto(base_url)
        page.get_by_role("link", name="🔐 Войти").click()
        page.locator("#id_username").fill(editor_user["username"])
        page.locator("#id_password").fill(editor_user["password"])
        page.get_by_role("button", name="Войти").click()
        page.get_by_role("link", name="📰 Читать все новости").click()
        page.get_by_role("link", name="✍️ Добавить новость").click()
        page.locator("#id_title").fill("1")
        page.locator("#id_content").fill(news_data["content"])
        page.get_by_role("button", name="✨ Опубликовать новость").click()
        expect(page).to_have_url(f"{base_url}news/add_news/")
        expect(page.locator(".form-group:has(#id_title) .errorlist")).to_have_text("Name must not start with a number")
        expect(page.locator(".form-group:has(#id_category) .errorlist")).to_have_text("This field is required.")