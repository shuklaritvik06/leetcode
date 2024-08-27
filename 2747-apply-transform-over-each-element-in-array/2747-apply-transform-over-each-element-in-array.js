/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    result = []
    for (let i of arr) {
        result.push(fn(i, arr.indexOf(i)))
    }
    return result
};