
export const urls = {
    base_url: __ENV.BASE_URL || "http://localhost:8000",

    home: '/',
    login: '/login/',
    register: '/register/',
    secret: '/secret/',

    categories_list: '/category/',
    category_news: (id) => `/category/${id}/`,
    add_category: '/category/add_category/',

    news: '/news/',
    news_details: (id) => `/news/${id}/`,
    add_news: '/news/add_news/',
    edit_news: (id) => `/news/${id}/edit/`
}