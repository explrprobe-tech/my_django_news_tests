import { BaseApi } from "./base_api.js";
import { urls } from '../config/urls.js'
import { check } from 'k6';


export class HomeApi extends BaseApi {

    constructor(home_endpoint = urls.home
    ) {
        super();
        this.home_endpoint = home_endpoint;
    }

    openHomePage() {
        return this._get(this.home_endpoint)
    }

    checkOpenHomePage(response) {
        return check(response, {
            "Open Home page is 200": (r) => r.status === 200
        })
    }

}