class SeamlessState {
    constructor(initialState = {}) {
        this.state = initialState;
    }

    setState(key, value) {
        const oldValue = this.state[key];
        this.state[key] = value;
        const stateChangeEvent = new CustomEvent(`stateChange:${key}`, { detail: { oldValue, currentValue: this.state[key] } });
        document.dispatchEvent(stateChangeEvent);
    }

    getState(key) {
        return this.state[key];
    }
}

const initialState = JSON.parse(this.getAttribute('state') || '{}');
seamless.state = new SeamlessState(initialState);
