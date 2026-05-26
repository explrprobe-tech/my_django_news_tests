import { readersFlow } from './config/scenarios.js'


export { readersFlow };

export let options = {
    scenarios: {
        readers: {
            executor: 'constant-vus',
            vus: 2,
            duration: '5s',
            exec: 'readersFlow'
        }
    }
};
