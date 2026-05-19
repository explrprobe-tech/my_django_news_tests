import http from 'k6/http'
import { sleep, check } from 'k6'
import { urls } from './config/urls.js'

export let options = {
    vus: 2,
    duration: '5s'
};

export default function() {
    let home_page = `${urls.base_url}`;
    let home_page_response = http.get(home_page);
    check(home_page_response, {
        'Home page is 200:': (r) => r.status === 200,
        'Home page has news card:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let category_list_page = `${urls.base_url}${urls.categories_list}`;
    let category_list_page_response = http.get(category_list_page);
    check(category_list_page_response, {
        'Category list page is 200:': (r) => r.status === 200,
        'Category list page has category card:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let category_news_page = `${urls.base_url}${urls.category_news(1)}`;
    let category_news_page_response = http.get(category_news_page);
    check(category_news_page_response, {
        'Category news page is 200:': (r) => r.status === 200,
        'Category news page has news card:': (r) => r.body.includes('news-card'),
    });
    sleep(1);

    let news_details_page = `${urls.base_url}${urls.news_details(1)}`;
    let news_details_page_response = http.get(news_details_page);
    check(news_details_page_response, {
        'News details page is 200:': (r) => r.status === 200,
        'News details page has news title:': (r) => r.body.includes('news-detail-title'),
    });
    sleep(1);

    let news_page = `${urls.base_url}${urls.news}`;
    let news_page_response = http.get(news_page);
    check(news_page_response, {
        'News page is 200:': (r) => r.status === 200,
        'News page has news card:': (r) => r.body.includes('news-card'),
    });
    sleep(1);
}