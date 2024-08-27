/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    prevNumber = n - 1
    return function() {
        current = prevNumber + 1
        prevNumber = current
        return current
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */