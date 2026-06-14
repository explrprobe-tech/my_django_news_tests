import { BaseApi } from "./base_api.js";
import { urls } from '../config/urls.js'
import { check } from 'k6';

export class CategoryApi extends BaseApi {

    constructor(category_endpoint = urls.categories_list,
        category_news_endpoint = urls.category_news,
        add_category_endpoint = urls.add_category,
    ) {
        super();
        this.category_endpoint = category_endpoint;
        this.category_news_endpoint = category_news_endpoint;
        this.add_category_endpoint = add_category_endpoint;
    }

    openCategoryPage() {
        return this._get(this.category_endpoint);
    }

    checkOpenCategoryPage(response) {
        return check (response, {
            "Open Category page is 200": (r) => r.status === 200
        });
    }

    openCategoryNewsPage(news_id) {
        return this._get(this.category_news_endpoint(news_id));
    }

    checkOpenCategoryNewsPage(response) {
        return check(response, {
            "Open Category News page is 200": (r) => r.status === 200
        });
    }

    openAddCategoryPage() {
        return this._get(this.add_category_endpoint);
    }

    checkOpenAddCategoryPage(response) {
        return check(response, {
            "Open Add Category page is 200": (r) => r.status === 200
        });
    }

    addCategory() {
        let random_value = Math.random().toString(36).substring(2, 6); 
        let data = {
            title: `Load test category title - ${random_value}`
        };
        return this._post(this.add_category_endpoint, data)
    }

    checkAddCategory(response) {
        return check(response, {
            "Add Category is 302": (r) => r.status === 302
        });
    }
}