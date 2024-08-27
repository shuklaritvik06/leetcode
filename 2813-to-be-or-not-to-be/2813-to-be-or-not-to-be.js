/**
 * @param {string} val
 * @return {Object}
 */
const evaluateCondition = (value, target, conditionType) => {
    const isMatch = value === target;
    if (conditionType === "equal" ? isMatch : !isMatch) {
        return true;
    }
    const errorPrefix = conditionType === "equal" && !isMatch ? "Not " : "";
    throw new Error(`${errorPrefix}Equal`);
};

var expect = function (val) {
    return {
        toBe: (target) => evaluateCondition(val, target, "equal"),
        notToBe: (target) => evaluateCondition(val, target, "notEqual"),
    }
};
/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */