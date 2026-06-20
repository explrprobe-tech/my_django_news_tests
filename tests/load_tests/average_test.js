import { testReadersFlow, testEditorFlow, testAdminFlow } from './config/scenarios.js'
import { jUnit, textSummary } from 'https://k6.io'


export { testReadersFlow, testEditorFlow, testAdminFlow };

export let options = {
    scenarios: {
        readers: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '5s', target: 10 },
                { duration: '10s', target: 50 },
                { duration: '10s', target: 80 },
                { duration: '5s', target: 0 },
            ],
            exec: 'testReadersFlow',
        },
        editors: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '2s', target: 2},
                { duration: '10s', target: 4},
                { duration: '10s', target: 5},
                { duration: '5s', target: 0},
            ],
            exec: 'testEditorFlow',
        },
        admins: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                {duration: '2s', target: 1},
                {duration: '10s', target: 2},
                {duration: '10s', target: 2},
                {duration: '5s', target: 0},
            ],
            exec: 'testAdminFlow',
        }
    },
    thresholds: {
        http_req_duration: ['p(95) < 300'],
        http_req_failed: ['rate < 0.005'],
    }
};

export function handleSummary(data) {
    return {
        'stdout': textSummary(data, { indent: ' ', enableColors: true}),
        'allure-results-k6/results.xml': jUnit(data, { name: 'k6 Average Load Tests'})
    };
}