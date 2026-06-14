import { BaseApi } from "./base_api.js";
import { urls } from '../config/urls.js'
import { check } from 'k6';

export class NewsApi extends BaseApi {
    
    constructor(news_endpoint=urls.news,
        news_details_endpoint=urls.news_details,
        add_news_endpoint=urls.add_news,
        edit_news_endpoint=urls.edit_news) {
            super();
            this.news_endpoint = news_endpoint;
            this.news_details_endpoint = news_details_endpoint;
            this.add_news_endpoint = add_news_endpoint;
            this.edit_news_endpoint = edit_news_endpoint;
        }

    openNewsPage() {
        return this._get(this.news_endpoint)
    }

    checkOpenNewsPage(response) {
        return check(response, {
            'Open News page is 200': (r) => r.status === 200
        });
    }

    openNewsDetailsPage(news_id) {
        return this._get(this.news_details_endpoint(news_id))
    }

    checkNewsDetailsPage(response) {
        return check(response, {
            'Open News Detail page is 200': (r) => r.status === 200
        })
    }

    openAddNewsPage() {
        return this._get(this.add_news_endpoint)
    }

    checkOpenAddNewsPage(response) {
        return check(response, {
            'Open Add News page is 200': (r) => r.status === 200
        });
    }

    addNews(category_id) {
        let random_value = Math.random().toString(36).substring(2, 6); 
        let data = {
            title: `Load test title - ${random_value}`,
            content: `Load test content - ${random_value}`,
            short_description: `Load test short_descriptioon - ${random_value}`,
            category: category_id,
            is_public: true,
        };
        return this._post(this.add_news_endpoint, data)
    }

    checkAddNews(response) {
        return check(response, {
            'Add News is 302': (r) => r.status === 302
        });
    }

    openEditNewsPage(news_id) {
        return this._get(this.edit_news_endpoint)
    }

    checkOpenEditNewsPage(response) {
        return check(response, {
            'Open Edit News page is 200': (r) => r.status === 200
        });
    }

    editNews(news_id) {
        let random_value = Math.random().toString(36).substring(2, 6); 
        let data = {
            title: `Load test edit title - ${random_value}`,
            content: `Load test edit content - ${random_value}`,
            short_description: `Load test edit short_descriptioon - ${random_value}`,
            category: category_id,
            is_public: true,
        };
        return this._post(this.edit_news_endpoint(news_id), data)
    }

    checkEditNews(response) {
        return check(response, {
            'Edit News is 302': (r) => r.status === 302
        });
    }

}