/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
    let grouping = {}
    this.map((item) => {
        const key = fn(item)
        if (grouping[key]) {
            const elements = grouping[key]
            elements.push(item)
        } else {
            grouping[key] = [item]
        }
    })
    return grouping
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */