/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    value_map = {}
    return function(...args) {
        let key = args.toString()
        if(value_map[key]===undefined){
            output = fn(...args)
            value_map[key] = output
            return output
        }
        return value_map[key]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */