import { BaseApi } from "./base_api.js";
import { urls } from '../config/urls.js';
import { check } from 'k6';



export class LoginApi extends BaseApi {

    constructor(login_endpoint=urls.login) {
            super();
            this.login_endpoint = login_endpoint;
    }

    openLoginPage() {
        return this._get(this.login_endpoint);
    }

    checkOpenLoginPage(response) {
        return check(response, {
            "Open Login page is 200": (r) => r.status === 200
        });
    }

    login(data_user) {
        return this._post(this.login_endpoint, data_user);
    }

    checkLogin(response) {
        return check(response, {
            "Login is 302": (r) => r.status === 302,
        });
    }

}