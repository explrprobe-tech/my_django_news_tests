import { testReadersFlow } from './config/scenarios.js'


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
