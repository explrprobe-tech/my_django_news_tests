import http from 'k6/http'
import { urls } from '../config/urls.js'


export class BaseApi {
    constructor(base_url=urls.base_url) {
        this.base_url = base_url;
        this.session = http;
    }

    _get(endpoint) {
        let url = `${this.base_url}${endpoint}`;
        return this.session.get(url)
    }

    getCsrfToken(endpoint) {
        let get_response = this._get(endpoint);
        let match = get_response.body.match(/name="csrfmiddlewaretoken" value="([^"]+)"/);
        return match ? match[1] : '';
    }

    _post(endpoint, data, need_csrf=true) {
        let url = `${this.base_url}${endpoint}`;
        let requestData = need_csrf ? {...data, csrfmiddlewaretoken: this.getCsrfToken(endpoint)} : data;
        return this.session.post(url, requestData, { redirects: 0 })
    }

    
}