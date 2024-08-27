class EventEmitter {
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscriptions = [];
    subscribe(eventName, callback) {
        this.subscriptions.push({ eventName, callback });
        return {
            unsubscribe: () => {
                this.subscriptions = this.subscriptions.filter((item) => item.callback !== callback);
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        let isMatch = this.subscriptions.filter((item) => item.eventName === eventName);
        if (isMatch) {
            return isMatch.map((item) => item.callback(...args));
        }
    }
}