import { testReadersFlow } from './config/scenarios.js';
import { jUnit, textSummary } from 'https://k6.io';


export { testReadersFlow };

export let options = {
    scenarios: {
        readers: {
            executor: 'constant-vus',
            vus: 2,
            duration: '5s',
            exec: 'testReadersFlow'
        }
    }
};

export function handleSummary(data) {
    return {
        'stdout': textSummary(data, { indent: ' ', enableColors: true}),
        'allure-results-k6/results.xml': jUnit(data, { name: 'k6 Average Load Tests'})
    };
}