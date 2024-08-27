class EventEmitter {
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    constructor() {
        this.events = new Map()
    }
    subscribe(eventName, callback) {
        if (!this.events.has(eventName)) {
            this.events.set(eventName, [])
        }
        const listeners = this.events.get(eventName)
        listeners.push(callback)
        return {
            unsubscribe: () => {
                const index = listeners.indexOf(callback)
                listeners.splice(index, 1)
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const listeners = this.events.get(eventName)
        if(listeners){
            return listeners.map((cb) => cb(...args));
        }
        return []
    }
}