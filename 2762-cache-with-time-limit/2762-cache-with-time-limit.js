var TimeLimitedCache = function () {
    this.cache = {}
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
    let flag = false;
    if (this.cache[key]) {
        flag = true;
        const prev_entry = this.cache[key];
        clearTimeout(prev_entry[1]);
    }
    const timeout = setTimeout(() => {
        delete this.cache[key];
    }, duration);
    this.cache[key] = [value, timeout]
    return flag;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
    if (this.cache[key]) {
        return this.cache[key][0]
    }
    return -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
    return Object.keys(this.cache).length
};

