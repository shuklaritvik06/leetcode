/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    result = [];
    i = 0;
    while (i <= arr.length - 1) {
        result.push(arr.slice(i, i + size));
        if ((i + size) <= arr.length - 1) {
            i += size;
        } else {
            i = arr.length;
        }
    }
    return result;
};
