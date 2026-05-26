import { readersFlow } from './config/scenarios.js'


export { readersFlow };

export let options = {
    scenarios: {
        readers: {
            executor: 'ramping-vus',
            startVUs: 0,
            stages: [
                { duration: '5s', target: 2 },
                { duration: '5s', target: 5 },
            ],
            exec: 'readersFlow',
        }
    },
    thresholds: {
        http_req_duration: ['p(95) < 300'],
        http_req_failed: ['rate < 0.005'],
    }
};
